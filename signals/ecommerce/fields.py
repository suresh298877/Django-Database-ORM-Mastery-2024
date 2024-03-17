from django.db import models

class ProductIdField(models.CharField):

    description='alskdfjalsdfasdkfj alksdfj aslkdf'

    def __init__(self,*args,**kwargs):
        kwargs['max_length']=10
        kwargs['unique']=True
        kwargs['null']=True
        super().__init__(*args,**kwargs)