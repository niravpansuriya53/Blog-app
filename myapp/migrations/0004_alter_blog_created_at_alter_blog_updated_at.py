# Generated by Django 4.1.5 on 2023-02-28 04:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_blog_pub_date_blog_created_at_blog_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 28, 4, 40, 32, 86480, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 28, 4, 40, 32, 86736, tzinfo=datetime.timezone.utc)),
        ),
    ]