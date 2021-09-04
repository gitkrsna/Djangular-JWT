from .serializers import StudentsSerializer
from .models import Students
from .ContextViewSet import ViewSet
# Create your views here.
class StudentsViewSet(ViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    