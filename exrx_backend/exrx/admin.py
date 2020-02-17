# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Exercise, Classification, Instruction

# Register your models here.
admin.site.register(Classification)
admin.site.register(Instruction)
admin.site.register(Exercise)