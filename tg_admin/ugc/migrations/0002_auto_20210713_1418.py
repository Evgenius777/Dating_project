# Generated by Django 3.2.5 on 2021-07-13 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль Пользователя', 'verbose_name_plural': 'Профили Пользователя'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='external_id',
            field=models.PositiveIntegerField(verbose_name='ID Пользователя'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время получения')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ugc.profile', verbose_name='Профиль Пользователя')),
            ],
            options={
                'verbose_name': 'Сообщение Пользователя',
                'verbose_name_plural': 'Сообщения Пользователя',
            },
        ),
    ]
