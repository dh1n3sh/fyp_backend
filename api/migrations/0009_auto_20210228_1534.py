# Generated by Django 3.1.5 on 2021-02-28 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='handwriting_model',
            new_name='handwriting_model_zip',
        ),
        migrations.AddField(
            model_name='student',
            name='handwriting_model_path',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
