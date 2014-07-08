import paramiko
import os
hostname='10.64.37.100'
port=22
username='dsadm'
remote_file='/home/dsadm/tom-X/id_rsa.pub'
dest_file='d:/lux/pyscripts/id_rsa.pub'
remote_dir='/home/dsadm/tom-X/'
local_dir='d:/lux/pyscripts/'

if __name__=='__main__':
    t=paramiko.Transport((hostname,port))
    t.connect(username=username,password=username)
    sftp=paramiko.SFTPClient.from_transport(t)
    sftp.put(local_dir+'ssh2.py',remote_dir+'ssh2.py')
    #sftp.get(dir_pathsrc_path)
    t.close()
