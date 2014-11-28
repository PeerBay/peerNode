
		
link=""
#~ from htmltreediff import diff


import urllib2
import web
from lxml.html.diff import htmldiff as diff
from lxml.cssselect import CSSSelector as query
from lxml.etree import fromstring
from lxml.html import tostring
from pyquery import PyQuery as pq
from lxml import etree
global sitelist
sitelist={}
urls = (
'^/get/?(.*)$','Proxy'
)

proxy = urllib2.ProxyHandler({'http': '127.0.0.1:8118'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
insert=query('ins')
delete=query('del')
class Proxy:
	def GET(self,link):
		web.header('Access-Control-Allow-Origin',      '*')
		link=web.webapi.urllib.unquote(link)
		return diffRequest(link)
		
newDom=""

def diffRequest(link):
	global newDom
	inserts=[]
	k=0
	html=urllib2.urlopen(link)
	html=html.read().decode("utf8")
	url=link.split("/")[2]
	print 
	if  url in sitelist:
		last=len(sitelist[url])-1
		diffential=diff(html,sitelist[url][last])
		#~ h = fromstring(diffential)
		#~ h = diffential
		dom=pq(diffential)
		domdel=dom("del")
		domins=dom("ins")
		lendomins=len(domins)
		print dir(domins[1]),dom("ins")[1].text
		for i in domins:
			inserts.append({"ins":i.text})
		for i in dom("del"):
			if k>=lendomins-1:
				inserts.append({"del":i.text})
			else:
				inserts[k]["del"]=i.text
			k+=1
								
		return inserts
			
	else:
		sitelist[url]=[html]	
		return html



class MyApplication(web.application):
    def run(self, port=8889, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=8889)
		







#~ import n2n
#~ 
#~ def startProxy():
	#~ 
#~ def startAnonymousProxy():
#~ 
#~ def stopProxy():
#~ 
#~ def banPeer():	
