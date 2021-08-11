'''
Author: flwfdd
Date: 2021-08-06 15:03:38
LastEditTime: 2021-08-11 23:26:51
Description: 
_(:з」∠)_
'''
from flask_cors import CORS
from flask import Flask,request,abort,send_file,make_response
import os
import json
import time
import oss2
import pymysql as mdb
import urllib.parse

app = Flask(__name__)
CORS(app)

auth = oss2.Auth('', '')
endpoint = 'http://oss-cn-hangzhou-internal.aliyuncs.com'

# 填写Bucket名称
bucket = oss2.Bucket(auth, endpoint, 'flwfdd')

#认证
def check(key):
    #return
    if key!='' and key!='': 0/0

def read_json(path):
    with open(path,"r",encoding="utf-8") as f:
        return json.loads(f.read())

def save_json(path,dic):
    with open(path,"w",encoding="utf-8") as f:
        f.write(json.dumps(dic,ensure_ascii=False))

#数据库操作，传入操作字符串，返回套着字典的列表
def query_sql(sql):
    con=mdb.connect(host='localhost',
        user='root',
        password='',
        database='memori',
        charset='utf8mb4')
    cur=con.cursor()
    cur.execute(sql)
    con.commit()
    con.close()
    des=cur.description
    l=[]
    for row in cur.fetchall():
        dis={}
        for i in range(len(cur.description)):
            dis[cur.description[i][0]]=row[i]
        l.append(dis)
    return l

@app.route("/")
def say_hello():
    return "hello memori!"
 
#图片上传接口
@app.route('/upload_img/',methods=["POST"])
def upload_img():
    check(request.cookies.get("key"))
    try:
        img=request.files['image']
        name=time.strftime("%Y%m%d_%H%M%S_", time.localtime())+urllib.parse.unquote(img.filename)
        img.save("../www/oss/img/"+name)
        bucket.put_object_from_file('memori/img/'+name, '../www/oss/img/'+name)
        return {"success":1,"file":{"url":"http://oss.flwfdd.xyz/memori/img/"+name}}
    except:
        return {"success":0}


#获取文章
@app.route('/get_doc/',methods=['GET'])
def get_doc():
    check(request.cookies.get("key"))
    args=request.values
    sql="SELECT * from log_doc where id="+args['id']
    dic=query_sql(sql)
    return dic[0]

#创建/更新文章
@app.route('/save_doc/',methods=['POST'])
def save_doc():
    check(request.cookies.get("key"))
    dic=request.get_json()
    if dic['id']!=-1: #更新文章
        sql="UPDATE log_doc set user='{}',title='{}',tag='{}',last_time={},blocks='{}' where id={}".format(\
            dic['user'],mdb.converters.escape_string(dic['title']),dic['tag'],dic['last_time'], \
            mdb.converters.escape_string(json.dumps(dic['blocks'],ensure_ascii=False)),dic['id'])
        query_sql(sql)
        doc_id=dic['id']
    else: #创建文章
        sql="INSERT INTO log_doc(user,title,tag,first_time,last_time,blocks)VALUES( \
            '{}','{}','{}',{},{},'{}')".format(\
            dic['user'],mdb.converters.escape_string(dic['title']),dic['tag'],dic['first_time'],dic['last_time'], \
            mdb.converters.escape_string(json.dumps(dic['blocks'],ensure_ascii=False)))
        query_sql(sql)
        sql="select auto_increment from information_schema.tables where table_schema='memori' and table_name='log_doc';"
        doc_id=query_sql(sql)[0]['auto_increment']-1
    return {"status":"ok","id":doc_id}

#获取文章列表
@app.route('/get_doc_list/',methods=['GET'])
def get_doc_list():
    check(request.cookies.get("key"))
    args=request.values
    sql='select id,user,title,tag,first_time,last_time from log_doc where concat(user,title,tag,blocks) like "%{}%" order by id desc limit {} offset {};'.format(args['search'],args['limit'],args['offset'])
    l=query_sql(sql)
    return {"list":l}

#创建记念
@app.route('/save_date/',methods=['GET'])
def save_date():
    check(request.cookies.get("key"))
    args=request.values
    sql="INSERT INTO log_date(user,name,date)VALUES( \
        '{}','{}','{}')".format(\
        args['user'],mdb.converters.escape_string(args['name']),args['date'])
    query_sql(sql)
    return {"status":"ok"}

#获取记念列表
@app.route('/get_date_list/',methods=['GET'])
def get_date_list():
    check(request.cookies.get("key"))
    args=request.values
    sql='select * from log_date where date>="{}" and date<="{}";'.format(args['start_date'],args['end_date'])
    l=query_sql(sql)
    return {"list":l}

#创建约定
@app.route('/save_flag/',methods=['GET'])
def save_flag():
    check(request.cookies.get("key"))
    args=request.values
    sql="INSERT INTO log_flag(user,name,start_date,due_date,status,value)VALUES( \
        '{}','{}','{}','{}',{},{})".format(\
        args['user'],mdb.converters.escape_string(args['name']),args['start_date'],args['due_date'],args['status'],args['value'])
    query_sql(sql)
    return {"status":"ok"}

#获取约定列表
@app.route('/get_flag_list/',methods=['GET'])
def get_flag_list():
    check(request.cookies.get("key"))
    args=request.values
    sql='select * from log_flag;'
    l=query_sql(sql)
    return {"list":l}

#更新约定
@app.route('/update_flag/',methods=['GET'])
def update_flag():
    check(request.cookies.get("key"))
    args=request.values
    sql='select * from log_flag where id={};'.format(args['id'])
    dic=query_sql(sql)[0]
    if dic['status']!=-1: 0/0
    sql='update log_flag set status={} , end_date="{}" where id={};'.format(args['status'],args['end_date'],args['id'])
    query_sql(sql)
    if int(args['status'])==0:
        sql='update log_wallet set count=count+{} where user != "{}";'.format(dic['value'],dic['user'])
        query_sql(sql)
    return {"status":"ok"}

#获取约定列表
@app.route('/get_wallet/',methods=['GET'])
def get_wallet():
    check(request.cookies.get("key"))
    args=request.values
    sql='select * from log_wallet;'
    l=query_sql(sql)
    return {"list":l}

#登陆
@app.route("/login/",methods=['GET'])
def login():
    args=request.values
    user=args['user']
    password=args['user']+args['password']
    if password=='flw0511' or password=='xy0204':
        res=make_response({"status":"ok"})
        res.set_cookie("user", "flw", max_age=30*24*3600)
        res.set_cookie("key", password, max_age=30*24*3600)
        return res
    else: 0/0

#登陆检查
@app.route("/check_login/",methods=['GET'])
def check_login():
    check(request.cookies.get("key"))
    return {'status':"ok"}

#文件服务器
@app.route("/<path>")
def file_route(path):
    try:
        return send_file("./"+path)
    except:
        abort(404)


app.run(host="0.0.0.0",port=2244)
