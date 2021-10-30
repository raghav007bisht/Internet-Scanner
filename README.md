# Internet-Scanner
The script was initially made for scanning internal network devices for port 80 but one can also scan whole internet for HTTP port and see all IPs that are listening on PORT 80

Requirements :
--------------
python 2.7

Dependency :
------------
MySQLdb - pip install MySQLdb

use command In case of error - No module named MySQLdb :
--------------------------------------------------------
  1. pip install mysql-python
  
     "or"
  
  2. pip install mysqlclient

Installation :
--------------
Create MySQL Databse before executing the script

Use follow the commands :-
  1. CREATE USER 'internet'@'localhost' IDENTIFIED BY 'Qwerty@321';
  2. GRANT SELECT ON * . * TO 'internet'@'localhost';
  3. CREATE DATABASE internet;
  4. GRANT ALL PRIVILEGES ON `internet` . * TO 'internet'@'localhost';
  5. CREATE TABLE network (time datetime, ip varchar(255), data varchar(255));
  
  Tested On Platforms :
  ---------------------
  1. Windows 7 and above with XAMPP
  2. Linux Ubuntu 18.0
  
  Screenshot :
  ------------
![ScreenShot](https://raw.githubusercontent.com/raghav007bisht/Internet-Scanner/main/win7.JPG)
