# Generated by Django 4.1.2 on 2022-10-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Md',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ConatactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('massage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Furnitures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='Lib/fu-imgs')),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Lib/te-imgs')),
                ('name', models.CharField(max_length=120)),
                ('ceo', models.CharField(max_length=120)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ab', models.ManyToManyField(to='app.about_md')),
                ('Co', models.ManyToManyField(to='app.conatactus')),
                ('Fu', models.ManyToManyField(to='app.furnitures')),
                ('Te', models.ManyToManyField(to='app.testimonial')),
            ],
        ),
    ]
