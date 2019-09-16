from django.http import Http404
from django.http import HttpResponse
from django.core.exceptions import FieldError, FieldDoesNotExist
from utils.exceptions import *


def get_object(model=None, pk=None, **kwargs):
    if not model:
        return HttpResponse('Bad request', status=400)
    if not pk:
        return HttpResponse('Bad request', status=400)

    try:
        return model.objects.get(pk=pk, **kwargs)
    except model.DoesNotExist:
        raise model.DoesNotExist


def get_object_by(model=None, key=None, val=None):
    if not model or not key or not val:
        return HttpResponse('Bad request', status=400)
    try:
        return model.objects.filter(**{key: val})
    except model.DoesNotExist:
        raise model.DoesNotExist
    except FieldError:
        raise model.DoesNotExist("Field `%s` not found" % field)


def get_all_objects(model=None):
    if not model:
        return HttpResponse('Bad request', status=400)
    try:
        return model.objects.all()
    except model.DoesNotExist:
        raise model.DoesNotExist


def filter_object(model=None, key=None, value=None):
    if not model:
        return HttpResponse('Bad request', status=400)
    if not key or not value:
        return HttpResponse('Bad request', status=400)

    try:
        return model.objects.filter(**{key: value})
    except model.DoesNotExist:
        raise Http404