import json, requests, time, random
from users.utils import make_signature
import jwt
from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import action, permission_classes
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import User
from .serializers import UserSerializer
from .permissions import IsSelf

class UsersViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        elif (
            self.action == "create"
            or self.action == "retrieve"
        ):
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsSelf]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode(
                {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
            )
            return Response(data={"token": encoded_jwt, "id": user.pk})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
    def send_sms(self, phone_number, auth_number):
        timestamp = str(int(time.time() * 1000))
        headers = {
            'Content-Type': "application/json; charset=UTF-8", # 네이버 참고서 차용
            'x-ncp-apigw-timestamp': timestamp, # 네이버 API 서버와 5분이상 시간차이 발생시 오류
            'x-ncp-iam-access-key': 'UrjpWBfDQDc62KN1SPDS',
            'x-ncp-apigw-signature-v2': make_signature()
        }
        body = {
            "type": "SMS",
            "contentType": "COMM",
            "from": "01072441542",
            "content": f"[인증번호:{auth_number}]",
            "messages": [{"to": f"{phone_number}"}]
        }
        body = json.dumps(body)
        requests.post('https://sens.apigw.ntruss.com/sms/v2/services/ncp:sms:kr:271291744572:halfdelivery_auth/messages', headers=headers, data=body)

    @action(detail=False, methods=["post"])
    def inputsms(self, request):
        try:
            input_phone_num = request.data.get('phone_number')
            auth_num = random.randint(1000, 10000)
            auth_mobile = User.objects.get(phone_number=input_phone_num)
            auth_mobile.auth_number = auth_num
            auth_mobile.save()
            self.send_sms(phone_number=request.data.get('phone_number'), auth_number=auth_num)
            return Response(data={'message': '인증번호 발송완료'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            User.objects.create(
                phone_number = input_phone_num,
                auth_number = auth_num
            ).save()
            self.send_sms(phone_number=input_phone_num, auth_number=auth_num)
            return Response(data={'message': '인증번호 발송 및 DB 입력완료'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def smsverification(self, request):
        try:
            verification = User.objects.get(phone_number=request.data.get('phone_number'))
            if verification.auth_number == int(request.data.get('auth_number')):
                return Response(data={'message': '인증 완료되었습니다.'}, status=status.HTTP_200_OK)
            else:
                return Response(data={'message': '인증 실패입니다.'}, status=400)
        
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
