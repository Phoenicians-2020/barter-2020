# Generated by Django 3.0.8 on 2020-07-23 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interests',
            options={'verbose_name': 'Interest', 'verbose_name_plural': 'Interests'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AddField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
