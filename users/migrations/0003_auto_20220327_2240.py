# Generated by Django 3.1.7 on 2022-03-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True),
        ),
    ]
