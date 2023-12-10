from django.urls import path

from dialogues.views import DialoguesView

urlpatterns = [
    path('', DialoguesView.as_view(), name='dialogues-list'),
    path('<int:dialogue_id>/', DialoguesView.as_view(), name='dialog-get-update-delete'),
]
