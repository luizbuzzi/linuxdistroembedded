import SimpleHTTPServer
import SocketServer
import subprocess,psutil,sys

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def do_GET(self):
                list_proc = ""
                for proc in psutil.process_iter():
                     try:
                         pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
                     except psutil.NoSuchProcess:
                         pass
                     else:
                         list_proc += str(pinfo) + "<br>"

                p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
                (_date, err) = p.communicate()
                p_status = p.wait()
                p = subprocess.Popen("uptime", stdout=subprocess.PIPE, shell=True)
                (_up_time, err) = p.communicate()
                p_status = p.wait()
                p = subprocess.Popen("cat /proc/cpuinfo | grep 'model\ name' | uniq", stdout=subprocess.PIPE, shell=True)
                (_model_name, err) = p.communicate()
                p_status = p.wait()
                p = subprocess.Popen("uname -orm", stdout=subprocess.PIPE, shell=True)
                (_sys_ver, err) = p.communicate()
                p_status = p.wait()
                
                

                f = open('./index.html','w')
                        
                message = """<html>
                        <head>
                        <title>Teste</title>
                        </head>
                        <body>
                                System Time: {date_time} <br>
                                Up time: {up_time} <br>
                                Processor Model: {proc_model} <br>
                                Processor Use(%) {proc_use} <br>
                                RAM Memory: {ram} <br>
                                System Version: {version} <br>
                                <br>
                                Process: <br>
                                {process}
                        </body>
                </html>"""
                
                new_message = message.format(date_time = _date,
                                             up_time = _up_time,
                                             proc_model = _model_name,
                                             proc_use = psutil.cpu_percent(interval=1, percpu=True),
                                             ram = psutil.virtual_memory(),
                                             version = _sys_ver,
                                             process = list_proc
                                             )
                                
                f.write(new_message)
                f.close()

                        
                self.path = './index.html'
                return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
                

Handler = MyRequestHandler

server = SocketServer.TCPServer(('0.0.0.0', 8080), Handler)
server.serve_forever()
