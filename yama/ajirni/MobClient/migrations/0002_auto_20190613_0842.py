# Generated by Django 2.2.2 on 2019-06-13 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MobClient', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='likes',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='images',
            name='item_id',
        ),
        migrations.AddField(
            model_name='images',
            name='item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='MobClient.Items'),
        ),
        migrations.AlterField(
            model_name='items',
            name='floor_no',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='no_bathrooms',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='no_killometers',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='no_rooms',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='price',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='quantity',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='items',
            name='surface_area',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]