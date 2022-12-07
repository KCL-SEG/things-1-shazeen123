from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('things', '0001_initial'),
    ]
    operations = [
        migrations.AlterField(
            model_name='thing',
            name='description',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]