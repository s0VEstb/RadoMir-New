from django.shortcuts import render
from . import models
from django.views import generic


class ClothListView(generic.ListView):
    template_name = 'tags/cloth.html'
    context_object_name = 'clothes'
    model = models.Cloth

    def get_queryset(self):
        return models.Cloth.objects.all()


class KinderClothListView(generic.ListView):
    template_name = 'tags/kinder_cloth.html'
    context_object_name = 'clothes_kinder'
    model = models.Cloth

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='For Kids')


class YoungClothListView(generic.ListView):
    template_name = 'tags/young_cloth.html'
    context_object_name = 'clothes_young'
    model = models.Cloth

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='For Young')


class OldClothListView(generic.ListView):
    template_name = 'tags/old_cloth.html'
    context_object_name = 'clothes_old'
    model = models.Cloth

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='For Old')
