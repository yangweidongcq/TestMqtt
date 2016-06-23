#! /usr/bin/python
# enconding:utf-8

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from flask import render_template, request, jsonify, send_from_directory
from flask import jsonify, request
from flask.views import View, MethodView
from flask import render_template
from dal.Infrastructure.topic import Topic
import redis
import time
from common.createredis import create_redis
__author__ = 'yangweidong'

class ShowMqttDataView(MethodView):
    def get(self):
        psize = request.args.get('psize', 20, type=int)
        pindex = request.args.get('pindex', 1, type=int)
        rows = Topic.select().order_by(Topic.create_time.desc()).paginate(pindex,psize)
        count = Topic.select().count()
        pagecount = count / psize + (1 if (count % psize) > 0 else 0)
        return render_template('/system/show_mqtt_data.html', rows=rows,psize=psize,pindex=pindex, pagecount=pagecount)


class NewMqttDtaView(MethodView):
    def get(self):
        return render_template("/system/show_new.html")

    def post(self):
        dic = {}
        re = redis.StrictRedis(host="123.56.201.7", port=6379)
        da = re.get("new_date")
        data = da.split(",")
        temperature = data[0]
        hcho_concentrer = data[2][:4]
        rh = data[1]
        pm_two_point_five = data[3]
        pm_one = data[4]
        pm_ten = data[5]
        topic_name = "environment"
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        dic["temperature"] = temperature
        dic["hcho_concentrer"] = hcho_concentrer
        dic["rh"] = rh
        dic["pm_two_point_five"] = pm_two_point_five
        dic["pm_one"] = pm_one
        dic["pm_ten"] = pm_ten
        dic["topic_name"] = topic_name
        dic["create_time"] = create_time
        print dic
        return jsonify({'success': 'ok', 'ret':dic })







