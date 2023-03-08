from django.urls import path

from resume.views import ResumeViews


urlpatterns = [
    path('<int:pk>', ResumeViews.as_view(), name='resume')
]
