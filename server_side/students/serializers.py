
from rest_framework import serializers
from .models import Fees, Students

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class FeesListSerializer(serializers.ModelSerializer):
    student = StudentsSerializer(read_only=True, many=False)
    class Meta:
        model = Fees
        fields = ('student', 'amount', 'fees_month')

class FeesSubmitSerializer(serializers.ModelSerializer):
    # post request can be made against the pk value of existing modal ie. Students Modal
    student = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=Students.objects.all())
    class Meta:
        model = Fees
        fields = '__all__'