# Generated by Django 2.2.15 on 2020-12-09 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(default='No description given')),
                ('sender', models.CharField(default='System', max_length=255)),
                ('type', models.CharField(choices=[('match', 1), ('tournament', 2), ('league', 3), ('team', 4), ('support', 5), ('news', 6), ('general', 7), ('store', 8)], default='general', max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('pk1', models.IntegerField(default=0)),
                ('read', models.BooleanField(default=False)),
                ('seen', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xp', models.PositiveSmallIntegerField(default=0)),
                ('credits', models.PositiveSmallIntegerField(default=0)),
                ('passes', models.PositiveSmallIntegerField(default=0)),
                ('total_earning', models.PositiveSmallIntegerField(default=0)),
                ('current_earning', models.PositiveSmallIntegerField(default=0)),
                ('about_me', models.TextField(blank=True, default='Forever a mystery')),
                ('steamid64', models.CharField(blank=True, default='No SteamID64', max_length=255)),
                ('discord', models.CharField(blank=True, default='No Dsicord', max_length=255)),
                ('xbl', models.CharField(blank=True, default='No Xbox Live Linked', max_length=30)),
                ('psn', models.CharField(blank=True, default='No PSN Linked', max_length=30)),
                ('steam', models.CharField(blank=True, default='No Steam Linked', max_length=30)),
                ('epic', models.CharField(blank=True, default='No Epic Linked', max_length=30)),
                ('lol', models.CharField(blank=True, default='No LOL Linked', max_length=30)),
                ('battlenet', models.CharField(blank=True, default='No Battle.net Linked', max_length=30)),
                ('activisionid', models.CharField(blank=True, default='No Activision ID Linked', max_length=30)),
                ('twitter_profile', models.CharField(blank=True, default='No Twitter Linked', max_length=30)),
                ('twitch_channel', models.CharField(blank=True, default='No Twitch Linked', max_length=50)),
                ('favorite_game', models.CharField(blank=True, default='N/A', max_length=50)),
                ('favorite_console', models.CharField(blank=True, default='N/A', max_length=50)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user_type', models.CharField(choices=[('user', 'Standard User'), ('admin', 'Admin'), ('superadmin', 'Super Admin')], default='user', max_length=10)),
                ('ip', models.CharField(default='0.0.0.0', max_length=45)),
                ('num_trophies', models.PositiveSmallIntegerField(default=0)),
                ('xbl_verified', models.BooleanField(blank=True, default=False)),
                ('psn_verified', models.BooleanField(default=False)),
                ('user_verified', models.BooleanField(blank=True, default=False)),
                ('num_bronze', models.PositiveSmallIntegerField(default=0)),
                ('num_silver', models.PositiveSmallIntegerField(default=0)),
                ('num_gold', models.PositiveSmallIntegerField(default=0)),
                ('num_plat', models.PositiveSmallIntegerField(default=0)),
                ('num_diamond', models.PositiveSmallIntegerField(default=0)),
                ('num_titanium', models.PositiveSmallIntegerField(default=0)),
                ('num_wagerwin', models.PositiveIntegerField(default=0)),
                ('num_wagerloss', models.PositiveIntegerField(default=0)),
                ('tournament_wins', models.PositiveSmallIntegerField(default=0)),
                ('dubl_tournament_wins', models.PositiveSmallIntegerField(default=0)),
                ('rank', models.PositiveSmallIntegerField(default=100)),
                ('country', django_countries.fields.CountryField(default='US', max_length=2)),
                ('email_enabled', models.BooleanField(default=True)),
                ('captain_teams', models.ManyToManyField(related_name='profile_captain_teams', to='teams.Team')),
                ('founder_teams', models.ManyToManyField(related_name='profile_founder_teams', to='teams.Team')),
                ('notifications', models.ManyToManyField(blank=True, related_name='user_notifications', to='profiles.Notification')),
                ('player_teams', models.ManyToManyField(related_name='profile_player_teams', to='teams.Team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BannedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='error', max_length=12)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='banned', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
