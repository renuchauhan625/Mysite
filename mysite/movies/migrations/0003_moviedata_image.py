# Generated by Django 3.0 on 2020-06-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='images/None/noimg.jpg', upload_to='images/'),
        ),
    ]