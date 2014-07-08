# -*- coding: cp936 -*-
"""
import cx_Oracle
task='SERGZ201304004'
workhome='d:/lux/work/'
work_dir=workhome+task+'/'
user='NAIAWII'
passwd='naiawii'
tns_name='cdwii01'
conn=cx_Oracle.connect(user,passwd,tns_name)

def main(work_dir):
  ""
  该脚本是为了自动化job开发，上线需要提交的一系列文件，包括创建job依赖的表的语句，表的依赖关系配置语句，还有执行sql的unix脚本。
  --created by lux
  --email:luxiao1223@gmail.com
  注意：
      需要修改的参数有
      1 task，对应pma里的任务号
      2 维护一个table_list.txt文件，该文件里存放此次job开发使用到的目标表名
      3 维护需要执行sql的tns信息，在生成执行sql的脚本时需要指定运行脚本的tns
  ""
  table_list=open(work_dir+'table_list.txt')
  t=table_list.readlines()
  tables=map(lambda s: s.strip(),t)
  print tables
  #生成job配置信息的插入语句
  #table_cfg(work_dir,tables)
  #生成表的创建语句
  create_table(work_dir,tables)
  #生成执行sql脚本
  #exec_sql(task,work_dir,[0,1,4])
  #生成表的insert脚本
  #dump_table_insert(work_dir,['td_mdb_mapping'])
def dump_table_insert(work_dir,tables):
  ""
  生成表的insert语句
  ""
  cur=getConn()
  for table in tables:
    f=open(work_dir+table+'.sql','w')
    sql='select * from '+table 
    cur.execute(sql)
    for row in cur:
      #f.write('insert into '+table+' values ('+"".join(str(row))+');\n')
      print row[6] 

def exec_sql(task,work_dir,tns):
  ""
  生成执行sql的unix脚本
  ""
  public_dir=workhome+'public/'
  src=public_dir+'task.sh'
  targ=work_dir+task+'.sh'
  with open(src) as infile:
      with open(targ,'w') as outfile:
          for line in infile:
              outfile.write(line)
              if line[0:11]=='echo "start':
                  outfile.write('\n_transfer_name=/home/dsadm/essrdl_transfer/'+task+'/\n')
                  for i in tns:
                      outfile.write('/home/dsadm/script/trans/mysql.sh $_tns_name%d $_user_name%d ${_transfer_name}"createTables.sql\n'%(i,i))
              elif line[0:5]=='mailx':
                  outfile.write('The PRD Transfer '+task+' Done!\n')
def table_cfg(work_dir,tables):
  ""
  生成插入TABLE_CONTROL的sql语句
  ""
  tc='TABLE_CONTROL'#TABLE_CONTROL表
  tdt='T_DATAMASK_TABLELIST'#DATAMASK表
  freq='D'#job运行频率，M代表Monthly，D代表Daily
  system_name='OLAS3'#运行job的服务器
  cfg=open(work_dir+'table_cfg.sql','w')
  for table in tables:
          tc_sql ="insert into %s VALUES('%s',0,0,'Y','Y','%s','S','S',NULL,NULL,4,NULL,NULL,1000,'%s');\n" %(tc,table,freq,system_name)
          tdt_sql="insert into %s VALUES('%s','%s','Y','Y','%s','S',NULL,NULL);\n"%(tdt,system_name,table,freq)
          cfg.write(tc_sql+tdt_sql)
  cfg.close()
def create_table(work_dir,tables):
  ""
  生成表的创建语句，输出到文件
  ""
  cur=conn.cursor()
  f=open(work_dir+'createTables.sql','w')
  for tbl in tables:
          sql=""
          select substr(t.sqlddl,1,decode(instr(t.sqlddl,'CONSTRAINT',1),0,
          length(t.sqlddl),instr(t.sqlddl,'CONSTRAINT',1)) - 6)||CHR(10)|| '  );'  as sqlddl 
          from (select to_char(substr(dbms_metadata.get_ddl('TABLE', upper('%s')),1,instr(dbms_metadata.get_ddl('TABLE',upper('%s')),'SEGMENT',-1) - 2) || ';') as sqlddl from dual) ts""%(tbl)
          cur.execute(sql)
          for row in cur:
                  f.write((("".join(row)).replace('"'+user+'".','')).replace('"','')) 
  f.close()
  conn.close()
def create_view(workpath):
  wt=open(workpath+'\week_tables.sql')
  mt=open(workpath+'\month_tables.sql')
  wv=open(workpath+'\create_vieww.sql','a')
  mv=open(workpath+'\create_viewm.sql','a')
  f=open(workpath+'\create_viewd.sql')
  flag=0 ## o means not find, 1 means find
  tables=[]
  table=''
  for line in mt:
    tables.append(line.strip('\n'))
  print tables
  for line in f:
    if flag==0:
      for table in tables:
        if table in line:
          flag=1
          mv.write(line)
          break
      continue
    if flag==1 and table not in line:
      mv.write(line)
    elif flag==1 and table in line:
      mv.write(line)
      flag=0 ## this means the view is end ""
  wt.close()
  wv.close()
  mt.close()
  mv.close()
  f.close()
  """
def diff_sys(workpath):
  dicfile=open(workpath+'\\tablem_sys.csv')
  dict={}
  for line in dicfile:
    dict[line.split(':')[0]]=line.split(':')[1].strip('\n')
  dicfile.close()
  freq='M'
  for tmp in dict.keys():
    flag=0
    with open(workpath+'\\VIEW_'+dict[tmp]+'_EO'+freq+'.sql','a+') as targ:
      with open(workpath+'\\create_viewm.sql') as mfile:
        for line in mfile:
          if flag==0:
            if tmp in line:#说明该表在mask里，于是按系统名来写入文件
              flag=1
              targ.write(line)
            continue
          if flag==1 and tmp not in line:
            targ.write(line)
          elif flag==1 and tmp in line:
            targ.write(line)
            flag=2
        if flag==0:
          if freq=='D':
            freq=''
          line='CREATE VIEW '+tmp+' AS SELECT * FROM NCAOWII'+freq+'.'+tmp+';\n'
          targ.write(line)
          
if __name__=='__main__':
  diff_sys(r'D:\lux\work\wii\wii优化\sys')
