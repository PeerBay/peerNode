import subprocess
import couchdb
import time

local_couch="http://admin:admin@localhost:5984"
remote_couch="http://nodes.iriscouch.com"
nodes=couchdb.Server(remote_couch)["nodes"]
couch = couchdb.Server(local_couch)
if "domains" not in couch:
	domains=couch.create("domains")
else:
	domains=couch["domains"]




def createKeys():	
	keys= subprocess.check_output(["kadnode","--daemon","--auth-gen-keys"])
	keys=keys.split("\n")
	public_key=keys[0].replace("public key: ","")
	secret_key=keys[1].replace("secret key: ","")
	return {"public":public_key,"secret":secret_key}
	
#~ def checkDomain():
	#~ 
#~ 
#~ def reportDomainToPublic():
	#~ 
def searchDomain():
	subprocess.call(["kadnode-ctl","lookup",friend+"."+domain+".p2p:"+f_domain_key])	
			
def check_domain(domain_name):
	if domain_name in nodes:
		return True
	return False			
def save_domain(domain_name,public):
	try:
		nodes[domain_name]={"public":public}
		return True
	except:
		return False
def restart_announce():
	subprocess.call(["killall","kadnode"])
	cmd=["kadnode"]	
	for i in domains:
		if "secret" in domains[i]:
			print domains[i]["secret"]	
			cmd.append("--auth-add-skey")
			d=i+".p2p:"+domains[i]["secret"]
			cmd.append(d.encode("utf8"))
			cmd.append("--value-id")
			d=i+".p2p"
			cmd.append(d.encode("utf8"))
		else:
			d=i+".p2p:"+domains[i]["public"]
			cmd.append("--auth-add-pkey")
			cmd.append(d.encode("utf8"))
	cmd.append("--daemon")
	cmd.append("--peerfile")
	cmd.append("peers.txt")
	print cmd
	subprocess.call(cmd)	
class Domain:
	restart_announce()
	def announce_domain(self,domain_name):
		if check_domain(domain_name) :
			return False
		keys=createKeys()
		domains[domain_name]=keys
		save_domain(domain_name,keys["public"])
		restart_announce()
		cmd=["kadnode-ctl", "announce", domain_name+".p2p"]
		subprocess.call(cmd)
		return True	

	def announce_user(self,user,domain_name):
		cmd=["kadnode-ctl", "announce", username+"."+domain+".p2p"]
		subprocess.call(cmd)

	def lookup(self,domain_name):
		ready=1
		if domain_name in nodes:
			public_key=nodes[domain_name]["public"].encode("utf8")
			#~ print nodes[domain_name]
			if domain_name not in domains:
				domains[domain_name]=nodes[domain_name]
				restart_announce()	
			print ["kadnode-ctl","lookup",domain_name+".p2p"]	
			#~ while "Search" in subprocess.check_output(["kadnode-ctl","lookup",domain_name+".p2p:"+public_key]):
				#~ time.sleep(1)
			while ready==1:	
				ready=subprocess.call(["kadnode-ctl","lookup",domain_name+".p2p"])
				time.sleep(1)
			ip=subprocess.check_output(["kadnode-ctl","lookup",domain_name+".p2p"])
			return ip
		else:
			print domain_name +" not in nodes."
	def status(self):
		return subprocess.check_output(["kadnode-ctl","status"])
			
		

