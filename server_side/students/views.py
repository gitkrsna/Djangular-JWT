from .serializers import FeesSerializer, StudentsSerializer
from .models import Fees, Students
from .ContextViewSet import ViewSet
# Create your views here.
class StudentsViewSet(ViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    
class FeesViewSet(ViewSet):
    queryset = Fees.objects.all()
    serializer_class = FeesSerializer    