#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'genghui'
__date__ = '2018/10/11 17:33'

"""
Python3命令行参数

sys.argv--获取Python命令行参数
getopt--专门用来处理命令行参数的，用于获取命令行选项和参数, 支持短选项和长选项
argparse--
"""

import sys
import getopt


def main(argv):
    inputfile = ""
    outputfile = ""

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test_cmd_line.py -i <inputfile> -o <outputfile>')
        sys.exit()

    for opt, arg in opts:
        if opt == "-h":
            print('test_cmd_line.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    print("输入的文件为: ", inputfile)
    print("输出的文件为: ", outputfile)


if __name__ == '__main__':
    print("参数个数为: %d" % len(sys.argv))
    print("参数列表为: ", sys.argv)
    main(sys.argv[1:])
