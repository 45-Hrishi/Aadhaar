# Generated by Django 3.1.4 on 2021-10-30 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(default='India', max_length=45)),
                ('State', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
                ('pincode', models.CharField(max_length=6)),
                ('Phoneno', models.CharField(max_length=10)),
                ('Telephone', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
