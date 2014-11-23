def createDomain(name):
	cmd=["kadnode-ctl", "announce", username+"."+domain+".p2p"]
	subprocess.call(cmd)
def createKeys():	
	keys= subprocess.check_output(["kadnode","--daemon","--auth-gen-keys"])
	keys=keys.split("\n")
	public_key=keys[0].replace("public key: ","")
	secret_key=keys[1].replace("secret key: ","")
	return {"public":public_key,"secret":secret_key}
	
def checkDomain():
	

def reportDomainToPublic():
	
def searchDomain():
	subprocess.call(["kadnode-ctl","lookup",friend+"."+domain+".p2p:"+f_domain_key])	
			
