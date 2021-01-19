from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64,
                             verbose_name="Заголовок поста")
    link = models.URLField(verbose_name="Ссылка на новость")
    creation_date = models.DateField(auto_now_add=True,
                                     verbose_name="Дата создания")
    amount_of_upvotes = models.IntegerField(verbose_name="Апвоут")
    author_name = models.CharField(max_length=64,
                                   verbose_name="Имя автора")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-creation_date"]


class Comment(models.Model):
    author_name = models.CharField(max_length=64,
                                   verbose_name="Автор комментария")
    content = models.TextField(max_length=512,
                               verbose_name="Тело комментария")
    creation_date = models.DateField(auto_now_add=True,
                                     verbose_name="Дата создания")
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments",
                             verbose_name="Пост")

    def __str__(self):
        return f"{self.post} | {self.author_name}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-creation_date"]
