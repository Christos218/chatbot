from django.urls import path
from django.contrib import admin
from base_app.views import query_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', query_view, name='query'),
    path('save-chat/', query_view, name='save_chat'),
    path('get-chat/', query_view, name='get_chat'),
    path('clear-chats/', query_view, name='clear_chats'),
]
