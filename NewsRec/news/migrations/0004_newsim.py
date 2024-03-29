

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20181209_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_id_base', models.CharField(max_length=64, verbose_name='ID_base')),
                ('new_id_sim', models.CharField(max_length=64, verbose_name='ID_sim')),
                ('new_correlation', models.FloatField(verbose_name='新闻相关度')),
            ],
            options={
                'db_table': 'newsim',
            },
        ),
    ]
