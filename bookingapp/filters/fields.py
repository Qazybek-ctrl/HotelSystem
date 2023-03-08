from django import forms

from django_filters import rest_framework as filters

class IntegerInFilter(filters.BaseInFilter):
    field_class = forms.IntegerField
    
