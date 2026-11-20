from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True, default='')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField('Название', max_length=80, unique=True)
    price = models.DecimalField(
        'Доплата, ₽', max_digits=6, decimal_places=2, default=0
    )

    class Meta:
        verbose_name = 'Добавка'
        verbose_name_plural = 'Добавки'
        ordering = ['name']

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField('Название', max_length=150, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='drinks',
        verbose_name='Категория',
    )
    price = models.DecimalField('Цена, ₽', max_digits=8, decimal_places=2)
    volume_ml = models.PositiveIntegerField('Объём, мл')
    description = models.TextField('Описание', blank=True, default='')
    toppings = models.ManyToManyField(
        Topping,
        related_name='drinks',
        verbose_name='Добавки',
        blank=True,
    )
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Напиток'
        verbose_name_plural = 'Напитки'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.volume_ml} мл)'


class Recipe(models.Model):
    drink = models.OneToOneField(
        Drink,
        on_delete=models.CASCADE,
        related_name='recipe',
        verbose_name='Напиток',
    )
    ingredients = models.TextField('Ингредиенты')
    steps = models.TextField('Приготовление')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'Рецепт: {self.drink.name}'