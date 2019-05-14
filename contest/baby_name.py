# coding: utf-8
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def mode_wanzhou():
    '''渔舟唱晚-->晚舟'''
    nagtive_list = u'死丧狗犬猪妖难乱苦愁仇毖灭妇虐凶崩戾恶畜鬼哭狼怨睡烂灾滥废'
    names = set()
    p = re.compile(ur'.+?([\u4e00-\u9fa5]{4})+.+?')
    # with open('/Users/lux/Downloads/shijing.txt') as f:
    with open('/Users/lux/Downloads/test.txt') as f:
        for line in f.readlines():
            m = p.search(line.decode('utf-8'))
            if m:
                for g in m.groups():
                    print m.groups(), line
                    if g[3] not in nagtive_list and g[1] not in nagtive_list:
                        names.add(u'卢'+g[3]+g[1])
    print ',\t'.join(names)

# a = list(u'卢思可', u'卢思牧', u'卢子振')
def main():
    mode_wanzhou()

if __name__ == '__main__':
    main()
