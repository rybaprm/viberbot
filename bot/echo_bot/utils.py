from viberbot.api.bot_configuration import BotConfiguration

from django.conf import settings

from viberbot import Api

from .models import ViberUser

bot_conf = BotConfiguration(
    name = 'ViberBotBrain',
    avatar = 'https://www.velvet.by/files/userfiles/309/velvet__2_177.jpg',
    auth_token = settings.VIBER_AUTH_TOKEN,
)

viber = Api(bot_conf)


#def get_or_create_viber_user(viber_id, name):
#		viber_user=ViberUser.objects.update_or_create(
#				viber_id=viber_id,
#					defaults={
#						'name':name,
#						'is_active':True
#					}
#			)
#		return viber_user
		
def get_or_create_viber_user(viber_id, is_active=True):
		viber_user, created=ViberUser.objects.update_or_create(
				viber_id=viber_id,
					defaults={
						#'name':name,
						'is_active':True
					}
			)
		if created:
			user_details=viber.get_user_details (viber_id)
			viber_user.name=user_details.get('name', None)
			viber_user.country=user_details.get('country', None)
			viber_user.api_version=user_details.get('api_version', None)
			viber_user.primary_device_os=user_details.get('primary_device_os', None)
			viber_user.device_type=user_details.get('device_type', None)
			viber_user.viber_version=user_details.get('viber_version', None)
			viber_user.avatar=user_details.get('avatar', None)
			
		
		viber_user.is_active=is_active
		viber_user.save()	
		return viber_user		