# Generated by Django 2.0.13 on 2020-06-12 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200612_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category', verbose_name='分类'),
        ),
    ]
