# Generated by Django 4.2.6 on 2023-10-16 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='이메일주소')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('username', models.CharField(max_length=50, verbose_name='이름')),
                ('mobile', models.CharField(max_length=20, verbose_name='휴대폰번호')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화여부')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정시간')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]