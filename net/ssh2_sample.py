import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
hostname='10.64.37.100'
user='dsadm'
passwd='dsadm'
ssh.connect(hostname,username=user,password=passwd)
cmd='hostname'
stdin,stdout,stderr=ssh.exec_command(cmd)
print stdout.read()
