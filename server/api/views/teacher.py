from django.http import Http404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status

from api.models import TeacherModel
from api.serializers import TeacherSerializer

import uuid

class TeacherDetailView(APIView):

    # Manipulate a particulare teacher: get, create, delete

    def get_object(self, pk):
        try:
            return TeacherModel.objects.get(pk=uuid.UUID(pk))
        except:
            raise Http404

    def get(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TeacherListView(generics.ListCreateAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializer