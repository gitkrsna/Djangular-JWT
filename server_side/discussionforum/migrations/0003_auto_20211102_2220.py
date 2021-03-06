# Generated by Django 3.2.5 on 2021-11-02 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discussionforum', '0002_alter_student_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='userupvote',
            name='is_upvote',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='discussionforum.post'),
        ),
        migrations.AlterField(
            model_name='userupvote',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userupvote', to='discussionforum.comment'),
        ),
        migrations.AlterField(
            model_name='userupvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='discussionforum.student'),
        ),
    ]
