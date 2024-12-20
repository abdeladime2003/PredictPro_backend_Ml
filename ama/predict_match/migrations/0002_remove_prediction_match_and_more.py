# Generated by Django 5.1.2 on 2024-11-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict_match', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prediction',
            name='match',
        ),
        migrations.RenameField(
            model_name='prediction',
            old_name='away_goals',
            new_name='predicted_away_goals',
        ),
        migrations.RenameField(
            model_name='prediction',
            old_name='home_goals',
            new_name='predicted_home_goals',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='away_win_probability',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='draw_probability',
        ),
        migrations.RemoveField(
            model_name='prediction',
            name='home_win_probability',
        ),
        migrations.AddField(
            model_name='prediction',
            name='away_team',
            field=models.CharField(default='away_team', max_length=100),
        ),
        migrations.AddField(
            model_name='prediction',
            name='home_team',
            field=models.CharField(default='home_team', max_length=100),
        ),
        migrations.AddField(
            model_name='prediction',
            name='result',
            field=models.CharField(default='Draw', max_length=20),
        ),
        migrations.DeleteModel(
            name='Match',
        ),
    ]
