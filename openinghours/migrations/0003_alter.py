from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openinghours', '0002_alter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='logo', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Slug'),
        ),
    ]
