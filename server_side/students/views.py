from rest_framework.viewsets import GenericViewSet
from .serializers import FeesListSerializer, FeesSubmitSerializer, StudentsSerializer
from .models import Fees, Students
from .ContextViewSet import ViewSet
from rest_framework import generics, mixins
# Create your views here.
class StudentsViewSet(ViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    
class FeesListViewSet(mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Fees.objects.all()
    serializer_class = FeesListSerializer   

class FeesSubmitViewSet(mixins.CreateModelMixin,GenericViewSet):
    queryset = Fees.objects.all()
    serializer_class = FeesSubmitSerializer 