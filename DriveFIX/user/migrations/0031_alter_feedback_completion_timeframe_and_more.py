# Generated by Django 5.1.1 on 2024-10-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0030_remove_feedback_comments_remove_feedback_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='completion_timeframe',
            field=models.CharField(blank=True, choices=[('Far Exceeded Timeframe', 'Far Exceeded Timeframe'), ('Exceeded Timeframe', 'Exceeded Timeframe'), ('Met Timeframe', 'Met Timeframe'), ('Under Timeframe', 'Under Timeframe')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='expectations_met',
            field=models.CharField(blank=True, choices=[('Did Not Meet Expectations', 'Did Not Meet Expectations'), ('Below Expectations', 'Below Expectations'), ('Met Expectations', 'Met Expectations'), ('Exceeded Expectations', 'Exceeded Expectations')], max_length=50, null=True),
        ),
    ]
