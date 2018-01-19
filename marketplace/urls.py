from django.conf.urls import include,url

urlpatterns = [    
    url(r'^$', views.list_products, name="marketplace")    
]