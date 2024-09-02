from django.contrib import admin
from django.urls import path
from pythonapplication import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first),
    path('home/',views.home),
    path('contact/',views.contact),
    path('contactcode/',views.contactcode),
    path('register/',views.register),
    path('registercode/',views.registercode),
    path('login/',views.login),
    path('logincode/',views.logincode),
    path('admin1/',views.admin1),
    path('user1/',views.user1),
    path('about/',views.about),
    path('services/',views.services),
    path('feedback/',views.feedback),
    path('feedbackcode/',views.feedbackcode),
    path('showfeedback/',views.showfeedback),
    path('addservice/',views.addservice),
    path('addservicecode/',views.addservicecode),
    path('showuser/',views.showuser),
    path('showservices/',views.showservices),
    path('addfeedback/',views.addfeedback),
    path('addfeedbackcode/',views.addfeedbackcode),
    path('showaddfeedback/',views.showaddfeedback),
    path('logout/',views.logout),
    path('delete_user/<int:pk>/',views.delete_user, name="delete_user"),
    path('delete_feedback/<int:pk>/',views.delete_feedback, name="delete_feedback"),
    path('delete_userfeedback/<int:pk>/',views.delete_userfeedback, name="delete_userfeedback"),
    path('delete_services/<int:pk>/',views.delete_services, name="delete_services"),
    path('showuserservices/',views.showuserservices),
    path('updateuser/<int:pk>/',views.updateuser, name="updateuser"),
    path('updatefeedback/<int:pk>/',views.updatefeedback, name="updatefeedback"),
    path('updateservices/<int:pk>/',views.updateservices, name="updateservices"),
    path('savefeedback/',views.savefeedback),
    path('saveservices/',views.saveservices),
    path('saveuser/',views.saveuser),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
