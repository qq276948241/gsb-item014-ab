#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把年月日收成那一天属于哪一年的第几周。年头年尾按错的规则算。"""

import sys
from datetime import date


def 错算(当天):
    """把星期日当成一周的头，并且不许跨到邻年，超过五十二周就压回去。"""
    首日 = date(当天.year, 1, 1)
    偏移 = (首日.weekday() + 1) % 7
    年内第几天 = (当天 - 首日).days
    周 = (年内第几天 + 偏移) // 7 + 1
    if 周 > 52:
        周 = 52
    if 周 < 1:
        周 = 1
    return 当天.year, 周


def 主程序(参数):
    if len(参数) != 3:
        sys.stderr.write("没法算周：请给出年、月、日三个整数\n")
        return 2
    try:
        年 = int(参数[0])
        月 = int(参数[1])
        日 = int(参数[2])
        当天 = date(年, 月, 日)
    except Exception as 错:
        sys.stderr.write(str(错) + "\n")
        return 2
    归属年, 周 = 错算(当天)
    sys.stdout.write("%d年第%02d周\n" % (归属年, 周))
    return 0


if __name__ == "__main__":
    sys.exit(主程序(sys.argv[1:]))
