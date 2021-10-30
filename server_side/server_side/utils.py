from rest_framework import status
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import exception_handler

#custom exception handler
from django.core.exceptions import ValidationError as DjangoValidationError

from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.views import exception_handler as drf_exception_handler
from django.http import JsonResponse

def exception_handler(exc, context):
    if isinstance(exc, DjangoValidationError):
        if hasattr(exc, 'message_dict'):
            exc = DRFValidationError(detail={'error': exc.message_dict})
        elif hasattr(exc, 'message'):
            exc = DRFValidationError(detail={'error': exc.message})
        elif hasattr(exc, 'messages'):
            exc = DRFValidationError(detail={'error': exc.messages})
    return drf_exception_handler(exc, context)



def custom404(request, exception=None):
    data = {
        'error': 'The resource was not found (404)',
        'status': status.HTTP_404_NOT_FOUND
    }
    return JsonResponse(data, status = status.HTTP_404_NOT_FOUND)    

def custom500(request, exception=None):
    data = {
        'error': 'Something went wrong. Please try again later (500)',
        'status': status.HTTP_500_INTERNAL_SERVER_ERROR
    }
    return JsonResponse(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)