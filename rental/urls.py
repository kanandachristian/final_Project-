from django.conf.urls import url
from django.views.generic import TemplateView
from rental import views

urlpatterns = [
    url(r'^register/?', views.register_form, name='register'),
    url(r'^login/?', views.login_form, name='login'),
    url(r'^signup/?', views.signup_form, name='signup'),
    url(r'^contact_us/?', views.contact_form, name='contact_us'),
    url(r'^SearchResults/?', views.search_result_form, name='searchresult'),
    url(r'^searching/?', views.search, name='search'),
    url(r'^book/?', views.book_form, name='book'),
    # url(r'^All-Renting-Properties/?', views.secondpage, name='second_page'),
    url(r'^post_property/?', views.postproperty, name='post_property'),


    url(r'^$', views.home_page, name='home_page'),

    url(r'^(?P<category_slug>[-\w]+)/$',
        views.secondpage, name='property_list_by_category'),

    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.thirdpage, name='property_detail'),

    # url(r'^(?P<type_slug>[-\w]+)/$',
    #     views.advert, name='property_list_by_type'),

    url(r'^Other_properties',
        views.ByType, name='by_type')

]
