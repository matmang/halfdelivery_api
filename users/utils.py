import sys
import os
import hashlib
import hmac
import base64
import requests
import time

def make_signature():
    timestamp = int(time.time() * 1000)
    timestamp = str(timestamp)

    access_key = "UrjpWBfDQDc62KN1SPDS"
    secret_key = "iyAvh3lyhjodAomMbhnbQw4RBdNRJp7XnoimXEBq"
    secret_key = bytes(secret_key, 'UTF-8')

    method = "POST"
    uri = "/sms/v2/services/ncp:sms:kr:271291744572:halfdelivery_auth/messages"

    message = method + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
    return signingKey
