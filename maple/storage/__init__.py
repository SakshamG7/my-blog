#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2019 jianglin
# File Name: __init__.py
# Author: jianglin
# Email: mail@honmaple.com
# Created: 2019-05-13 16:36:40 (CST)
# Last Update: Friday 2019-06-07 13:17:57 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import Blueprint

from . import config
from .router import (BucketListView, BucketView, FileListView, FileShowView,
                     FileView)

site = Blueprint('storage', __name__)

site.add_url_rule(
    '/api/bucket',
    view_func=BucketListView.as_view('buckets'),
)
site.add_url_rule(
    '/api/bucket/<int:pk>',
    view_func=BucketView.as_view('bucket'),
)
site.add_url_rule(
    '/api/file/<bucket>',
    view_func=FileListView.as_view('files'),
)
site.add_url_rule(
    '/api/file/<bucket>/<int:pk>',
    view_func=FileView.as_view('file'),
)
site.add_url_rule(
    "/storage/<path:filename>",
    view_func=FileShowView.as_view("show"),
)


def init_conf(app):
    variables = [item for item in dir(config) if not item.startswith("__")]
    for k, v in app.config.get("STORAGE", dict()).items():
        if k not in variables:
            continue
        setattr(config, k, v)


def init_app(app):
    init_conf(app)
    app.register_blueprint(site, subdomain=config.SUBDOMAIN)
