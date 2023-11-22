from django.shortcuts import render

# 클래스형 뷰 사용 시 사용
from django.views.generic import TemplateView

def chat_view(request):
    return render(request, 'order/chat_template.html')

class ChatView(TemplateView):
    template_name = "order/chat_template.html"
