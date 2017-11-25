# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

import models
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','content')
    list_filter=('title',)
admin.site.register(models.Article,ArticleAdmin)
