import paramiko
import getpass
import sys
import threading
import os


# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('176.19.5.195', username='root', password='123456', port=2222)
# ssh.exec_command('mkdir /tmp/demo')
# result = ssh.exec_command('id root')
# print(result[1].read().decode('utf8'))
# print(result[2].read())
# ssh.close()
################################################################
def rcmd(host, password, cmd, port=22, username='root'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password, port=port)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    data = stdout.read().decode('utf8')
    error = stderr.read().decode('utf8')
    if data:
        print('[%s:OUT]:\n%s' % (host, data))
    if error:
        print('[%s:ERROR]:\n%s' % (host, error))
    ssh.close()


if __name__ == '__main__':
    rcmd(host='176.19.5.195', password='123456', cmd='ls ~', port=2222)
    rcmd('176.19.5.195', '123456', 'id wang5', 2222)
    if len(sys.argv) != 3:
        print('请确认输入信息')
        exit(1)
    pwd = getpass.getpass()
    ipfile = sys.argv[1]
    if not os.path.isfile(ipfile):
        print('文件不存在')
        exit(2)
    with open(ipfile) as f:
        for line in f:
            ip = line.strip()
            t = threading.Thread(target=rcmd, args=(ip, pwd, sys.argv[2]))
            t.start()
