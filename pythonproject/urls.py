from django.contrib import admin
from django.urls import path,include
from pythonapplication import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pythonapplication.urls')),
    path('home/',include('pythonapplication.urls')),
    path('contact/',include('pythonapplication.urls')),
    path('contactcode/',include('pythonapplication.urls')),
    path('register/',include('pythonapplication.urls')),
    path('registercode/',include('pythonapplication.urls')),
    path('login/',include('pythonapplication.urls')),
    path('logincode/',include('pythonapplication.urls')),
    path('admin1/',include('pythonapplication.urls')),
    path('user1/',include('pythonapplication.urls')),
    path('about/',include('pythonapplication.urls')),
    path('services/',include('pythonapplication.urls')),
    path('feedback/',include('pythonapplication.urls')),
    path('feedbackcode/',include('pythonapplication.urls')),
    path('showfeedback/',include('pythonapplication.urls')),
    path('addservice/',include('pythonapplication.urls')),
    path('addservicecode/',include('pythonapplication.urls')),
    path('showuser/',include('pythonapplication.urls')),
    path('showservices/',include('pythonapplication.urls')),
    path('addfeedback/',include('pythonapplication.urls')),
    path('addfeedbackcode/',include('pythonapplication.urls')),
    path('showaddfeedback/',include('pythonapplication.urls')),
    path('logout/',include('pythonapplication.urls')),
    path('delete_user/',include('pythonapplication.urls')),
    path('delete_feedback/',include('pythonapplication.urls')),
    path('delete_addfeedback/',include('pythonapplication.urls')),
    path('delete_services/',include('pythonapplication.urls')),
    path('showuserservices/',include('pythonapplication.urls')),
    path('updateuser/',include('pythonapplication.urls')),
    path('saveuser/',include('pythonapplication.urls')),
    path('updatefeedback/',include('pythonapplication.urls')),
    path('updateservices/',include('pythonapplication.urls')),
    path('savefeedback/',include('pythonapplication.urls')),
    path('saveservices/',include('pythonapplication.urls')),

]
