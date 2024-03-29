

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cate_id', models.CharField(max_length=64, unique=True, verbose_name='ID')),
                ('cate_name', models.CharField(max_length=64, verbose_name='名字')),
            ],
            options={
                'db_table': 'cate',
            },
        ),
        migrations.AlterField(
            model_name='new',
            name='new_cate',
            field=models.ForeignKey(on_delete=False, related_name='类别', to='news.cate'),
        ),
    ]
