# -*- coding: utf-8 -*-
# !/usr/bin/env python
"""
-------------------------------------------------
   File Name：     
   Description：
-------------------------------------------------
__author__ = 'zhu733756'
"""
from django import forms
class AddForm(forms.Form):
    a=forms.IntegerField()
    b=forms.IntegerField()