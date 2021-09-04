from django.http import response
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class ViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return_response = {"success": "true", "status": status.HTTP_200_OK}
        return Response(return_response, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return_response = {"message": "updated successfully", "status": status.HTTP_200_OK}
        return Response(return_response)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return_response = {"message": "deleted successfully", "status": status.HTTP_200_OK}
        return Response(return_response)    