# Generated by Django 5.1.1 on 2024-09-14 11:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mailing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='mailing_clients',
            field=models.ManyToManyField(to='mailing.client', verbose_name='clients'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='mailing_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='mailing_user'),
        ),
        migrations.AddField(
            model_name='attempt',
            name='mailing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing', verbose_name='mailing'),
        ),
        migrations.AddField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='message_user'),
        ),
        migrations.AddField(
            model_name='mailing',
            name='mailing_message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mailing.message', verbose_name='message'),
        ),
    ]
