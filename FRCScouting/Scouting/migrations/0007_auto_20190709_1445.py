# Generated by Django 2.2.3 on 2019-07-09 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scouting', '0006_robot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='robot',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='image3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='image4',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='robot',
            name='image5',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]