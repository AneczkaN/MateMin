# Generated by Django 4.1 on 2024-06-25 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_commentarticle_articlecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsArticle', to='core.article'),
        ),
    ]
