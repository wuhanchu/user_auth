# -*- coding:utf-8 -*-

from flask import request
import re

from lib import txt_compare
from webapi import baseRoute
from lib.oauth2 import require_oauth

from lib.JsonResult import JsonResult


@baseRoute.route('/tools/report', methods=['POST'])
@require_oauth('profile')
def report():
    args = request.get_json()

    base_text = args.get("base_text")
    check_text = args.get("check_text")

    base_text = re.sub('[,.，。 \n?!？！]', '', base_text)
    base_text = txt_compare.num_to_char(base_text)

    check_text = re.sub('[,.，。 \n?!？！]', '', check_text)
    check_text = txt_compare.num_to_char(check_text)

    op2, m, s1, op, s2, I_COUNT_PCT, D_COUNT_PCT, S_COUNT_PCT = txt_compare.med_classic_gui(
        base_text, check_text)
    accuracy = 1 - (m / len(s1.replace(" ", '')))

    return JsonResult.success("处理成功！", {"accuracy": accuracy, "op": op, "op2": op2, "s1": s1, "s2": s2,
                                        "I_COUNT_PCT": I_COUNT_PCT,
                                        "D_COUNT_PCT": D_COUNT_PCT, "S_COUNT_PCT": S_COUNT_PCT})
