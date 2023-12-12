from django.urls import path

from dialogues.views import DialoguesView

urlpatterns = [
    path('', DialoguesView.as_view(), name='dialogue-list'),
    path('<int:dialogue_id>/', DialoguesView.as_view(), name='dialogue-operations'),
]
