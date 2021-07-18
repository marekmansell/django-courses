# Generated by Django 3.2.5 on 2021-07-18 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('state', models.CharField(choices=[('D', 'Draft'), ('O', 'Open'), ('P', 'Private')], default='D', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(help_text='Explain what will user learn in this lesson.')),
                ('length', models.IntegerField(blank=True, help_text='Number of days that curriculum will be open.', null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('start', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='CurriculumDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, help_text='Describe study material.', null=True)),
                ('data', models.FileField(help_text='Upload study material (document, video, image).', upload_to='')),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='Artefact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, help_text='Describe what you have learned.', null=True)),
                ('data', models.FileField(blank=True, help_text='Upload proof of your work (document, video, image).', null=True, upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.curriculum')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.run')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, help_text='Describe your opinion about the artefact.', null=True)),
                ('artefact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.artefact')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('artefact', 'author')},
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to='')),
                ('run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.run')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('run', 'user')},
            },
        ),
    ]
