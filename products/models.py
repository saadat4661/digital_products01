from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_(
        'parent'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_(
        'avatar'), upload_to='categories/', blank=True)
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)
    created_time = models.DateTimeField(
        verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(
        verbose_name=_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), blank=True)
    avatar = models.ImageField(verbose_name=_(
        'avatar'), upload_to='categories/', blank=True)
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)
    categories = models.ManyToManyField(
        'Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(
        verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(
        verbose_name=_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class File(models.Model):

    AUDIO_TYPE = 1
    VIDEO_TYPE = 2
    PDF_TYPE = 3
    IMAGE_TYPE = 4

    FILE_TYPES = (
        (AUDIO_TYPE, 'audio'),
        (VIDEO_TYPE, 'video'),
        (PDF_TYPE, 'pdf'),
        (IMAGE_TYPE, 'image')
    )
    product = models.ForeignKey('Product', verbose_name=_(
        'product'), on_delete=models.CASCADE, related_name='files')
    title = models.CharField(verbose_name=_('title'), max_length=50)
    file = models.FileField(verbose_name=_(
        'file'), upload_to='files/%Y/%m/%d/')
    file_type = models.PositiveSmallIntegerField(
        verbose_name=_('file type'), choices=FILE_TYPES, default=PDF_TYPE)
    is_enable = models.BooleanField(verbose_name=_('is enable'), default=True)
    created_time = models.DateTimeField(
        verbose_name=_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(
        verbose_name=_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('File')
        verbose_name_plural = _('Files')
