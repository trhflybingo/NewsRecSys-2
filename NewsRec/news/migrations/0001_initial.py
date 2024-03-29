

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='new',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_id', models.CharField(max_length=64, unique=True, verbose_name='ID')),
                ('new_cate', models.CharField(max_length=30, verbose_name='类别')),
                ('new_time', models.DateTimeField(verbose_name='发表时间')),
                ('new_seenum', models.IntegerField(verbose_name='浏览次数')),
                ('new_disnum', models.IntegerField(verbose_name='跟帖次数')),
                ('new_title', models.CharField(max_length=30, verbose_name='标题')),
                ('new_content', models.TextField(verbose_name='新闻内容')),
            ],
            options={
                'db_table': 'new',
            },
        ),
    ]
