def bs(target,orderedlist):
"""二分查找，话说我之前一直不能理解while后面
跟个else有什么用，现在好像有点感觉了"""
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
  print bs(17, [3,5,6,7,8,13,16,18,19,25])

