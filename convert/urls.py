from django.conf.urls import include, url
from django.views.generic import TemplateView
from convert import views

urlpatterns = [
    url(r'convers/?', views.events, name='conv1'),
    url(r'converted/?', views.actionconv, name='conv2'),
    url(r'conE', TemplateView.as_view(
        template_name='converterError.html'), name='Error')
]
