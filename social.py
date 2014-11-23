def announce_domains(domain):
	subprocess.call(["killall","kadnode"])
	couch = couchdb.Server(local_couch)
	if "domains" not in couch:
		domains=couch.create("domains")
	else:
		domains=couch["domains"]	
	if domain not in domains:
		keys= subprocess.check_output(["kadnode","--daemon","--auth-gen-keys"])
		keys=keys.split("\n")
		public_key=keys[0].replace("public key: ","")
		secret_key=keys[1].replace("secret key: ","")
		domains[domain]={"public":public_key,"secret":secret_key}
		tvcouch=couchdb.Server("http://nodes.iriscouch.com")   
		nodes=tvcouch["nodes"]         
		nodes[domain]={"public":public_key}
	cmd=["kadnode"]	
	for i in domains:
		print domains[i]["secret"]	
		cmd.append("--auth-add-skey")
		cmd.append("*."+i+".p2p:"+domains[i]["secret"])
	cmd.append("--daemon")	
	print cmd    
	subprocess.call(cmd)
	time.sleep(10)
	while "Send ping to" not in subprocess.check_output(["kadnode-ctl","import","bttracker.debian.org"]):
		print "kadnode:no response"
		time.sleep(0.5)
		continue
		

def ip_updater():
	while True:
		find_ip_cmd="upnpc -s | grep ExternalIPAddress | sed 's/[^0-9\.]//g'"
		new_ip=subprocess.check_output(find_ip_cmd,shell=True)
		new_ip=my_external_ip.split("\n")[0]
		if new_ip!=old_ip and new_ip!="0.0.0.0":
			tvcouch=couchdb.Server("http://nodes.iriscouch.com")   
			nodes=tvcouch["nodes"]         
			nodes[domain]={"public":public_key,"ip":new_ip}
		old_ip=new_ip
		time.sleep(60)	
