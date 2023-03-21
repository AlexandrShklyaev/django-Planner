# Generated by Django 4.0.1 on 2023-03-16 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалена')),
                ('created', models.DateTimeField(verbose_name='Дата создания')),
                ('updated', models.DateTimeField(verbose_name='Дата последнего обновления')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'К выполнению'), (2, 'В процессе'), (3, 'Выполнено'), (4, 'Архив')], default=1, verbose_name='Статус')),
                ('priority', models.PositiveSmallIntegerField(choices=[(1, 'Низкий'), (2, 'Средний'), (3, 'Высокий'), (4, 'Критический')], default=2, verbose_name='Приоритет')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goals.goalcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Цель',
                'verbose_name_plural': 'Цели',
            },
        ),
    ]
