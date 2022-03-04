from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choice(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
        return code

# Create your models here.
class Room(models.model):
    code = models.CharField(Max_Length=8, default="",unique=True)
    host = models.CharField(Max_Length=50,unique=True)
    guest_can_pause = models.BooleanField(null=False, dafault=false)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
