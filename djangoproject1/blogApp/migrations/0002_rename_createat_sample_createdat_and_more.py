# Generated by Django 4.0.4 on 2022-05-27 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sample',
            old_name='createAt',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='publishAt',
            new_name='publishedAt',
        ),
        migrations.RenameField(
            model_name='sample',
            old_name='updateAt',
            new_name='updatedAt',
        ),
        migrations.RemoveField(
            model_name='sample',
            name='id',
        ),
        migrations.AlterField(
            model_name='sample',
            name='slug',
            field=models.SlugField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]