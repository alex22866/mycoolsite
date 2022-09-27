from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE, verbose_name='Автор', null=True)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=32, verbose_name='Имя', null=True, blank=True)
    login = models.CharField(max_length=255, verbose_name='Логин')

    def __str__(self):
        return self.name


class Comments(models.Model):
    text = models.TextField(max_length=300, verbose_name='Комментарий', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to='User', verbose_name='Пользователь', on_delete=models.CASCADE) #CASCADE если пользв удалит коммы ты они вместе удалятся

    def __str__(self):  #что именно возращает
        return self.text if self.text else str(self.user) #возращает текст если есть текст иначе верни юзера


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.name}{self.last_name}'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')

    def __str__(self):
        return self.title
