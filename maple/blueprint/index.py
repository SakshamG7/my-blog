#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ********************************************************************************
# Copyright © 2018 jianglin
# File Name: index.py
# Author: jianglin
# Email: lin.jiang@upai.com
# Created: 2018-02-08 14:45:03 (CST)
# Last Update: 星期四 2018-02-08 15:03:12 (CST)
#          By:
# Description:
# ********************************************************************************
from flask import render_template
from flask.views import MethodView
from maple.extension import cache


class IView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return render_template('index.html')


class IndexView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return render_template('index/index.html')


class AboutView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return render_template('index/about.html')


class FriendView(MethodView):
    @cache.cached(timeout=180)
    def get(self):
        return render_template('index/friends.html')
