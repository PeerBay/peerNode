def startTunnel(to=None,password=None,Network=None):
	
def stopTunnel(pid):
	
def saveTunnel(pid=None,to=None,password=None,Network=None):	


def isSupernodeCapable():
	if "is redirected to internal" in subprocess.check_output(['upnpc' ,"-r",supernode_port,'TCP',supernode_port,'UDP']):
		subprocess.Popen(["supernode","-l",supernode_port]) 
		#~ subprocess.call(["upnpc","-r",supernode_port,"UDP"])	
		#~ subprocess.call(["upnpc","-r",supernode_port,"TCP"])
		find_ip_cmd="upnpc -s | grep ExternalIPAddress | sed 's/[^0-9\.]//g'"
		my_external_ip=subprocess.check_output(find_ip_cmd,shell=True)
		my_external_ip=my_external_ip.split("\n")[0]
		domain_supernode=my_external_ip+":"+supernode_port	
		return True
	else:
		find_ip_cmd="upnpc -s | grep ExternalIPAddress | sed 's/[^0-9\.]//g'"
		my_external_ip=subprocess.check_output(find_ip_cmd,shell=True)
		my_external_ip=my_external_ip.split("\n")[0]
		domain_supernode=my_external_ip+":"+supernode_port	
		return False
		
