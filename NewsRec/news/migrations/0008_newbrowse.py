

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20181212_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='newbrowse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64, verbose_name='用户名')),
                ('new_id', models.CharField(max_length=64, verbose_name='ID')),
                ('new_browse_time', models.DateTimeField(verbose_name='浏览时间')),
            ],
            options={
                'db_table': 'newbrowse',
            },
        ),
    ]
