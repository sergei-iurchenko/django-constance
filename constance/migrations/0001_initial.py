from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [('database', '0002_auto_20190129_2304')]
    run_before = [('database', '0003_delete_constance')]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.CreateModel(
                    name='Config',
                    fields=[
                        (
                            'id',
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name='ID',
                            ),
                        ),
                        ('key', models.CharField(max_length=255, unique=True)),
                        (
                            'value',
                            picklefield.fields.PickledObjectField(
                                blank=True, editable=False, null=True
                            ),
                        ),
                    ],
                    options={
                        'default_permissions': ('view', 'change'),
                        'verbose_name': 'constance',
                        'verbose_name_plural': 'constances',
                    },
                ),
            ],
        ),
    ]
