# Generated by Django 3.1.5 on 2021-01-13 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assisted_grading', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('offering_dept', models.CharField(max_length=50)),
                ('course_id', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='QpNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_number', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('maxMarks', models.IntegerField()),
                ('children_count', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='Department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='professor',
            old_name='Email',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='Name',
        ),
        migrations.AddField(
            model_name='professor',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='GradeNode',
            fields=[
                ('qpnode_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='assisted_grading.qpnode')),
                ('awarded_marks', models.IntegerField()),
                ('remarks', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('segmentation_image', models.FileField(upload_to='uploads/segmentation_images/')),
                ('processed_image', models.FileField(upload_to='uploads/processed_images/')),
            ],
            bases=('assisted_grading.qpnode',),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.DurationField()),
                ('consolidated_marksheet', models.FileField(upload_to='uploads/testMarksheets/')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assisted_grading.course')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answerscript_pdf', models.FileField(upload_to='uploads/submissions/')),
                ('submission_time', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assisted_grading.test')),
            ],
        ),
        migrations.CreateModel(
            name='QpNodeAdjList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('childNode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='QpdNodeToChild', to='assisted_grading.qpnode')),
                ('parentNode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assisted_grading.qpnode')),
            ],
        ),
        migrations.AddField(
            model_name='qpnode',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assisted_grading.test'),
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assisted_grading.professor'),
        ),
        migrations.CreateModel(
            name='GradeNodeAdjList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('childNode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GradeNodeToChild', to='assisted_grading.gradenode')),
                ('parentNode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assisted_grading.gradenode')),
            ],
        ),
        migrations.AddField(
            model_name='gradenode',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assisted_grading.submission'),
        ),
    ]