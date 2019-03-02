# Generated by Django 2.1.7 on 2019-03-02 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('results', '0005_auto_20190302_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compoundb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('outputval', models.TextField(blank=True, default='rsult not calculated', null=True)),
                ('pdf', models.FileField(upload_to='files/')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]