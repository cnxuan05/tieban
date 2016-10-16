#coding:utf-8


from calc_8 import *
######
dict_path = 'dict.txt'
dict_all = {}
fp = open(dict_path)
cur_line = 1000
for line in fp:
    cur_line = cur_line + 1
    dict_all[cur_line] = line
fp.close()
####

