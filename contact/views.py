# views.py
import json

from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from config.settings import EMAIL_HOST_USER

from .forms import ContactForm


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

            # Enviar correo de confirmación al usuario
            send_mail(
                'Confirmación de recepción de mensaje',
                'Hemos recibido tu mensaje y nos pondremos en contacto contigo pronto.',
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            return JsonResponse({'message': 'Mensaje enviado con éxito'}, status=201)
        else:
            return JsonResponse(form.errors, status=400)
    
    def get(self, request, *args, **kwargs):
        return JsonResponse({'error': 'Método no permitido'}, status=405)
