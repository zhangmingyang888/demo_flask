# coding=utf-8
import os
from datetime import datetime as dt

if not os.path.exists('../o2o_log'):
    os.makedirs('../o2o_log')

# 并行工作进程数
workers = 5
# 监听内网端口5000
bind = '0.0.0.0:8080'
# 设置守护进程
daemon = 'true'
# 设置日志记录水平
loglevel = 'error'
# 设置进程文件目录
pidfile = '../o2o_log/app_run.pid'
# 设置访问日志和错误信息日志路径
accesslog = '../o2o_log/app_access_{0}.log'.format(dt.now().strftime('%Y-%m-%d'))
errorlog = '../o2o_log/app_error_{0}.log'.format(dt.now().strftime('%Y-%m-%d'))
# 超时时间
timeout = 120
