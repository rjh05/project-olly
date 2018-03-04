# Generated by Django 2.0 on 2018-03-04 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BannedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='error', max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xp', models.PositiveSmallIntegerField(default=0)),
                ('credits', models.PositiveSmallIntegerField(default=0)),
                ('total_earning', models.PositiveSmallIntegerField(default=0)),
                ('about_me', models.CharField(blank=True, default='Forever a mystery', max_length=500)),
                ('xbl', models.CharField(blank=True, default='No Xbox Live Linked', max_length=19)),
                ('psn', models.CharField(blank=True, default='No PSN Linked', max_length=16)),
                ('twitter_profile', models.CharField(blank=True, default='No Twitter Linked', max_length=17)),
                ('twitch_channel', models.CharField(blank=True, default='No Twitch Linked', max_length=50)),
                ('favorite_game', models.CharField(blank=True, default='N/A', max_length=50)),
                ('favorite_console', models.CharField(blank=True, default='N/A', max_length=50)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user_type', models.CharField(default='user', max_length=10)),
                ('ip', models.CharField(default='0.0.0.0', max_length=16)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
