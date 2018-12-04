import socket
import select

import threading

sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sk1.bind(('192.168.1.250', 8888))

sk1.listen(1000)

#可读
input = [sk1,]

cli_list = []

output = []
other = []

#保存客户端的信息
cli_list = []

def func(data, conn):
	#print(conn)
	for item in cli_list:
		if item["client"] == conn:
			#print("recv: %s"%(data))
			fp = open(item[fp], "a+")
			fp.write(str(data))
			fp.close()
			
			dict = json.loads(str(data))
			
			#插入数据库

while True:
	r_list, w_list, e_list = select.select(input, [], [], 1)
	
	#遍历r_list
	for conn in r_list:
		#如果是服务端就绪，代表有新的客户端连接
		if conn == sk1:
			#接收新的客户端的连接请求
			cli, addr = conn.accept()
			input.append(cli)
			print("hello new guys: ", addr)
			cli_dict = {}
			file_name = addr[0] + '_' + str(addr[1])
			#fp = open(file_name, "a+")
			
			#cli_dict["fp"] = fp
			cli_dict["fp"] = file_name
			cli_dict["client"] = cli
			cli_list.append(cli_dict)
			print(cli_list)
			#cli_dict = {cli:"192.168.1.100_8888.log"} 
		else:
			data = conn.recv(1024) 
			print("recv: ", data)
			#存log文件
			#创建一个新的线程来处理data
			
			threading.Thread(target=func, args=(data, conn)).start()
				