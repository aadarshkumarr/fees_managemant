# Generated by Django 4.0.4 on 2022-05-16 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feesm', '0004_remove_fee_transaction_date_of_ch_dd_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fee',
            old_name='collected_fee',
            new_name='current_amount_deposited',
        ),
        migrations.RenameField(
            model_name='fee',
            old_name='fee_deposited_at_university',
            new_name='total_fee_deposited_at_university',
        ),
    ]