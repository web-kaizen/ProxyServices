from django.urls import path

from bots.views import BotDetailsView, BotListView


urlpatterns = [
    path('', BotListView.as_view(), name='bot-list'),
    path('<int:bot_id>/', BotDetailsView.as_view(), name='bot-details'),
]
