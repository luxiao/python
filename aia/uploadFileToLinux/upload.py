import os,paramiko,datetime,time

share_folder=r'\\aiash-prod\Dashboard\TrueUp\MGTDB'
category={'Actuarial':'ANPVONB_TRUEUP_ACTUARIAL.CSV','Finance':'SPFYP_TRUEUP_FINANCE.CSV','SRF':'TEMPLATE_ADJUST_VONB.CSV'}

target_host='10.64.34.229'
port=22
username='dsadm'
remote_dir='/home/dsadm/MGTDB/'

def fileScan():
  td=datetime.date.today()
  firstday_of_month=datetime.datetime(td.year,td.month,td.day-1)
  firstday_ctime=time.mktime(firstday_of_month.timetuple())#million seconds
  for key in category.keys():
    f=share_folder+os.path.sep+key+os.path.sep+category[key]
    if os.path.isfile(f):
      file_mtime=os.path.getmtime(f)
      if file_mtime>firstday_ctime:
        print "Start upload file "+f
        print fileUpload(key,f)
    else:
      log=open(os.getenv('home')+'\\Desktop\\TrueupFileNotExists.log','a+')
      log.write('\n'+f+' is not exists.'+'\n'+ str(td))

def fileUpload(key,file_path):
  file_name=os.path.split(file_path)[1]
  if key=='Actuarial':
    key=key.upper()
  t=paramiko.Transport((target_host,port))
  t.connect(username=username,password=username)
  sftp=paramiko.SFTPClient.from_transport(t)
  i=sftp.put(file_path,remote_dir+key+'/'+file_name)
  t.close()
  return i

if __name__=='__main__': 
  fileScan() 
