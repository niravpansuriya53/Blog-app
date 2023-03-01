# Generated by Django 4.1.5 on 2023-03-01 09:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_blog_created_at_alter_blog_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 9, 39, 35, 479723, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 9, 39, 35, 480028, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloog', to='myapp.blog'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 9, 39, 35, 479723, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 9, 39, 35, 480028, tzinfo=datetime.timezone.utc)),
        ),
    ]