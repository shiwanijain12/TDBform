from django.db import models

# Create your models here.
class Participant(models.Model):
    id=models.IntegerField(primary_key=True)
    member1_name=models.CharField(max_length=20)
    member1_phone=models.IntegerField()
    member1_email=models.EmailField(max_length=200)
    member2_name=models.CharField(max_length=20)
    member2_phone=models.IntegerField()
    member2_email=models.EmailField(max_length=200)
    member3_name=models.CharField(max_length=20)
    member3_phone=models.IntegerField()
    member3_email=models.EmailField(max_length=200)
    member4_name=models.CharField(max_length=20)
    member4_phone=models.IntegerField()
    member4_email=models.EmailField(max_length=200)
