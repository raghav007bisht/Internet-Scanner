#!/usr/bin/python
#----------------------------------------------------------------------------------------------
#                Create MySQL Databse before executing the script
# Follow the commands :-
#                1. CREATE USER 'internet'@'localhost' IDENTIFIED BY 'Qwerty@321';
#                2. GRANT SELECT ON * . * TO 'internet'@'localhost';
#                3. CREATE DATABASE internet;
#                4. GRANT ALL PRIVILEGES ON `wave` . * TO 'internet'@'localhost';
#                5. CREATE TABLE network (time datetime, ip varchar(255), data varchar(255));
#----------------------------------------------------------------------------------------------


import MySQLdb
import socket
import sys
import time
import thread
import string
import time
from datetime import datetime
import threading
import socket
import threading
from Queue import Queue, Empty

print('##############################################################')
time.sleep(1)
print('#                  Whole Internet Scanner v1.0               #')
print('#                  Scan IP from 1.1.1.1 to 255.255.255.255   #')
print('#                                                            #')
time.sleep(1)
print('#                                Programmer : Raghav Bisht   #')
time.sleep(1)
print('##############################################################')

# DB Connectors And Strings#################################
db = MySQLdb.connect(host="localhost", user="internet", passwd="Qwerty@321",db="internet")
cursor = db.cursor()
print_lock = threading.Lock()
start_time = datetime.now()
print str(start_time)
def http_banner_grabber(ip, port=80, method="GET",timeout=2, http_type="HTTP/1.1"):
    assert method in ['GET', 'HEAD']
    assert http_type in ['HTTP/0.9', "HTTP/1.0", 'HTTP/1.1']
    cr_lf = '\r\n'
    lf_lf = '\n\n'
    crlf_crlf = cr_lf + cr_lf
    res_sep = ''
    rec_chunk = 4096
    try:
    	s = socket.socket()
   	s.settimeout(timeout)
   	s.connect((ip, port))
    except:
	return
	#q.task_done()
	#sys.exit(0)
    req_data = "{} / {}{}".format(method, http_type, cr_lf)
    if http_type == "HTTP/1.1":
        req_data += 'Host: {}:{}{}'.format(ip, port, cr_lf)
        req_data += "Connection: close{}".format(cr_lf)
    	req_data += cr_lf
	s.sendall(req_data.encode())
	res_data = b''
    while 1:
        try:
            chunk = s.recv(rec_chunk)
            res_data += chunk
        except socket.error:
            break
        if not chunk:
            break
    if res_data:
	try:
       		res_data = res_data.decode()
	except:
		return
    else:
        return '', ''
    if crlf_crlf in res_data:
        res_sep = crlf_crlf
    elif lf_lf in res_data:
        res_sep = lf_lf
    if res_sep not in [crlf_crlf, lf_lf] or res_data.startswith('<'):
        return '', res_data
    content = res_data.split(res_sep)
    banner, body = "".join(content[:1]), "".join(content[1:])
    times = str(datetime.now())
    try:
	with print_lock:
		cursor.execute("""INSERT INTO network (time,ip,data) VALUES (%s,%s,%s)""",(times,ip,banner))
		db.commit()
	#with print_lock:
	#	print "Task COm"
    except Exception as e:
		print e
		print "MySQL Error"
		
def threader():
    while True:
        worker = q.get()
        http_banner_grabber(worker)
        q.task_done()
q = Queue()
count=0
for x in range(200):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

# Change IP Range accordingly By default its set for all IPs #################################
# IPs format eg. 1.1.1.1 means ip1.ip2.ip3.ip4 #################################

for ip1 in range(1,255):
	for ip2 in range(1,255):
		for ip3 in range(1,255):
			for ip4 in range(1,255):
				ip_dest = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)	
				try:
					count=count+1
					q.put(ip_dest)
				except Exception as e:
					print e
					continue
					
q.join()
print "Total Ips Scanned:" +str(count)
end_time = datetime.now()
print str(end_time)
print "Total Time of the Scan:" + str(end_time-start_time)
