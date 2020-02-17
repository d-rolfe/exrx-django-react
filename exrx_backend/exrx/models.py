# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Classification(models.Model):
    utility = models.CharField(max_length=50)
    mechanics = models.CharField(max_length=50)
    force = models.CharField(max_length=50)

class Instruction(models.Model):
    preparation = models.TextField()
    execution = models.TextField()

# todo: class for Synergist, Stabilizers, etc ... how to have list tho?

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    target_muscle = models.CharField(max_length=50)
    apparatus = models.CharField(max_length=50)
    instructions = models.ForeignKey(Instruction, on_delete=models.CASCADE)

