from django.conf import settings

from django.views import View

from django.http import HttpResponse, JsonResponse

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt

from django.views.generic import TemplateView

from viberbot.api.viber_requests import ViberMessageRequest, ViberSubscribedRequest, ViberUnsubscribedRequest, ViberConversationStartedRequest

from viberbot.api.messages import TextMessage, PictureMessage, KeyboardMessage, ContactMessage

from .utils import viber, get_or_create_viber_user

from . services.massages_json import WELCOME_MESSAGE_PICTURE, WEATHER_KEYBOARD

from . services.openweathermap import print_weather_for_day

from . services.message_processing import message_processing


#from .models import ViberUser








	
class SetWebhookView(View):
	def get(self, request, *args, **kwargs):
		event_types=['subscribed', 'unsubscribed', 'conversation_started']
		viber.set_webhook(
		url='https://'+settings.ALLOWED_HOSTS[0]+'/viber/callback/', webhook_events=event_types,
		)
		return HttpResponse(status=200)

class UnsetWebhookView(View):
	def get(self, request):
		viber.unset_webhook()
		return HttpResponse(status=200)

@method_decorator(csrf_exempt, name='dispatch')
class CallbackView(View):
	def post(self, request):
		viber_request = viber.parse_request(request.body)
		print(viber_request)
		messageprocessing=message_processing(viber_request)
		if isinstance(messageprocessing,JsonResponse):
			return messageprocessing
		



		
		#viber.send_messages(viber_request.sender.id, TextMessage(text=print_weather_for_day(viber_request.message.text)))		
		return HttpResponse(status=200)

class TestView(TemplateView):
	template_name='echo_bot/test.html'