# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import Banner, Narration, Work, Process, Comic, Make

from django.contrib import admin

# Register your models here.
admin.site.register(Banner)
admin.site.register(Narration)
admin.site.register(Work)
admin.site.register(Process)
admin.site.register(Comic)
admin.site.register(Make)
