import paramiko
hostname='10.64,37.100'
port=22
username='dsadm'
passwd='dsadm'
pkey='c:\users\NSNP419\DOCUMENTS\id_rsa'
key=paramiko.RSAKey.from_private_key_file(pkey)
s=paramiko.SSHClient()
s.load_system_host_keys()
s.connect(hostname,port,username,passwd)
stdin,stdout,stderr=s.exec_command('hostname')

print stdout.read()

