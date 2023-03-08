from rest_framework.generics import RetrieveUpdateAPIView

from resume.models import Resume
from resume.permissions import IsOwner
from resume.serializers import ResumeRetrieveSerializer


class ResumeViews(RetrieveUpdateAPIView):
    #service
    http_method_names = ['get', 'patch']
    queryset = Resume.objects.all()
    permission_classes = [IsOwner]
    serializer_class = ResumeRetrieveSerializer