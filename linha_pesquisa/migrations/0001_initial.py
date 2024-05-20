# Generated by Django 3.2.7 on 2022-05-22 04:35

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Linha_Gossypium_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='uncategorized', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Linha_Setaria_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='uncategorized', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Linha_Setaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='linha_pesquisa.linha_setaria_category')),
            ],
        ),
        migrations.CreateModel(
            name='Linha_Gossypium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', ckeditor_uploader.fields.RichTextUploadingField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='linha_pesquisa.linha_gossypium_category')),
            ],
        ),
    ]