from django.db import models


class Recording(models.Model):

    reader = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date.strftime("%d/%m/%Y, %H:%M")}: ' \
               f'Читатель: {self.reader} || ' \
               f'Книга: {self.title} (автор: {self.author})'
