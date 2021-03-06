# Generated by Django 3.2.8 on 2022-02-15 23:39

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journey', '0003_auto_20220215_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(help_text='optional', on_delete=django.db.models.deletion.CASCADE, related_name='travelblog_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(help_text='optional'),
        ),
        migrations.AlterField(
            model_name='post',
            name='favorite_place',
            field=models.CharField(help_text='optional', max_length=250),
        ),
    ]
