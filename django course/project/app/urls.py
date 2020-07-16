from django.urls import include, path
from app import views
 
app_name = 'app'
 
urlpatterns = [
     path('contact_form',views.contact_form,name='contact_form'),
     path('about',views.about,name='about'),
     path('contact',views.contact,name='contact'),
     path('contact_form_submit',views.contact_form_submit,name='contact_form_submit'),
     path('all_data',views.all_data,name='all_data'),
     path('portfolio',views.portfolio,name='portfolio'),




]
