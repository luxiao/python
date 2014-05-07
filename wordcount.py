"""编写这个python脚本的原因很简单，源于自己写python代码写到
一定程度会觉得没什么好提高的，就只能从外部找刺激了。本题目在
http://www.abling.com/programtestpython.html
下面就是我的解法，同时上面的test还要求写一份关于实现的算法原理，
我表示没有算法啊。。。完全就是一步步写。没有递归，也没有其他。我觉得我的嵌套太深了，学习下google的
"""

import sys

def wordcount(src,targ):
  result={}
  with open(src) as inp:
    with open(targ,'w+') as out:
      for line in inp.readlines():
        word=''
        for c in line:
          lc=c.lower()
          w=ord(lc)
          if w >=95 and w<=122:
            word=word+lc
          else:
            if word:
              if result.has_key(word):
                result[word]+=1
              else:
                result.update({word:1})
              word=''
          continue
      for k in sorted(result.keys()):
        out.write(k+': '+str(result[k])+'\n')
if __name__=='__main__':
  args=sys.argv
  print args
  if len(args)!=3:
    print 'Invalid parameter number'
  else:
    wordcount(args[1],args[2])

#谷歌版 虽然二者的题目不一样，所以处理逻辑上会有一点差异    
#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def sort_by_value(item):
    return item[-1]

def build_dict(filename):
    f = open(filename, 'rU')
    words = f.read().split()
    count = {}

    for word in words:
        word = word.lower()
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

    f.close()

    return count

def print_words(filename):
    dict = build_dict(filename)

    for word in sorted(dict.keys()):
        print word, dict[word]

def print_top(filename):
    count = build_dict(filename)
    i = 0

    items = sorted(count.items(), key=sort_by_value, reverse=True)
    for item in items[:20]:
        print item[0] + ': ' + str(item[1]) + ' times'
        i += 1

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
      print_words(filename)
    elif option == '--topcount':
      print_top(filename)
    else:
      print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
    main()
