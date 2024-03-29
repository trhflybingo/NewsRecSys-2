

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_newsim'),
    ]

    operations = [
        migrations.CreateModel(
            name='newhot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_id', models.CharField(max_length=64, unique=True, verbose_name='ID')),
                ('new_hot', models.FloatField(verbose_name='热度值')),
                ('new_cate', models.ForeignKey(on_delete=False, related_name='类别名', to='news.cate')),
            ],
            options={
                'db_table': 'newhot',
            },
        ),
    ]
