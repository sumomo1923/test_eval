# Generated by Django 4.1.4 on 2023-03-22 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("eval", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="score",
            old_name="eval_item",
            new_name="eval_items",
        ),
    ]