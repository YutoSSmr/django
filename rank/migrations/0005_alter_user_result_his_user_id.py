# Generated by Django 4.0.3 on 2023-02-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0004_user_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_result_his',
            name='user_id',
            field=models.CharField(max_length=5),
        ),
    ]
