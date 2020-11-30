# Generated by Django 3.1.3 on 2020-11-30 17:21

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_title_in_red_letters', models.CharField(blank=True, max_length=1000, null=True)),
                ('first_content_title', models.CharField(blank=True, max_length=1000, null=True)),
                ('first_content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_of_first_content', models.ImageField(blank=True, null=True, upload_to='Blogapp/images/')),
                ('second_content_title', models.CharField(blank=True, max_length=1000, null=True)),
                ('second_content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_of_second_content', models.ImageField(blank=True, null=True, upload_to='Blogapp/images/')),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_one', models.ImageField(blank=True, null=True, upload_to='images/gallery/', verbose_name='image')),
                ('image_one_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='image title')),
                ('image_one_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='image description')),
            ],
            options={
                'verbose_name_plural': 'Our Activities Gallery',
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='Blogapp/images')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('child_story', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="child's story")),
            ],
            options={
                'verbose_name_plural': 'Help The Little Children',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RecentEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_event', models.CharField(blank=True, max_length=1000, null=True)),
                ('about_event', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Write about Event')),
                ('image_of_event', models.ImageField(blank=True, null=True, upload_to='Blogapp/images/')),
            ],
            options={
                'verbose_name_plural': 'Recent Events',
            },
        ),
        migrations.CreateModel(
            name='ShortDiscriptionInAboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('first_letter_of_name_in_capital_letter', models.CharField(blank=True, max_length=1, null=True, verbose_name="first letter of 'name' in capital letter")),
                ('flaticon', models.CharField(blank=True, max_length=100, null=True, verbose_name='flaticon class')),
                ('short_description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name_plural': 'A Short Description on Vision, Mission, History, Goal, etc.',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_image', models.ImageField(blank=True, null=True, upload_to='images/gallery/')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('position', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=255, null=True)),
                ('pinterest_url', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'Our Team',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testifier_image', models.ImageField(upload_to='images/Testimony')),
                ('testifier_name', models.CharField(max_length=100)),
                ('remark', models.CharField(default='', max_length=100)),
                ('testimonies', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'Testimonial',
            },
        ),
    ]
