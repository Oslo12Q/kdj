#encoding: utf-8
from django.shortcuts import render

# Create your views here.
from .models import *
import time
import datetime
import json
from django.shortcuts import render_to_response,render
from django.http import HttpResponse

def get_json_response(request, json_rsp):
    data = 'callback('+str(json.dumps(json_rsp))+')'
    return HttpResponse(data)
##上传user,post获取用户名
def post_user(request):
    if request.method != 'POST':
        return get_json_response(request, dict(suc_id=0, ret_cd=405, ret_ts=long(time.time()), user_code=None, data=None))   
    user_code = request.POST.get('user_code') or ''
    if not user_code:
        return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()), user_code=None, data=None))

    User.objects.create(user_name = user_code,score ='0',create_time = datetime.datetime.now())

    return get_json_response(request, dict(suc_id=1, ret_cd=200, ret_ts=long(time.time()), user_code=user_code, data=None))


def anyse_score(request):
    if request.method != 'POST':
        return get_json_response(request, dict(suc_id=0, ret_cd=405, ret_ts=long(time.time()), user_code=None, score =None,data=None))   
    user_code = request.POST.get('user_code') or ''
    if not user_code:
        return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()), user_code=None, score =None,data=None))   
    score = request.POST.get('score') or ''
    if not score:
        return get_json_response(request, dict(suc_id=0, ret_cd=104, ret_ts=long(time.time()), user_code=user_code,score =None,data=None)) 

    User.objects.filter(user_name=user_code).update(score=score)
    return get_json_response(request, dict(suc_id=1, ret_cd=200, ret_ts=long(time.time()), user_code=user_code,score=score, data=None))


def list_user(request):
    user_list = []
    user = User.objects.order_by("score")
    for _ in user:
        id = _.id
        user_name = _.user_name
        score = _.score
        user_data = {
            "id":id,
            "user_name":user_name,
            "score":score
        }
        user_list.append(user_data)
    
    return get_json_response(request, dict(suc_id=0, ret_cd=200, ret_ts=long(time.time()),data=user_list))
    #return HttpResponse(user_list)