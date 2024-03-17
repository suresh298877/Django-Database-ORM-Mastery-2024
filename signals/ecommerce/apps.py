from django.apps import AppConfig
from django.db.models.signals import post_save

def example_reciever(sender,**kwargs):
    print('Instance is saved')


class EcommerceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce'

    def ready(self)->None:
        post_save.connect(example_reciever)