"""
    数据库服务
"""
from ats_base.base import req, api
from ats_base.common import util
from ats_base.config.configure import CONFIG

KEY = 'db'


def query(table: str, **condition):
    """
    查询
    :param table:
    :param condition:
    :return:
    """
    con = util.to_dict(condition=condition)
    result = req.post('{}/{}'.format(api.get(CONFIG.get(util.SERVICE, KEY)), table), jsons=con)
    if result['code'] == 500:
        raise Exception(result['message'])

    if type(result['data']) is list and len(result['data']) == 1:
        return result['data'].pop()
    else:
        return result['data']


def save(table: str, **data):
    """
    保存
    :param table:
    :param data:
    :return:
    """
    td = util.to_dict(data=data)
    result = req.post('{}/{}'.format(api.get(CONFIG.get(util.SERVICE, KEY)), table), jsons=td)
    if result['code'] == 500:
        raise Exception(result['message'])

    return result['data']


def update(table: str, condition: dict, **data):
    """
    更新
    :param table:
    :param condition:
    :param data:
    :return:
    """
    td = util.to_dict(condition=condition, data=data)
    result = req.put('{}/{}'.format(api.get(CONFIG.get(util.SERVICE, KEY)), table), jsons=td)
    if result['code'] == 500:
        raise Exception(result['message'])

    return result['data']


def delete(table: str, **condition):
    """
    删除
    :param table:
    :param condition:
    :return:
    """
    con = util.to_dict(condition=condition)
    result = req.delete('{}/{}'.format(api.get(CONFIG.get(util.SERVICE, KEY)), table), jsons=con)
    if result['code'] == 500:
        raise Exception(result['message'])

    return result['data']
