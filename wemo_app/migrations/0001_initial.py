# Generated by Django 2.0 on 2018-01-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo_title', models.CharField(max_length=30)),
                ('memo_text', models.TextField()),
            ],
        ),
    ]
