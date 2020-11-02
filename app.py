import os

print("HEY SALAS do you want a start a new project? please choose a domain name\r\n")
vhost = input()
cmd = "mkdir /var/www/html/{0}".format(vhost)
os.system(cmd)
cmd = "chown -R $USER:$USER /var/www/html/{0}".format(vhost)
os.system(cmd)
 
cmd = "chmod -R 755 /var/www/html/{0}".format(vhost)
os.system(cmd)
 
 

f_name = '/var/www/html/{0}/index.html'.format(vhost)
f = open(f_name, 'w')
f.write("<html><head><title>This is an Index Page</title></head><body><h1>WAS CREATE WITH SALAS_vhost</h1></body></html>")
f.close()
 
f_name = '/etc/apache2/sites-available/{0}.conf'.format(vhost)
f_content = """<VirtualHost *:80>\r\n
                 ServerAdmin webmaster@localhost\r\n
                 ServerName {0}\r\n
                 ServerAlias www.{0}\r\n
                 DocumentRoot /var/www/html/{0}\r\n
                 </VirtualHost>""".format(vhost)
f =  open(f_name, 'w')
 
f.write(f_content)
f.close()

cmd = "a2ensite {0}".format(vhost)
os.system(cmd)
 
cmd = "systemctl restart apache2"
os.system(cmd)

f_n = '/etc/hosts'
f_c = '127.0.0.1    {0}'.format(vhost)
sf = open(f_n,'a')
sf.write('\n')
sf.write(f_c)

sf.close()
cmd = 'code /var/www/html/{0}'.format(vhost)
os.system(cmd) 