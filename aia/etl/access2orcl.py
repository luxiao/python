# -*- coding: cp936 -*- 
from win32com.client import Dispatch
from adoconstants import *
import cx_Oracle,datetime,os,re,time

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
lib={}
lib["gemail"]= re.compile(r'[\w.-]+@[\w.-]+')    
lib["cphone"] = re.compile(r"1[-\d\s-]{10,}")    
lib["qqnum"] = re.compile(r"[1-9][\d\s]{5,}")

def getRe(instr,retype):
  outstr=''
  match=re.findall(lib[retype],instr)
  if match:
    for tmp in match:
      if retype=='gemail' and outstr=='':
        outstr=tmp
      if retype=='qqnum' and outstr=='':
        tmp=tmp.replace(' ','').replace('-','')
        if len(tmp)>=5 and len(tmp)<11:
          outstr=tmp
      if retype=='cphone' and outstr=='':
        tmp=tmp.replace(' ','').replace('-','')
        if len(tmp)==11:
          outstr=tmp
  return outstr
def callPrc(par):
  para_list=[]
  para_list.append(par)
  conn=cx_Oracle.connect('naiawii/naiawii@cdwii01')
  cur=conn.cursor()
  cur.callproc('prc_netdata',para_list)
  cur.close()
  conn.close()  
def acc2orcl(mdb,collectDate):
  oConn = Dispatch('ADODB.Connection')
  oConn.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source="+mdb+"SpiderResult.mdb;"
  oConn.Open()
  conn=cx_Oracle.connect('naiawii/naiawii@cdwii01')
  cur=conn.cursor()
  table='NETDATANEW'
  td=datetime.date.today()
  if oConn.State == adStateOpen:
    print "Connected to the database: "+mdb[-4:-1]
    oRS = Dispatch('ADODB.RecordSet')
    oRS.ActiveConnection = oConn
    sql="""select ID,Mid(用户ID,1,200),Mid(城市,1,600),Mid(标题,1,600),出处,主题内容
           ,Mid(出行天数,1,25),Mid(出发日期,1,10),Mid(目的地,1,600),Mid(发起人,1,200)
           ,Mid(发起人城市,1,10),Mid(主题发表时间,1,10),Mid(发起人Mail,1,50),Mid(发起人QQ,1,50)
           ,Mid(发起人联系方式,1,100),PageUrl,采集日期 from content where 采集日期>'"""+collectDate+" 16:00:00'"+\
           " and 采集日期<'"+td.isoformat()+" 16:00:00'"
    oRS.Open(sql,oConn)
    param=[]
    while not oRS.EOF:
      content=oRS.Fields(5).Value.encode('utf8')
      email=oRS.Fields(12).Value.encode('utf8')
      qqnum=oRS.Fields(13).Value.encode('utf8')
      phone=oRS.Fields(14).Value.encode('utf8')
      if str(email)=='' or '@' not in str(email):
        email=getRe(content,'gemail')    
      if str(qqnum)=='':
        qqnum=getRe(content,'qqnum')
      if str(phone)=='':
        phone=getRe(content,'cphone')
      if str(email)=='' and str(qqnum)!='':
        email=qqnum+'@qq.com'
      #print 'email: '+email+',qqnum: '+qqnum+',phone: '+phone
      param.append({'id':oRS.Fields(0).Value,'userid':oRS.Fields(1).Value.encode('utf8')\
                    ,'city':oRS.Fields(2).Value.encode('utf8'),'title':oRS.Fields(3).Value.encode('utf8')\
                    ,'souloc':oRS.Fields(4).Value.encode('utf8'),'postcontent':content\
                    ,'days':oRS.Fields(6).Value.encode('utf8'),'departdate':oRS.Fields(7).Value.encode('utf8')\
                    ,'destination':oRS.Fields(8).Value.encode('utf8'),'postman':oRS.Fields(9).Value.encode('utf8')\
                    ,'postcity':oRS.Fields(10).Value.encode('utf8'),'postdate':oRS.Fields(11).Value.encode('utf8')\
                    ,'postemail':email,'qqnum':qqnum,'postcontact':phone,'pageurl':oRS.Fields(15).Value.encode('utf8')\
                    ,'inputdate':oRS.Fields(16).Value.encode('utf8')})
      oRS.MoveNext()
    print len(param)
    cur.setinputsizes(postcontent=cx_Oracle.CLOB)
    cur.executemany('insert into netdatanew (id, userid, city,title, souloc,postcontent, days, departdate,destination, postman\
,  postcity, postdate, postemail, qqnum, postcontact,pageurl,inputdate) values (:id, :userid, :city,:title\
, :souloc,:postcontent,  :days, :departdate,:destination, :postman, :postcity, :postdate, :postemail,  :qqnum, :postcontact\
, :pageurl, :inputdate)',param)
    cur.close()
    conn.commit()
    conn.close()
    oRS.Close()
    oRS=None
  else:
    print "Failed to connect to the database."
def getCollectDate(mdb):
  oConn = Dispatch('ADODB.Connection')
  oConn.ConnectionString = "Provider=Microsoft.Jet.OLEDB.4.0;Data Source="+mdb+"SpiderResult.mdb;"
  oConn.Open()  
  if oConn.State == adStateOpen:
    oRS = Dispatch('ADODB.RecordSet')
    oRS.ActiveConnection = oConn
    getDate='select top 1 采集日期 from content order by 采集日期 desc'
    oRS.Open(getDate,oConn)
    while not oRS.EOF:
      coll=oRS.Fields(0).Value.encode('utf8')
      oRS.MoveNext()
    print "采集日期："+coll   
    oRS.Close()
    oRS=None
    return coll[0:11]
  else:
    return '';
def main(share_folder):
  #log=open(datetime.date.today().isoformat()+'.log','a+')
  acc_loc='Y:\\'
  colDate=getCollectDate(acc_loc+'145\\')
  valid_day=datetime.datetime((int)(colDate[0:4]),(int)(colDate[5:7]),(int)(colDate[8:10]))
  validday_ctime=time.mktime(valid_day.timetuple())
  for i in xrange(181,190):
    #log.write(str(datetime.datetime.now())+'\n'+'Start import mdb file '+str(i)+'\n')
    acc_db=acc_loc+str(i)+'\\'+'SpiderResult.mdb'
    if os.path.isfile(acc_db) :
      file_mtime=os.path.getmtime(acc_db)
      if file_mtime>validday_ctime:
        acc2orcl(acc_loc+str(i)+'\\',colDate)
      #log.write(str(datetime.datetime.now())+'\n'+'end import mdb file '+str(i)+'\n\n')
    else:
      pass#log.write(str(datetime.datetime.now())+'\n'+'not a valid mdb file '+str(i)+'\n\n')
  print 'start call prc at: '+str(datetime.datetime.now())
  para=''
  #para=colDate[0:9]
  callPrc(para)#para格式2013-10-23
  print 'end prc at: '+str(datetime.datetime.now())
  #log.close()
if __name__ == '__main__':
  main("")
