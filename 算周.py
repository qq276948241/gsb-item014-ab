#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把年月日收成那一天属于哪一年的第几周。一周从星期一开始，归属看一月四日落在哪一周。"""

import sys
from datetime import date


def 算周(当天):
    """按周一开头、一月四日所在周为第一年第一周的规则算归属年和周数。"""
    归属年, 周, _ = 当天.isocalendar()
    return 归属年, 周


def 收成整数(字):
    串 = 字.strip()
    if not 串:
        raise ValueError
    if 串[0] in "+-":
        串 = 串[1:]
    if not 串.isdigit():
        raise ValueError
    return int(字)


def 主程序(参数):
    if len(参数) != 3:
        sys.stderr.write("没法算周：请给出年、月、日三个整数\n")
        return 2
    try:
        年 = 收成整数(参数[0])
        月 = 收成整数(参数[1])
        日 = 收成整数(参数[2])
    except ValueError:
        sys.stderr.write("没法算周：年、月、日都必须是整数\n")
        return 2
    try:
        当天 = date(年, 月, 日)
    except ValueError:
        sys.stderr.write("没法算周：%s年%s月%s日这个日子不存在\n" % (参数[0], 参数[1], 参数[2]))
        return 2
    归属年, 周 = 算周(当天)
    sys.stdout.write("%04d年第%02d周\n" % (归属年, 周))
    return 0


if __name__ == "__main__":
    sys.exit(主程序(sys.argv[1:]))
