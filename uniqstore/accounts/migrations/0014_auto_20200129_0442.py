# Generated by Django 3.0.2 on 2020-01-29 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200129_0433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='cartitem_ptr',
        ),
        migrations.AddField(
            model_name='checkout',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
