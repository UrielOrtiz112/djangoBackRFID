from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from alumno.models import alumno
from alumno.serializers import AlumnoSerializer

# Create your views here.
class AlumnoList(APIView):
    def get(self, request, format=None):
        queryset = alumno.objects.all()
        serializer = AlumnoSerializer(queryset, many=True, context = {'request':request})
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AlumnoSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response (datas)
        return Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)
class AlumnoDetail(APIView):
    def get_object(self,pk):
        try: 
            return alumno.objects.get(pk=pk)
        except alumno.DoesNotExist:
            raise Http404
    def get(self, request,pk, format=None):
        alumno = self.get_object(pk) 
        serializer = AlumnoSerializer(alumno)
        return Response(serializer.data) 
    def put(self, request,pk, format=None):
        alumno = self.get_object(pk)
        serializer = AlumnoSerializer(alumno, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        alumno = self.get_object(pk)
        alumno.delete()
        return Response('Eliminado')

