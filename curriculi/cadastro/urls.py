from django.conf.urls import url
from . import views

urlpatterns = [
<<<<<<< HEAD
    url(r'^$', views.index, name='index'),
    url(r'^cadastro/save$', views.save, name='save')
]
=======
	url(r'^$', views.index, name = 'index'),
]
>>>>>>> bdcb33a421f4c76d5b4aef65749b1120855a3125
