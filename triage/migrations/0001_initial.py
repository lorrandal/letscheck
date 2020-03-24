# Generated by Django 3.0.4 on 2020-03-24 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('canned_response', models.TextField()),
                ('rating', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='triage.Rating')),
            ],
        ),
        migrations.CreateModel(
            name='MessageToNews',
            fields=[
                ('message', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='chat.Message')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='triage.News')),
            ],
        ),
    ]
