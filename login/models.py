from ast import Pass
from inspect import trace
from django.db import models
from django.db.models import Q
import hashlib


class User(models.Model):

    user_id = models.CharField(max_length=20, unique=True)
    hashed_password = models.CharField(max_length=64)
    last_login = models.DateTimeField('last login')
    
    def logincheck(request):

        print(request.POST['user_id'])
        print(hashlib.sha256(str(request.POST['password']).encode('utf-8')).hexdigest())

        try :

            query = User.objects.get( Q(user_id=request.POST['user_id']) & Q(hashed_password=hashlib.sha256(str(request.POST['password']).encode('utf-8')).hexdigest()) )
            return query

        except(KeyError, User.DoesNotExist):
            
            return False
    
    def __str__(self):
        return self.user_id
