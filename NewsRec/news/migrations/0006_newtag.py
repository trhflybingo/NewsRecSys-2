

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_newhot'),
    ]

    operations = [
        migrations.CreateModel(
            name='newtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_tag', models.CharField(max_length=64, verbose_name='标签')),
                ('new_id', models.CharField(max_length=64, unique=True, verbose_name='ID')),
                ('new_hot', models.FloatField(verbose_name='热度值')),
            ],
            options={
                'db_table': 'newtag',
            },
        ),
    ]
