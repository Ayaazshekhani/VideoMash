# Generated by Django 2.1.2 on 2018-10-20 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_document_videodwldurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='bonusWordsFile',
            field=models.FileField(default='dummy.txt', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='stigmaWordsFile',
            field=models.FileField(default='dummy.txt', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='subtitleFile',
            field=models.FileField(default='dummy.txt', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='videoFile',
            field=models.FileField(default='dummy.txt', upload_to='documents/'),
        ),
    ]
