# Generated by Django 3.2.9 on 2021-12-04 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_comment_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
