from django.http import HttpResponse, JsonResponse

from viberbot.api.viber_requests import ViberMessageRequest, ViberSubscribedRequest, ViberUnsubscribedRequest, ViberConversationStartedRequest

from viberbot.api.messages import TextMessage, PictureMessage, KeyboardMessage, ContactMessage

from ..utils import viber, get_or_create_viber_user

from . massages_json import WELCOME_MESSAGE_PICTURE, WEATHER_KEYBOARD, GET_PHONE_NUMBER_KEYBOARD_BUTTON

from . openweathermap import print_weather_for_day

def message_processing(viber_request):
	if isinstance(viber_request, ViberMessageRequest):
		get_or_create_viber_user(viber_request.sender.id)
	elif isinstance(viber_request, ViberSubscribedRequest):
		get_or_create_viber_user(viber_request.user.id)
	elif isinstance(viber_request, ViberConversationStartedRequest):
		if viber_request.subscribed==True:
			get_or_create_viber_user(viber_request.user.id)
	elif isinstance(viber_request, ViberUnsubscribedRequest):
		get_or_create_viber_user(viber_request.user_id, False)
		
	if isinstance(viber_request, ViberMessageRequest):
		if isinstance(viber_request.message,ContactMessage):
			if viber_request.message.tracking_data.split('|')[0] == 'share-phone':
				viber.send_messages(viber_request.sender.id,TextMessage(text='Погода для города '+viber_request.message.tracking_data.split('|')[1]))
				viber.send_messages(viber_request.sender.id, TextMessage(text=print_weather_for_day(viber_request.message.tracking_data.split('|')[1])))
				viber.send_messages(viber_request.sender.id,TextMessage(text='Привет. Начнем общение... Выбери тему:'))
				viber.send_messages(viber_request.sender.id,WEATHER_KEYBOARD())
		if isinstance(viber_request.message,TextMessage):
			if viber_request.message.tracking_data == None:
				viber.send_messages(viber_request.sender.id,TextMessage(text='Привет. Начнем общение... Выбери тему:'))
				viber.send_messages(viber_request.sender.id,WEATHER_KEYBOARD())
			if viber_request.message.tracking_data.split('|')[0] == 'share-phone':
				viber.send_messages(viber_request.sender.id,GET_PHONE_NUMBER_KEYBOARD_BUTTON(viber_request.message.tracking_data))
			if viber_request.message.tracking_data == 'weather' and viber_request.message.text == 'weather':
				viber.send_messages(viber_request.sender.id, TextMessage(tracking_data ='what_weater', text='Введите город для котогоро нужно получить погоду'))
			if viber_request.message.tracking_data == 'weather' and not viber_request.message.text == 'weather':
				viber.send_messages(viber_request.sender.id,TextMessage(text='Вы не выберли тему:'))
				viber.send_messages(viber_request.sender.id,TextMessage(text='Выбери тему ещё раз:'))
				viber.send_messages(viber_request.sender.id,WEATHER_KEYBOARD())
			if viber_request.message.tracking_data == 'what_weater':
				viber.send_messages(viber_request.sender.id, TextMessage(text=print_weather_for_day(viber_request.message.text)))
				viber.send_messages(viber_request.sender.id,WEATHER_KEYBOARD())
			if viber_request.message.text == 'СТОП':
				viber.send_messages(viber_request.sender.id,TextMessage(text='Bot now stop...'))
				viber.unset_webhook()
	elif isinstance(viber_request, ViberConversationStartedRequest):
		if viber_request.subscribed==True:
			if not viber_request.context == None:
				viber.send_messages(viber_request.user.id,TextMessage(text='Погода для города '+viber_request.context))
				viber.send_messages(viber_request.user.id,TextMessage(text=print_weather_for_day(viber_request.context)))
				viber.send_messages(viber_request.user.id,TextMessage(text='Привет. Начнем общение... Выбери тему:'))
				viber.send_messages(viber_request.user.id,WEATHER_KEYBOARD())
			else:
				viber.send_messages(viber_request.user.id,TextMessage(text='Привет. Начнем общение... Выбери тему:'))
				viber.send_messages(viber_request.user.id,WEATHER_KEYBOARD())
			#viber.send_messages(viber_request.user.id,TextMessage(text='Привет. Начнем общение... Выбери тему:'))
			#viber.send_messages(viber_request.user.id,WEATHER_KEYBOARD())
		elif viber_request.subscribed==False:
			return JsonResponse(WELCOME_MESSAGE_PICTURE(viber_request.context))