
from rest_framework import serializers
from .models import Fees, Students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class FeesSerializer(serializers.ModelSerializer):
    # post request can be made against the pk value of existing modal ie. Students Modal
    student = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Students.objects.all())
    class Meta:
        model = Fees
        fields = '__all__'

