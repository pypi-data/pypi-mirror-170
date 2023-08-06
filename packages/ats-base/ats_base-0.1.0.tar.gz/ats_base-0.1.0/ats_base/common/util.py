import os
import re
import time
import uuid

from pathlib import Path

from dateutil import parser
from dateutil.relativedelta import relativedelta

SERVICE = 'SERVICE'


def to_dict(**kwargs):
    """
    转化为dict类型数据
    :param kwargs:
    :return:
    """
    return kwargs


def to_list(*args):
    """
    转化为list类型数据
    :param args:
    :return:
    """
    return args


def extract_digit(s: str):
    """
    提取字符串中所有数字
    :param s:
    :return:
    """
    return "".join(list(filter(str.isdigit, s)))


def time_add(dt: str, years: int = 0, months: int = 0, days: int = 0,
             hours: int = 0, minutes: int = 0, seconds: int = 0):
    """
    时间加法器
    :param dt:
    :param years:
    :param months:
    :param days:
    :param hours:
    :param minutes:
    :param seconds:
    :return:
    """
    t = parser.parse(dt)
    t = t + relativedelta(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds)

    return t.strftime('%Y-%m-%d %H:%M:%S')


def time_diff(dt1: str, dt2: str):
    """
    时间差
    :param dt1:
    :param dt2:
    :return: 秒
    """
    t1 = parser.parse(dt1)
    t2 = parser.parse(dt2)

    return (t2 - t1).total_seconds()


def is_valid_url(url: str):
    """
    验证url有效性
    :param url:
    :return:
    """
    regex = r'http[s]?://(?:[a-zA-Z][0-9]|[$-@.&+]|[!*\(\),]|(?:%[0-9a-zA-F]))+'

    p = re.compile(regex)

    if url is None:
        return False

    if re.search(p, url):
        return True

    return False


def replace(content: dict, **kwargs):
    """
    替换字典中变量
    :param content:
    :return:
    """
    ds = str(content)

    for key, value in kwargs.items():
        if type(value) is str:
            ds = ds.replace('#{}'.format(key.upper()), value.replace('\'', '"'))
            ds = ds.replace('*{}'.format(key.upper()), value.replace('\'', '"'))
        else:
            ds = ds.replace('\'#{}\''.format(key.upper()), str(value))
            ds = ds.replace('\'*{}\''.format(key.upper()), str(value))

    return eval(ds)


resp = {'code': 200, 'msg': '', 'data': None}


def success(msg: str = None, data: dict = None):
    """
    接口 - 成功返回的消息
    :param msg:
    :param data:
    :return:
    """
    resp['code'] = 200
    resp['msg'] = msg
    resp['data'] = data
    return resp


def error(msg: str):
    """
    接口 - 失败返回的消息
    :param msg:
    :return:
    """
    resp['code'] = 500
    resp['msg'] = msg
    resp['data'] = None
    return resp


def gen_sn():
    """
    生成唯一的测试序列号
    :return:
    """
    return uuid.uuid4().hex


def sys_current_time():
    """
    服务器系统时间
    :return:
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# class PathUtil(object):
#     """
#     路径处理工具类
#     """
#
#     def __init__(self):
#         # 判断调试模式
#         debug_vars = dict((a, b) for a, b in os.environ.items() if a.find('IPYTHONENABLE') >= 0)
#         # 根据不同场景获取根目录
#         if len(debug_vars) > 0:
#             """当前为debug运行时"""
#             self.root_path = sys.path[2]
#         elif getattr(sys, 'frozen', False):
#             """当前为exe运行时"""
#             self.root_path = os.getcwd()
#         else:
#             """正常执行"""
#             self.root_path = sys.path[1]
#         # 替换斜杠
#         self.root_path = self.root_path.replace("\\", "/")
#
#     def getPathFromResources(self, file_name):
#         """
#         按照文件名拼接资源文件路径
#         :param file_name:
#         :return:
#         """
#         file_path = "%s/resources/%s" % (self.root_path, file_name)
#         return file_path

def exist(*args):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(root_dir, *args)
    if os.path.exists(file_path):
        return True
    else:
        return False


def makeDir(*args):
    root_dir = os.path.dirname(os.path.dirname(__file__))
    dir_path = os.path.join(root_dir, *args)
    if not os.path.exists(dir_path):
        Path(dir_path).mkdir(parents=True, exist_ok=True)

    return dir_path

# pathUtil = PathUtil()
