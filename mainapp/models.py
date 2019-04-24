import os
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import FileExtensionValidator
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse

# from django_resized import ResizedImageField

# Create your models here.


class Tag(models.Model):

    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Category(models.Model):
    """category model class"""
    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Раздел"
        verbose_name_plural = "Разделы"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class ContentMixin(models.Model):
    '''base class for Post, Article and Documents'''
    title = models.CharField(u'Название', max_length=200)
    url_code = models.CharField(u'Код ссылки', max_length=30, blank=True, default='НЕ УКАЗАН')
    short_description = models.CharField(
        u'Краткое описание', max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    published_date = models.DateTimeField(
        u'Дата публикации', blank=True, null=True)
    created_date = models.DateTimeField(u'Дата создания', default=timezone.now)
    text = RichTextUploadingField(verbose_name='Текст')
    author = models.ForeignKey(
        'auth.User', verbose_name='Автор', on_delete=models.CASCADE)
    publish_on_main_page = models.BooleanField(
        verbose_name="Опубликовать на главной", default=False)

    class Meta:
        abstract = True

class SidePanel(models.Model):
    title = models.CharField(u'Название', max_length=200)
    html = RichTextUploadingField(verbose_name='Контент')

    class Meta:
        verbose_name = 'Боковая панель'
        verbose_name_plural = 'Боковые панели'

    def __str__(self):
        return self.title

class Post(ContentMixin):
    '''child of contentmixin'''
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE)
    publish_on_news_page = models.BooleanField(
        verbose_name="Опубликовать в ленте новостей", default=False)
    secondery_main = models.BooleanField(
        verbose_name="Опубликовать как недавние ", default=False)
    side_panel = models.ForeignKey(SidePanel, verbose_name='Боковая панель',
                blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['created_date']
        get_latest_by = ['created_date']
        verbose_name = 'Страница'
        verbose_name_plural = "Страницы"

    def get_absolute_url(self):
        return reverse("detailview",
                       kwargs={"content": "post", "pk": self.pk})

    def publish(self):
        """unused function"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Article(ContentMixin):
    '''child of ContentMixin'''

    class Meta:
        ordering = ['created_date']
        get_latest_by = ['created_date']
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"

    def publish(self):
        """unused, left for future"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(u'Название', max_length=500)
    document = models.FileField(verbose_name='Документ',
                                upload_to="documents/",
                                validators=[FileExtensionValidator(
                                    allowed_extensions=[
                                        'pdf', 'docx', 'doc', 'jpg', 'jpeg'],
                                    message="Неправильный тип файла, используйте\
                                        PDF, DOCX, DOC, JPG, JPEG")])
    url_code = models.CharField(u'Код ссылки', max_length=30, blank=True, default='НЕ УКАЗАН')
    uploaded_at = models.DateTimeField(
        verbose_name='Загружен', default=timezone.now)
    tags = models.ManyToManyField(Tag, verbose_name='Тэги', blank=True)
    created_date = models.DateTimeField(
        default=timezone.now, verbose_name='Дата создания')
    post = models.ForeignKey(Post, verbose_name='Страница',
                             blank=True, default='',
                             on_delete=models.SET_NULL,
                             null=True)
    publish_on_main_page = models.BooleanField(
        verbose_name="Опубиковать на главной", default=False)

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title


def upload_to(instance, filename):
    """left for future, unused function"""
    filename_base, filename_ext = os.path.splitext(filename)
    return "upload/{post_pk}/{filename}{extension}".format(
        post_pk=instance.pk,
        filename=slugify(filename_base),
        extension=filename_ext.lower(),)


def get_image_filename():
    """unused function, left for future"""
    return 'image_{}'.format(slugify(timezone.now()))


class PostPhoto(models.Model):
    """model to load photos to content page"""
    post = models.ForeignKey(Post, verbose_name=u'новость',
                             related_name='images',
                             on_delete=models.SET_NULL,
                             null=True)
    image = models.ImageField(u'изображение', upload_to="upload/")
    title = models.CharField(u'название', max_length=64,
                             blank=True, default=get_image_filename)
    position = models.PositiveIntegerField(u'Позиция', default=0)

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
        ordering = ['position']

    def __str__(self):
        return '{} - {}'.format(self.post, self.image)


class Message(models.Model):
    """this is the class to use within adapter patter realization"""
    STATUS_LIST = (
        (0, 'new'),
        (1, 'registered'),
        (2, 'added_to_sending_queue'),
        (3, 'notify_sent')
    )
    title = models.CharField(u'Заголовок', max_length=64, blank=True)
    typeof = models.CharField(u'Тип сообщения', max_length=64, blank=True)
    params = models.CharField(u'Параметры сообщения',
                              max_length=512, blank=True)
    sender_email = models.EmailField(
        u'Адрес электронной почты', max_length=64, blank=True)
    sender_phone = models.CharField(u'Телефон', max_length=64, blank=True)
    created_date = models.DateTimeField(
        u'Дата получения', default=timezone.now)
    status = models.IntegerField(u'Статус', default=0, choices=STATUS_LIST)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.title

    def set_status(self, status_code):
        # if status_code in STATUS_LIST:
        self.status = status_code


class Contact(models.Model):
    title = models.CharField(u'Название контакта', max_length=64, blank=False)
    description = models.CharField(u'Описание', max_length=200, blank=False)
    email = models.EmailField(
        u'Адрес электронной почты', max_length=64, blank=False)
    phone = models.CharField(u'Телефон', max_length=64, blank=False)
    number = models.SmallIntegerField(u'Порядок вывода на сайт', default=0)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.title


class Staff(models.Model):
    photo = models.ImageField(u'Фотография', blank=True)
    name = models.CharField(u'ФИО', max_length=120, blank=False)
    job = models.CharField(u'Должность', max_length=120, blank=False)
    experience = models.CharField(u'Опыт работы', max_length=500, blank=True)
    priority = models.SmallIntegerField(u'Приоритет', default=0)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return '{} - {}'.format(self.name, self.job)


class Registry(models.Model):
    """this is the class to load external registry records"""
    STATUS_LIST = ((0, 'new'), (1, 'published'))
    title = models.CharField(u'Название', max_length=64, blank=True)
    org = models.CharField(u'Организация', max_length=120, blank=True)
    typeof = models.CharField(u'Тип', max_length=64, blank=True)
    params = models.CharField(u'Параметры',
                              max_length=999, blank=True)
    created_date = models.DateTimeField(
        u'Дата получения', default=timezone.now)
    status = models.IntegerField(u'Статус', default=0, choices=STATUS_LIST)

    class Meta:
        verbose_name = 'Запись реестра'
        verbose_name_plural = 'Записи реестра'

    def __str__(self):
        return self.title
