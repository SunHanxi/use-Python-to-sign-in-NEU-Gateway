# -*- coding:utf-8 -*-  
import requests  
import getpass  
print "Username:",  
name = raw_input()  
print "Password:"
psd = raw_input()
payload = {'action': 'login', 'ac_id': '1','username': name,'password': psd, 'save_me':'0'}  
r = requests.post('https://ipgw.neu.edu.cn/srun_portal_pc.php?url=&ac_id=1', data=payload)  
res = r.text  
  
if res.find(u'网络已连接'):  
        print 'You are connected.'  
else:  
        print 'Unknown error'
