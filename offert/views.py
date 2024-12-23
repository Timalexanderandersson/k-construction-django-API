from django.shortcuts import render
from .serializers import OffertSerializers
from rest_framework import generics, status 
from django.http import Http404
from rest_framework.response import Response
from django.core.mail import send_mail


from .models import Offert

# Create your views here.

class PostOffert(generics.ListCreateAPIView):
    serializer_class = OffertSerializers
    queryset = Offert.objects.all()

    def post(self, request):
      serializer = OffertSerializers(data=request.data)
      if serializer.is_valid():
        mail = serializer.save()
        self.send_email(mail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def send_email(self, mail):
       subject = f'Offert from: {mail.name}'
       message = (
        f'Phone number: {mail.phone_number}\n\n'
        f'Category: {mail.option_service}\n\n'
        f'Work description: {mail.job_description}\n'
        f'Mail sent from: {mail.epost}\n\n'
       )
       from_email = 'from@gmail.com'
       recipient_list = ["timovetim@gmail.com"]

       send_mail(
         subject,
         message,
         from_email,
         recipient_list,
         fail_silently=False,
        )