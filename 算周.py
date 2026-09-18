#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把年月日收成那一天属于哪一年的第几周。

规则：一周从星期一开始，星期天是这一周的最后一天；
某一周属于哪一年，看这一周包不包括那一年的一月四日，
包括才算那一年的第一周。年头年尾可能归到邻年。
"""

import sys
from datetime import date


def 算周(当天):
    """按 ISO 周规则算：周一开头，含一月四日的那周是该年第一周。"""
    归属年, 周, _ = 当天.isocalendar()
    return 归属年, 周


def 主程序(参数):
    if len(参数) != 3:
        sys.stderr.write("没法算周：请给出年、月、日三个整数\n")
        return 2
    try:
        年 = int(参数[0])
        月 = int(参数[1])
        日 = int(参数[2])
    except ValueError:
        sys.stderr.write("没法算周：年、月、日都必须是整数\n")
        return 2
    try:
        当天 = date(年, 月, 日)
    except ValueError:
        sys.stderr.write("没法算周：%s年%s月%s日这一天不存在\n" % (参数[0], 参数[1], 参数[2]))
        return 2
    归属年, 周 = 算周(当天)
    sys.stdout.write("%04d年第%02d周\n" % (归属年, 周))
    return 0


if __name__ == "__main__":
    sys.exit(主程序(sys.argv[1:]))
