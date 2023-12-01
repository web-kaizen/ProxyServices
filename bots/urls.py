from django.urls import path

from bots.views import BotDetailsView, BotListView

urlpatterns = [
    path('list/', BotListView.as_view(), name='bot-list'),
    path('details/<int:bot_id>', BotDetailsView.as_view(), name='bot-details'),
]
