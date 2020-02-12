from viberbot.api.messages import TextMessage, PictureMessage, KeyboardMessage, ContactMessage

def WELCOME_MESSAGE_PICTURE(viber_request_context):
	WELCOME_MESSAGE_PICTURE = {
			"min_api_version":"3",
			"sender":{
				"name":"ViberBotBrain",
				"avatar":"https://www.velvet.by/files/userfiles/309/velvet__2_177.jpg"
			},
			"tracking_data":"share-phone|"+viber_request_context,
	#		"type":"text",
	#		"text":"Привет в нашем боте...",
			"type":"picture",
			"text":"Привет в нашем боте...",
			"media":"https://www.velvet.by/files/userfiles/309/velvet__2_177.jpg",
			"thumbnail":"https://www.velvet.by/files/userfiles/309/velvet__2_177.jpg",
			"keyboard":{
				"Type":"keyboard",
				#"DefaultHeight":True,
				"Buttons":[
					{
					"ActionType":"share-phone",
					"Silent":True,
					"ActionBody":"reply",
					"Text":"Подписаться и отправить номер телефона",
					"TextSize":"large"
					}
				]
			}
		}
	return WELCOME_MESSAGE_PICTURE
		
WELCOME_MESSAGE_TEXT = {
		"sender":{
			"name":"ViberBotBrain",
			"avatar":"https://www.velvet.by/files/userfiles/309/velvet__2_177.jpg"
		},
		"tracking_data":"share-phone",
		"type":"text",
		"text":"Привет в нашем боте...",
		"keyboard":{
			"Type":"keyboard",
			#"DefaultHeight":True,
			"Buttons":[
				{
				"ActionType":"share-phone",
				"Silent":True,
				"ActionBody":"reply",
				"Text":"Подписаться и отправить номер телефона",
				"TextSize":"large"
				}
			]
		}
	}
	
def WEATHER_KEYBOARD():
	WEATHER_KEYBOARD = {
	"Type": "keyboard",
	"Buttons": [
			{
			"Columns": 3,
			"Rows": 2,
			"BgColor": "#e6f5ff",
			"BgMedia": "http://link.to.button.image",
			"BgMediaType": "picture",
			"BgLoop": True,
			"ActionType": "reply",
			"ActionBody": "weather",
			"ReplyType": "message",
			#"Text": "Push me!"
			"Text": "Погода"
			}
		]
	}
	message = KeyboardMessage(tracking_data='weather', keyboard=WEATHER_KEYBOARD)
	return message
	
def GET_PHONE_NUMBER_KEYBOARD_BUTTON(viber_request_message_tracking_data):
	GET_PHONE_NUMBER_KEYBOARD_BUTTON = {
		"Type": "keyboard",
		"Buttons": [
			{
			"ActionType": "share-phone",
			"Silent":True,
			"ActionBody": "reply",
			"Text": 'Отправить номер телефона'
			}
		]
	}
	message = TextMessage(min_api_version=3, text= "Для продолжения нам необходим Ваш номер телефона.", tracking_data=viber_request_message_tracking_data, keyboard=GET_PHONE_NUMBER_KEYBOARD_BUTTON)
	return message