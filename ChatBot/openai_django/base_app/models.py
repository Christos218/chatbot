from django.db import models

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=100, null=True)
    conversation = models.TextField()
    user_timestamp = models.DateTimeField(auto_now_add=True)
    bot_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat ({self.role})"
