# Generated by Django 3.0.8 on 2020-09-05 06:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(blank=True, max_length=500, null=True)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('artist', models.CharField(blank=True, max_length=500, null=True)),
                ('genre', models.CharField(blank=True, max_length=500, null=True)),
                ('reason', models.CharField(blank=True, max_length=500, null=True)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
