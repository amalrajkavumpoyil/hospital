# Generated by Django 4.1.4 on 2022-12-13 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='dep_name',
        ),
        migrations.AddField(
            model_name='booking',
            name='doc_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Home.doctors'),
            preserve_default=False,
        ),
    ]
