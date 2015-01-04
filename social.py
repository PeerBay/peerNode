
class User():
	#~This class gives all functions needed for user entities
	def createPendingUser(username,public_key):
		#~ a doc couchdb/domainname/username {key:public_key,pending:true} is created
		#~ the doc is pending until the admin accepts it.
	def createUser(username):
		#~ check if admin with isAdmin(user_ctx)
		#~ update doc couchdb/domainname/username {key:public_key,pending:false}
		#~ create database with username db name(rcouch:dropbox).
		#~ create public database with username db name(not rcouch).
		
		 
	def deleteUser(username):
		#~Admin only
	def modifyUser(username)	 
	def createPrivateEdge(username):
		#~ a obsfucated network name is given to an edge and name and password are returned to the user
		
	def addFriend(username,domain,key):
		#~ public edge generates the domain name into an subnet and a network name( tun name is handled by n2n library)
		#~ public=n2n.publicedge(domain)
		#~ default gateway and couchdb address is generated based domain_match
		#~ gateway=n2n.gateway(domain)
		#~ leave friendRequest on public db gateway/domain/ with domain ,network ,password 
		 
		 
	def publicShare(post):
		#~ move this to javascript
		
	def privateShare(post,users):		
		#~ move this to javascript
	def deleteFriend():
	def friendRequest(to):
	def supernodeData():
	def acceptFriend():
	def checkForRequests():
	def changeDomain():
	def addDomain():
	def createEdge():
	def inviteFriendsToEdge():
	def createPseudoUser():	
	def isAdmin():										

class Admin()

