from config.settings import AUTH_PASSWORD_VALIDATORS
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# ? 채팅시, 메시지들 저장할 모델들.
class Message(models.Model):
    author = models.ForeignKey(User, related_name="author_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages(self):
        return Message.objects.order_by("-timestamp").all()[:10]  # ? 최근 10개 메시지 기본으로 로딩.
