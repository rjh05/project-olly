# Generated by Django 2.2.15 on 2020-11-13 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_team_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('matches', '0023_matchstats_statsplayer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMatchStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rounds_won', models.PositiveSmallIntegerField(default=0)),
                ('rounds_lost', models.PositiveSmallIntegerField(default=0)),
                ('total_kills', models.PositiveSmallIntegerField(default=0)),
                ('total_deaths', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MatchCheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='match_checkin', to='matches.Match')),
                ('players', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('reporter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checkin_user', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='checking_in_team', to='teams.Team')),
            ],
        ),
    ]
