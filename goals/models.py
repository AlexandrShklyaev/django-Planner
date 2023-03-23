from django.db import models
from django.utils import timezone

from core.models import User

NULLABLE = {'null': True, 'blank': True}


class DatesModelMixin(models.Model):
    created = models.DateTimeField(verbose_name="Дата создания")
    updated = models.DateTimeField(verbose_name="Дата последнего обновления")

    class Meta:
        abstract = True  # Помечаем класс как абстрактный – для него не будет таблички в БД

    def save(self, *args, **kwargs):
        if not self.id:  # Когда модель только создается – у нее нет id
            self.created = timezone.now()
        self.updated = timezone.now()  # Каждый раз, когда вызывается save, проставляем свежую дату обновления
        return super().save(*args, **kwargs)


class Status(models.IntegerChoices):
    to_do = 1, "К выполнению"
    in_progress = 2, "В процессе"
    done = 3, "Выполнено"
    archived = 4, "Архив"


class Priority(models.IntegerChoices):
    low = 1, "Низкий"
    medium = 2, "Средний"
    high = 3, "Высокий"
    critical = 4, "Критический"


class GoalCategory(DatesModelMixin):
    title = models.CharField(verbose_name="Название", max_length=255)
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT)
    is_deleted = models.BooleanField(verbose_name="Удалена", default=False)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Goal(DatesModelMixin):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    category = models.ForeignKey(to=GoalCategory, verbose_name='Категория', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.PROTECT)
    status = models.PositiveSmallIntegerField(verbose_name='Статус',
                                              choices=Status.choices, default=Status.to_do)
    priority = models.PositiveSmallIntegerField(verbose_name='Приоритет',
                                                choices=Priority.choices, default=Priority.medium)
    due_date = models.DateTimeField(verbose_name='Дедлайн', **NULLABLE)

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'

    def __str__(self):
        return self.title


class GoalComment(DatesModelMixin):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, verbose_name='Автор', related_name='comments')
    goal = models.ForeignKey(to=Goal, verbose_name='Цель', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
