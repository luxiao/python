"""下次再怀疑python很慢的时候就抽自己两耳刮子
两个50万行的csv文件，根据共同的一列来进行合并，首先该列的值在两个csv里是乱序的，
我的第一个写法用了3个小时，轻叹python是有多慢，但是仔细琢磨还是我写的有问题，
于是又准备优化下，结果这一优化直接亮瞎了我的眼，只需要2秒"""
def merge_csv():
    zz_wms = open(u'/Users/tom/Downloads/郑州仓(1).csv')
    wms_info = (line.split(',') for line in zz_wms)
    zz_erp = open('/Users/tom/ch/zz.csv')
    erp_info = [line.split(',') for line in zz_erp]
    with open('/Users/tom/ch/zz_new.csv', 'w+') as out:
        for line in wms_info:
            data = [line[0], line[3], line[5]]
            express_number = line[2]
            for erp_line in erp_info:
                if express_number in erp_line:
                    data.extend(l.strip() for l in erp_line)
                    break
                else:
                    continue
            new_line = ','.join(data+['\n'])
            out.write(new_line)

def merge_csv_v2():
    zz_wms = open(u'/Users/tom/Downloads/郑州仓(1).csv')
    wms_info = (line.split(',') for line in zz_wms)
    zz_erp = open('/Users/tom/ch/zz.csv')
    erp_info = {i[0]:i for i in [line.split(',') for line in zz_erp]}
    with open('/Users/tom/ch/zz_new_v2.csv', 'w+') as out:
        for line in wms_info:
            data = [line[0], line[3], line[5]]
            express_number = line[2]
            if express_number in erp_info:
                data.extend(erp_info[express_number])
            new_line = ','.join(data)
            out.write(new_line)
  
