from django.db import models


class ViberUser(models.Model):
	name=models.CharField(max_length=128,null=True, blank=True)
	viber_id=models.CharField(max_length=24)
	country=models.CharField(max_length=2, null=True, blank=True)
	is_active=models.BooleanField(null=True, blank=True)
	is_active=models.BooleanField(null=True, blank=True)
	api_version=models.PositiveSmallIntegerField(null=True, blank=True)
	create_date=models.DateTimeField(auto_now_add=True, null=True)
	phone_number=models.CharField(max_length=16, null=True, blank=True)
	avatar=models.ImageField(upload_to='avatars', null=True, blank=True)
	primary_device_os=models.CharField(max_length=24,null=True, blank=True)
	device_type=models.CharField(max_length=24,null=True, blank=True)
	viber_version=models.CharField(max_length=8,null=True, blank=True)

	def __str__(self):
		return self.name

class Message(models.Model):
	text=models.TextField()
	timestamp=models.DateTimeField()
	user=models.ForeignKey("ViberUser", on_delete=models.SET_NULL, null=True)

		
# Create your models here.
