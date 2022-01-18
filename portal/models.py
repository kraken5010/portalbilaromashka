from django.db import models
from datetime import date

from django.urls import reverse


class Department(models.Model):
    name = models.CharField('Департаменти', max_length=100, db_index=True)
    slug = models.SlugField('URL', unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('department', kwargs={'dep_slug': self.slug})

    class Meta:
        verbose_name_plural = 'Департаменти'
        ordering = ['id']


class CommercialArticle(models.Model):
    """"Статьи коммерческого департамента"""
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('URL', max_length=130, unique=True)
    content = models.TextField('Контент')
    time_create = models.DateField('Дата створення', default=date.today)
    draft = models.BooleanField('Чернетка', default=False)
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('comm_article', kwargs={'comm_slug': self.slug})

    class Meta:
        verbose_name = '<<Комерційний>> стаття'
        verbose_name_plural = '<<Комерційний>> статті'


class CommercialStructure(models.Model):
    """"Структура коммерческого департамента"""
    full_name = models.CharField('ПІБ', max_length=150, help_text="Прізвище Ім'я По батькові")
    position = models.CharField('Посада', max_length=100)
    photo = models.ImageField('Фото', upload_to='workers/', blank=True)
    phone = models.CharField('Номер телефону', max_length=12, help_text='Формат: 380xxxxxxxxx')
    email = models.EmailField()
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return f'{self.full_name} - {self.position}'

    class Meta:
        verbose_name = '<<Комерційний>> структура'
        verbose_name_plural = '<<Комерційний>> структура'
        ordering = ['id']


class OperationsArticle(models.Model):
    """"Статьи операционного департамента"""
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('URL', max_length=130, unique=True)
    content = models.TextField('Контент')
    time_create = models.DateField('Дата створення', default=date.today)
    draft = models.BooleanField('Чернетка', default=False)
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('oper_article', kwargs={'oper_slug': self.slug})

    class Meta:
        verbose_name = '<<Операційний>> стаття'
        verbose_name_plural = '<<Операційний>> статті'


class OperationsStructure(models.Model):
    """"Структура операционного департамента"""
    full_name = models.CharField('ПІБ', max_length=150, help_text="Прізвище Ім'я По батькові")
    position = models.CharField('Посада', max_length=100)
    photo = models.ImageField('Фото', upload_to='workers/', blank=True)
    phone = models.CharField('Номер телефону', max_length=12, help_text='Формат: 380xxxxxxxxx')
    email = models.EmailField()
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return f'{self.full_name} - {self.position}'

    class Meta:
        verbose_name = '<<Операційний>> структура'
        verbose_name_plural = '<<Операційний>> структура'
        ordering = ['id']


class FinancialArticle(models.Model):
    """"Статьи финансового департамента"""
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('URL', max_length=130, unique=True)
    content = models.TextField('Контент')
    time_create = models.DateField('Дата створення', default=date.today)
    draft = models.BooleanField('Чернетка', default=False)
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('fin_article', kwargs={'fin_slug': self.slug})

    class Meta:
        verbose_name = '<<Фінансовий>> стаття'
        verbose_name_plural = '<<Фінансовий>> статті'


class FinancialStructure(models.Model):
    """"Структура финансового департамента"""
    full_name = models.CharField('ПІБ', max_length=150, help_text="Прізвище Ім'я По батькові")
    position = models.CharField('Посада', max_length=100)
    photo = models.ImageField('Фото', upload_to='workers/', blank=True)
    phone = models.CharField('Номер телефону', max_length=12, help_text='Формат: 380xxxxxxxxx')
    email = models.EmailField()
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return f'{self.full_name} - {self.position}'

    class Meta:
        verbose_name = '<<Фінансовий>> структура'
        verbose_name_plural = '<<Фінансовий>> структура'
        ordering = ['id']


class AccountingCategoryArticle(models.Model):
    name = models.CharField('Бухгалтерія категорія', max_length=100, db_index=True)
    slug = models.SlugField('URL', unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '<<Бухгалтерія категорії>>'
        ordering = ['id']


class AccountingArticle(models.Model):
    """"Статьи департамента бухгалтерии"""
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('URL', max_length=130, unique=True)
    content = models.TextField('Контент')
    time_create = models.DateField('Дата створення', default=date.today)
    draft = models.BooleanField('Чернетка', default=False)
    cat = models.ForeignKey(AccountingCategoryArticle, on_delete=models.PROTECT, null=True, verbose_name='Бухгалтерія категорія')
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('acc_article', kwargs={'acc_slug': self.slug})

    class Meta:
        verbose_name = '<<Бухгалтерія>> стаття'
        verbose_name_plural = '<<Бухгалтерія>> статті'


class AccountingStructure(models.Model):
    """"Структура департамента бухгалтерии"""
    full_name = models.CharField('ПІБ', max_length=150, help_text="Прізвище Ім'я По батькові")
    position = models.CharField('Посада', max_length=100)
    photo = models.ImageField('Фото', upload_to='workers/', blank=True)
    phone = models.CharField('Номер телефону', max_length=12, help_text='Формат: 380xxxxxxxxx')
    email = models.EmailField()
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return f'{self.full_name} - {self.position}'

    class Meta:
        verbose_name = '<<Бухгалтерія>> структура'
        verbose_name_plural = '<<Бухгалтерія>> структура'
        ordering = ['id']


class DevelopmentArticle(models.Model):
    """"Статьи департамента развития"""
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('URL', max_length=130, unique=True)
    content = models.TextField('Контент')
    time_create = models.DateField('Дата створення', default=date.today)
    draft = models.BooleanField('Чернетка', default=False)
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('dev_article', kwargs={'dev_slug': self.slug})

    class Meta:
        verbose_name = '<<Розвиток>> стаття'
        verbose_name_plural = '<<Розвиток>> статті'


class DevelopmentStructure(models.Model):
    """"Структура департамента развития"""
    full_name = models.CharField('ПІБ', max_length=150, help_text="Прізвище Ім'я По батькові")
    position = models.CharField('Посада', max_length=100)
    photo = models.ImageField('Фото', upload_to='workers/', blank=True)
    phone = models.CharField('Номер телефону', max_length=12, help_text='Формат: 380xxxxxxxxx')
    email = models.EmailField()
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return f'{self.full_name} - {self.position}'

    class Meta:
        verbose_name = '<<Розвиток>> структура'
        verbose_name_plural = '<<Розвиток>> структура'
        ordering = ['id']


class ItCategoryArticle(models.Model):
    name = models.CharField('IT категорія', max_length=100, db_index=True)
    slug = models.SlugField('URL', unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '<<IT категорії>>'
        ordering = ['id']


class ItArticle(models.Model):
    """"Статьи департамента IT"""
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('URL', max_length=130, unique=True)
    content = models.TextField('Контент')
    time_create = models.DateField('Дата створення', default=date.today)
    draft = models.BooleanField('Чернетка', default=False)
    cat = models.ForeignKey(ItCategoryArticle, on_delete=models.PROTECT, null=True, verbose_name='IT категорія')
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('it_article', kwargs={'it_slug': self.slug})

    class Meta:
        verbose_name = '<<IT>> стаття'
        verbose_name_plural = '<<IT>> статті'


class ItStructure(models.Model):
    """"Структура департамента IT"""
    full_name = models.CharField('ПІБ', max_length=150, help_text="Прізвище Ім'я По батькові")
    position = models.CharField('Посада', max_length=100)
    photo = models.ImageField('Фото', upload_to='workers/', blank=True)
    phone = models.CharField('Номер телефону', max_length=12, help_text='Формат: 380xxxxxxxxx')
    email = models.EmailField()
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return f'{self.full_name} - {self.position}'

    class Meta:
        verbose_name = '<<IT>> структура'
        verbose_name_plural = '<<IT>> структура'
        ordering = ['id']


class MarketingArticle(models.Model):
    """"Статьи департамента маркетинг"""
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('URL', max_length=130, unique=True)
    content = models.TextField('Контент')
    time_create = models.DateField('Дата створення', default=date.today)
    draft = models.BooleanField('Чернетка', default=False)
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mark_article', kwargs={'mark_slug': self.slug})

    class Meta:
        verbose_name = '<<Маркетинг>> стаття'
        verbose_name_plural = '<<Маркетинг>> статті'


class MarketingStructure(models.Model):
    """"Структура департамента маркетинг"""
    full_name = models.CharField('ПІБ', max_length=150, help_text="Прізвище Ім'я По батькові")
    position = models.CharField('Посада', max_length=100)
    photo = models.ImageField('Фото', upload_to='workers/', blank=True)
    phone = models.CharField('Номер телефону', max_length=12, help_text='Формат: 380xxxxxxxxx')
    email = models.EmailField()
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return f'{self.full_name} - {self.position}'

    class Meta:
        verbose_name = '<<Маркетинг>> структура '
        verbose_name_plural = '<<Маркетинг>> структура'
        ordering = ['id']


class PersonnelArticle(models.Model):
    """"Статьи департамента Персонал"""
    title = models.CharField('Заголовок', max_length=100)
    slug = models.SlugField('URL', max_length=130, unique=True)
    content = models.TextField('Контент')
    time_create = models.DateField('Дата створення', default=date.today)
    draft = models.BooleanField('Чернетка', default=False)
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pers_article', kwargs={'pers_slug': self.slug})

    class Meta:
        verbose_name = '<<Персонал>> стаття'
        verbose_name_plural = '<<Персонал>> статті'


class PersonnelStructure(models.Model):
    """"Структура департамента Персонал"""
    full_name = models.CharField('ПІБ', max_length=150, help_text="Прізвище Ім'я По батькові")
    position = models.CharField('Посада', max_length=100)
    photo = models.ImageField('Фото', upload_to='workers/', blank=True)
    phone = models.CharField('Номер телефону', max_length=12, help_text='Формат: 380xxxxxxxxx')
    email = models.EmailField()
    dep = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, verbose_name='Департамент')

    def __str__(self):
        return f'{self.full_name} - {self.position}'

    class Meta:
        verbose_name = '<<Персонал>> структура'
        verbose_name_plural = '<<Персонал>> Структура'
        ordering = ['id']


class Leader(models.Model):
    """"Структура коммерческого департамента"""
    full_name = models.CharField('ПІБ', max_length=150, help_text="Прізвище Ім'я По батькові")
    position = models.CharField('Посада', max_length=100)
    photo = models.ImageField('Фото', upload_to='workers/', blank=True)
    phone = models.CharField('Номер телефону', max_length=12, help_text='Формат: 380xxxxxxxxx')
    email = models.EmailField()

    def __str__(self):
        return f'{self.full_name} - {self.position}'

    class Meta:
        verbose_name = 'Керівництво'
        verbose_name_plural = 'Керівництво'
        ordering = ['id']




