# Generated by Django 3.1.1 on 2021-01-19 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=64, verbose_name="Заголовок поста"),
                ),
                ("link", models.URLField(verbose_name="Ссылка на новость")),
                (
                    "creation_date",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                ("upvotes", models.IntegerField(verbose_name="Апвоут")),
                (
                    "author_name",
                    models.CharField(max_length=64, verbose_name="Имя автора"),
                ),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
                "ordering": ["-creation_date"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "author_name",
                    models.CharField(max_length=64, verbose_name="Автор комментария"),
                ),
                (
                    "content",
                    models.TextField(max_length=512, verbose_name="Тело комментария"),
                ),
                (
                    "creation_date",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="app.post",
                        verbose_name="Пост",
                    ),
                ),
            ],
            options={
                "verbose_name": "Комментарий",
                "verbose_name_plural": "Комментарии",
                "ordering": ["-creation_date"],
            },
        ),
    ]