

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_newtag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newtag',
            name='new_id',
            field=models.CharField(max_length=64, verbose_name='ID'),
        ),
    ]
