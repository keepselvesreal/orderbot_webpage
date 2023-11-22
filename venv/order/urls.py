from django.urls import path
# FBV 경우
from .views import chat_view
# CBV 경우
from .views import ChatView

urlpatterns = [
    path('chat/', ChatView.as_view())
    # path('chat/', chat_view, name='chat'),
]
