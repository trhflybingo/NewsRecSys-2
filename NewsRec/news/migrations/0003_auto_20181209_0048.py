

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20181208_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='new_title',
            field=models.CharField(max_length=100, verbose_name='标题'),
        ),
    ]
