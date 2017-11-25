from django.conf.urls import url
from persona.views import  persona, personas

urlpatterns = [
    
   url(r'^/$', personas ),
   url(r'^(?P<persona_id>\d+)/$', persona, name='persona_url' ),
    
]