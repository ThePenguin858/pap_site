# Generated by Django 3.0.7 on 2020-06-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='cid',
            field=models.AutoField(default=1, primary_key=True, serialize=False, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]