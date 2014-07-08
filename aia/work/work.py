# -*- coding: cp936 -*-
import win32com,sys,os,os.path,codecs,types,shutil,datetime,subprocess
from easyword import WordWrap
import win32clipboard as clip

tpl=r'D:\lux\work\template'
td=datetime.date.today().isoformat().replace('-','')

def sendEmail(att_list,type='WII',receiver='citpmsqc@nomail.aia.biz'):
  olMailItem = 0x0
  obj = win32com.client.Dispatch("Outlook.Application")
  newMail = obj.CreateItem(olMailItem)
  newMail.Subject = 'RTC '+type+' project transfer'
  newMail.Body = 'Dear all,\n\tThe attached form need to be transferred to share folder. Thanks.\n\nBest Regards,\nTom Lu'
  newMail.To = receiver
  #newMail.CC = "moreaddresses here"
  #newMail.BCC = "address"
  for attachment in att_list:
    newMail.Attachments.Add(attachment)
  #newMail.Attachments.Add(attachment2)
  #newMail.display()
  newMail.Send()

def main(task,task_type):
  #1 根据task所属系统应用特定模板
  conf={'task':task}
  if task_type=='boe':
    conf.update({'report':'IGM127'
          ,'report_path':'IGMReport/IGMDaily/POS'
          ,'bv_path':'IGMReport/BV_IGM127'
          ,'publish':'IGMDaily_POSAGT02'
          ,'publish_path':'IGMReport/IGMDaily'
          ,'action':'UPD'})
  type_dir=os.sep.join((tpl,task_type))
  cfg_file=os.sep.join((type_dir,task_type+'.cfg'))
  tpl_dir=os.sep.join((type_dir,'tpl',''))   
  
  with open(cfg_file) as cfg:
    for line in cfg.readlines():
      l=line.split('=')
      if len(l)>1:
        conf[l[0]]=l[1].strip()
  #获取模板文件列表
  tpl_files =[os.path.join(tpl_dir,f) for f in os.listdir(tpl_dir) if os.path.isfile(os.path.join(tpl_dir,f))]
  task_dir=os.path.join(conf['workdir'],task)
  if not os.path.exists(task_dir):
    os.makedirs(task_dir)
  conf['task_dir']=task_dir
  #将模板文件拷贝到目标目录，并且替换相应内容
  for f in tpl_files:
    if f.find('.doc')>0:
      word_rep(f,conf,task_type)      
    elif f.find('.txt')>0 or f.find('.sh')>0:
      txt_rep(f,conf)
      if f.find('.txt')>0:
        subprocess.call('notepad.exe "'+task_dir+'\\'+td+'.txt'+'"') 
  #2 copy文件到RTC本地目录，同时启动RTC程序，手动推送到RTC
  task_files=[f for f in os.listdir(task_dir)
             if os.path.isfile(os.path.join(task_dir,f))]
  #过滤掉不需要copy的文件
  rtc_flags=['sql','sh','biar','dsx','pck','xml'] 
  rtc_files=[os.path.join(task_dir,f) for f in task_files
             if rtc_flags.count(f[f.index('.')+1:])]
  rtc_target=os.path.join(conf['RTCloc'],task)
  if not os.path.exists(rtc_target):
    os.makedirs(rtc_target)
  for f in rtc_files:
    shutil.copy2(f,rtc_target)
  #将标签内容放到剪贴板
  clip.OpenClipboard()
  clip.EmptyClipboard()
  clip.SetClipboardText(conf['version_label'])
  clip.CloseClipboard()
  #启动RTC，并且等待RTC的操作结束
  subprocess.call(r'D:\IBM\TeamConcert\eclipse.exe')
  
  #3 发送邮件到QC
  attachments=[os.path.join(task_dir,f) for f in task_files
             if f.find('UAT')>0]
  sendEmail(attachments,task_type.upper())
  
  
def word_rep(src,conf,task_type):
  start=int(conf['uat_form_txt_position'])
  rep_list=[i for i in conf.keys()]
  rep_list.extend(['date','version_label'])
  conf['date']=td
  conf['version_label']=conf['task']+'-'+td+'-01'
  w=WordWrap(start,src)
  if src.find('PROD')>=0:
    target=task+'-'+td+src[src.index('PROD')+4:]
  elif src.find('UAT')>=0:
    #如果是uat则插入QC取rtc文件的配置
    if os.path.exists(conf['task_dir']+'\\'+td+'.txt'):
      w.addInlineObj(conf['task_dir']+'\\'+td+'.txt')
    else:
      print '找不到rtc配置信息'
    target=task+'-'+'UAT'+src[src.index('UAT')+3:]
  #替换doc内的文本
  try:
    for s in rep_list:
      w.textReplace('{'+s+'}',conf[s])
    w.saveAs(conf['task_dir']+'\\'+target)
  except:
    print 'error occured.'
  finally:
    w.quit()

def txt_rep(src,conf,tns='1'):
  rep_list=[i for i in conf.keys() if i=='task' or i.startswith('rtc_') or i.startswith('sh_')]
  if src.find('RTC')>=0:
    #rep_list.append('rtc_type')
    #conf['rtc_type']='\\'+conf['task'][:conf['task'].index('201')]
    target=td+src[src.index('RTC')+3:]
  elif src.find('.sh')>=0:
    rep_list.append('tns')
    conf['tns']=tns
    target=task+src[src.index('.'):]
  with open(os.path.join(conf['task_dir'],target),'w+') as output:
    with open(src) as inputfile:
      for l in inputfile.readlines():
        for s in rep_list:
          l=l.replace('{'+s+'}',conf[s])
        output.write(l)


if __name__=='__main__':
  task='ESSRDLCHO201407037'  
  main(task,'wii')
  #sendEmail([r'D:\lux\work\2014\SERCHO201403029\transfer\2014-04-02\SERCHO201403029-UAT-01.doc'],'WII')
  
  
