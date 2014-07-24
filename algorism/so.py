# -*- coding: cp936 -*-
def bs(target,orderedlist):
  """二分查找"""
  start = 0
  end = len(orderedlist)
  while start < end:
    mid = (start + end)/2
    mid_value = orderedlist[mid]
    if target == mid_value:
      return mid
    elif target < mid_value:
      end = mid - 1
      print 'end from %d'%end
    elif target > mid:
      start = mid + 1
      print 'start from %d'%start
  else:
    return None

if __name__ == '__main__':
  print bs(1, [3,5,6,7,8,13,16,18,19,25])
