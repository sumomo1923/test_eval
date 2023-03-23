# Generated by Django 4.1.4 on 2023-03-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eval", "0004_alter_audiofile_item_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="score",
            name="rating_ac",
            field=models.IntegerField(default="", verbose_name="정확도"),
        ),
        migrations.AlterField(
            model_name="score",
            name="rating_accent",
            field=models.IntegerField(default="", verbose_name="억양/강세"),
        ),
        migrations.AlterField(
            model_name="score",
            name="rating_fu",
            field=models.IntegerField(default="", verbose_name="유창도"),
        ),
        migrations.AlterField(
            model_name="score",
            name="rating_pause",
            field=models.IntegerField(default="", verbose_name="휴지/머뭇거림"),
        ),
        migrations.AlterField(
            model_name="score",
            name="rating_ph",
            field=models.IntegerField(default="", verbose_name="자음/모음"),
        ),
        migrations.AlterField(
            model_name="score",
            name="rating_rule",
            field=models.IntegerField(default="", verbose_name="발음 규칙"),
        ),
        migrations.AlterField(
            model_name="score",
            name="rating_speed",
            field=models.IntegerField(default="", verbose_name="발화 속도"),
        ),
        migrations.AlterField(
            model_name="score",
            name="rating_un",
            field=models.IntegerField(default="", verbose_name="이해도"),
        ),
    ]