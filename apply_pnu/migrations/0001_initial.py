# Generated by Django 2.2.7 on 2020-03-06 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='이름')),
                ('major', models.CharField(max_length=30, verbose_name='학과')),
                ('phone_number', models.CharField(max_length=20, verbose_name='전화번호')),
                ('m_or_f', models.CharField(choices=[('남', '남'), ('여', '여')], max_length=2, verbose_name='성별')),
                ('email', models.EmailField(max_length=254, verbose_name='이메일')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApplyForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduce', models.TextField(max_length=1000, verbose_name='자기소개')),
                ('position', models.TextField(max_length=500, verbose_name='역할상상')),
                ('goal', models.TextField(max_length=500, verbose_name='목표')),
                ('plan', models.TextField(max_length=500, verbose_name='계획')),
                ('team', models.TextField(max_length=500, verbose_name='팀활동')),
                ('concept', models.TextField(max_length=500, verbose_name='컨셉')),
                ('portfolio', models.FileField(blank=True, upload_to='portfolio/', verbose_name='포폴')),
                ('interview', models.TextField(max_length=255, verbose_name='면접')),
                ('experience', models.TextField(max_length=1000, verbose_name='경험')),
                ('schedule', models.TextField(max_length=1000, verbose_name='고정스케줄')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apply_pnu.Profile')),
            ],
        ),
    ]
