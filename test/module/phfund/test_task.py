# -*- coding: utf-8 -*-
import pytest
import json
from run import app

from module.phfund.task import sync_data


def test_sync_data():
    """
    测试音频转写
    """

    with open("test/data/group.json") as file_obj:
        department_list = json.load(file_obj)
    with open("test/data/user.json") as file_obj:
        user_list = json.load(file_obj)
    sync_data(department_list, user_list)
