# Generated by Django 2.1.7 on 2019-04-19 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsanalysis', '0004_weibohot'),
    ]

    operations = [
        migrations.CreateModel(
            name='toutiao',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('abstruct', models.CharField(max_length=200)),
                ('analysis', models.IntegerField()),
            ],
        ),
    ]
