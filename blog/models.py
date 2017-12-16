# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


# Create your models here.
class Banner(models.Model):
    # 轮播图
    title = models.CharField(max_length=20, verbose_name=u"标题", default='')
    button = models.CharField(max_length=50, verbose_name=u"按钮", default='')

    img = models.ImageField(upload_to="text_img/%Y/%m", verbose_name=u"文章图片", max_length=100)
    time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Narration(models.Model):
    title = models.CharField(max_length=20, verbose_name=u"标题", default='')
    content = models.TextField(verbose_name=u'内容')

    class Meta:
        verbose_name = u"叙述"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.title


class Work(models.Model):
    describe = models.CharField(max_length=20, verbose_name=u"标题", default='')
    img = models.ImageField(upload_to="work_img/%Y/%m", verbose_name=u"文章图片", max_length=100)
    content = models.TextField(verbose_name=u'内容')

    class Meta:
        verbose_name = u"工作"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.describe


class Process(models.Model):
    describe = models.CharField(max_length=20, verbose_name=u"标题", default='')
    img = models.ImageField(upload_to="process_img/%Y/%m", verbose_name=u"文章图片", max_length=100)
    content = models.TextField(verbose_name=u'内容')

    class Meta:
        verbose_name = u"描述"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.describe


class Make(models.Model):
    describe = models.CharField(max_length=20, verbose_name=u"标题", default='')
    img = models.ImageField(upload_to="make_img/%Y/%m", verbose_name=u"文章图片", max_length=100)
    content = models.TextField(verbose_name=u'内容')

    class Meta:
        verbose_name = u"制作"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.describe


class Comic(models.Model):
    describe = models.CharField(max_length=50, verbose_name=u"标题", default='')
    img = models.ImageField(upload_to="comic_img/%Y/%m", verbose_name=u"文章图片", max_length=100)

    class Meta:
        verbose_name = u"动漫"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.describe
