# -*- coding: cp936 -*-
dict={}
with open('Mandarin.dat') as inp:
  for line in inp.readlines():
    k,v=line.split('\t')
    dict[k]=v
for char in u'你好吗':
  print '%x' % ord(char)
