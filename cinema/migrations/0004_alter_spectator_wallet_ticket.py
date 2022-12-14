# Generated by Django 4.0.6 on 2022-08-08 13:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_remove_showtime_price_currency_alter_showtime_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spectator',
            name='wallet',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Top up your account'),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)], verbose_name='Showtime')),
                ('time_purchase', models.DateTimeField(auto_now_add=True)),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cinema.showtime', verbose_name='Showtime')),
                ('spectator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Spectator')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'ordering': ['-time_purchase'],
            },
        ),
    ]
