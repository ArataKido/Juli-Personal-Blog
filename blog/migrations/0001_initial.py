# Generated by Django 4.0 on 2022-09-01 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('description', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('TRAVEL', 'TRAVEL'), ('FASHION', 'FASHION'), ('LIFESTYLE', 'LIFESTYLE'), ('DESIGN', 'DESIGN'), ('MUSIC', 'MUSIC'), ('VIDEO', 'VIDEO'), ('ADVANTRUE', 'ADVANTRUE')], max_length=20)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
