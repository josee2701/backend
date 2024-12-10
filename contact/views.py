import json

from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.response import Response

from config.settings import EMAIL_HOST_USER

from .forms import ContactForm
from .models import Contact
from .serializers import ContactSerializer


class ContactSerializerViewSet(viewsets.ModelViewSet):
    """
    ViewSet para manejar las operaciones CRUD de ContactSerializer y enviar correos electrónicos.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            # Obtener los datos del formulario
            name = contact.name
            apellido = contact.apellido
            email = contact.email
            phone = contact.phone
            message = contact.message

            try:
                # Enviar correo a tu dirección personal
                send_mail(
                    'Nuevo mensaje de contacto',
                    f'Nombre: {name} {apellido}\nEmail: {email}\nTeléfono: {phone}\n\nMensaje:\n{message}',
                    EMAIL_HOST_USER,
                    [EMAIL_HOST_USER],
                    fail_silently=False,
                )

                # Renderizar plantilla para el correo de confirmación
                confirmation_html_message = render_to_string('confirmation_email.html', {
                    'name': name,
                    'apellido': apellido,
                })

                # Enviar correo de confirmación al usuario
                confirmation_email = EmailMessage(
                    'Confirmación de recepción de mensaje',
                    confirmation_html_message,
                    EMAIL_HOST_USER,
                    [email],
                )
                confirmation_email.content_subtype = 'html'
                confirmation_email.send()

                return Response(
                    {'message': 'Mensaje enviado con éxito'},
                    status=status.HTTP_201_CREATED
                )

            except Exception as e:
                return Response(
                    {'error': f'Ocurrió un error al enviar los correos: {str(e)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
@method_decorator(csrf_exempt, name='dispatch')
class ContactView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        form = ContactForm(data)
        
        if form.is_valid():
            contact = form.save()

            # Obtener los datos del formulario
            name = contact.name
            apellido = contact.apellido
            email = contact.email
            phone = contact.phone
            message = contact.message

            # Enviar correo a tu dirección personal
            send_mail(
                'Nuevo mensaje de contacto',
                f'Nombre: {name} {apellido}\nEmail: {email}\nTeléfono: {phone}\n\nMensaje:\n{message}',
                EMAIL_HOST_USER,
                [EMAIL_HOST_USER],
                fail_silently=False,
            )

            # Renderizar plantilla para el correo de confirmación
            confirmation_html_message = render_to_string('confirmation_email.html')

            # Enviar correo de confirmación al usuario
            confirmation_email = EmailMessage(
                'Confirmación de recepción de mensaje',
                confirmation_html_message,
                EMAIL_HOST_USER,
                [email]
            )
            confirmation_email.content_subtype = 'html'
            confirmation_email.send()

            return JsonResponse({'message': 'Mensaje enviado con éxito'}, status=201)
        else:
            return JsonResponse(form.errors, status=400)
    
    def get(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Método no permitido'}, status=405)
