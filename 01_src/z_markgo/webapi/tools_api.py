# -*- coding:utf-8 -*-

from flask import request, send_file, make_response, render_template

from lib import param_tool, com_tool, sql_tool, busi_tool, txt_compare
from webapi import baseRoute, app
from lib.oauth2 import require_oauth

from lib.JsonResult import JsonResult


@baseRoute.route('/tools/report', methods=['POST'])
@require_oauth('profile')
def report():
    args = request.get_json()
    op2, m, s1, op, s2, I_COUNT_PCT, D_COUNT_PCT, S_COUNT_PCT = txt_compare.med_classic_gui(
        args.get("base_text"), args.get("check_text"))
    accuracy = 1 - (m / len(s1.replace(" ", '')))

    return JsonResult.success("处理成功！", {"accuracy": accuracy, "op": op, "op2": op2, "s1": s1, "s2": s2,
                                        "I_COUNT_PCT": I_COUNT_PCT,
                                        "D_COUNT_PCT": D_COUNT_PCT, "S_COUNT_PCT": S_COUNT_PCT})
