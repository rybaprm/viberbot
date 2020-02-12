from django.urls import path

from . views import SetWebhookView,CallbackView,UnsetWebhookView,TestView


urlpatterns = [
    path('set/', SetWebhookView.as_view()),
    path('callback/', CallbackView.as_view()),
	path('unset/', UnsetWebhookView.as_view()),
	path('test/', TestView.as_view()),
]