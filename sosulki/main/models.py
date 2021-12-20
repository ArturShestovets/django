from django.db import models

# Create your models here.
class Feedback(models.Model):

    name = models.CharField('Имя', max_length=20, help_text='Максимум 20 символов')
    email = models.EmailField('Почта')
    message = models.TextField('Сообщение')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'