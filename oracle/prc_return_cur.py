import cx_Oracle,csv
def exec_prc(s=''):
  conn=cx_Oracle.connect('naiawii/naiawii@cdwii01')
  cur=conn.cursor()
  f=open('result.csv','w+')
  l_cur = cur.var(cx_Oracle.CURSOR)
  l_query=cur.callproc('prc_finance_ytd',('','',l_cur))
  results=l_query[2]
  csv.register_dialect('custom',delimiter=',',skipinitialspace=True)
  writer=csv.writer(f,dialect='custom')
  for field in results.description:
    s=s+field[0]+','
  f.write(s[0:-1]+'\n')
  writer.writerows(results)
  f.close()
  conn.close()
exec_prc()
