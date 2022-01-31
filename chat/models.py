from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name="author_messages", on_delete=models.CASCADE)
    to = models.ForeignKey(User, related_name="to_whom_messages", on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages(person1, person2):
        messages = Message.objects.order_by('-timestamp').all()
        messages_for_page = list()
        for message in messages:
            if (message.author.username == person1 and message.to.username == person2) \
                or (message.author.username == person2 and message.to.username == person1):
                messages_for_page.append(message)
        return messages_for_page[:10]

    