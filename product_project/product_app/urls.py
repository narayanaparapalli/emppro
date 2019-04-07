from django.conf.urls import url,include
from product_app import views

urlpatterns=[
    #url(r'^$',views.home1),
    url(r'^home/',views.home),
    url(r'^insert/',views.insert),
    url(r'^display/',views.display),
    url(r'^update/',views.update),
    url(r'^delete/',views.delete),
    url(r'^reg/',views.reg),
    url(r'login/',views.login)
]