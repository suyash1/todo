import pytz
import dateutil.parser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .exceptions import MissingArgumentError


def to_utc_time(timestr=None):
    if timestr:
        parsed_time = dateutil.parser.parse(timestr)
        utc_time = parsed_time.replace(tzinfo=pytz.utc) - parsed_time.utcoffset()
        return utc_time.time()
    raise MissingArgumentError('missing `timestr` argument.')


def do_paginate(data_list, page_number, result_per_page):
    paginator = Paginator(data_list, result_per_page)
    try:
        ret_data_list = paginator.page(page_number)
    except EmptyPage:
        ret_data_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        ret_data_list = paginator.page(1)
    return [ret_data_list, paginator]