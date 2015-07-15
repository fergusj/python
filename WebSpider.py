import urllib2
import re
import sys
import chardet  #chardet��һ���ǳ�����ı���ʶ��ģ�顣
import threading
import time
#reload(sys)
#sys.setdefaultencoding('utf-8') 

rawProxyList = []
checkedProxyList = []

#�˸�Ŀ����վ
targets = ['http://www.proxy360.cn/Region/Brazil','http://www.proxy360.cn/Region/China','http://www.proxy360.cn/Region/America','http://www.proxy360.cn/Region/Taiwan',
           'http://www.proxy360.cn/Region/Japan','http://www.proxy360.cn/Region/Thailand','http://www.proxy360.cn/Region/Vietnam','http://www.proxy360.cn/Region/bahrein']

#����
retext = '''<span class="tbBottomLine" style="width:140px;">[\r\n\s]*(.+?)[\r\n\s]+</span>[\r\n\s]*'''
retext += '''<span class="tbBottomLine" style="width:50px;">[\r\n\s]*(.+?)[\r\n\s]*</span>[\r\n\s]*'''
retext += '''<span class="tbBottomLine " style="width:70px;">[\r\n\s]*.+[\r\n\s]*</span>[\r\n\s]*'''
retext += '''<span class="tbBottomLine " style="width:70px;">[\r\n\s]*(.+?)[\r\n\s]*</span>[\r\n\s]*'''
p = re.compile(retext,re.M)

#��ȡ�������
class ProxyGet(threading.Thread):
    def __init__(self,target):
        threading.Thread.__init__(self)
        self.target = target
        
    def getProxy(self):
        print "Ŀ����վ�� " + self.target
        req = urllib2.urlopen(self.target)
        result = req.read()
        #print chardet.detect(result)
        matchs = p.findall(result)
        for row in matchs:
            ip = row[0]
            port = row[1]
            address = row[2].decode("utf-8").encode("gbk")
            proxy = [ip,port,address]
            #print proxy
            rawProxyList.append(proxy)
            
    def run(self):
        self.getProxy()       
        
        
#����������    
class ProxyCheck(threading.Thread):
    def __init__(self,proxyList):
        threading.Thread.__init__(self)
        self.proxyList = proxyList
        self.timeout = 5
        self.testUrl = "http://www.baidu.com/"
        self.testStr = "030173"
        
    def checkProxy(self):
        cookies = urllib2.HTTPCookieProcessor()
        for proxy in self.proxyList:
            proxyHandler = urllib2.ProxyHandler({"http" : r'http://%s:%s' %(proxy[0],proxy[1])})  
            #print r'http://%s:%s' %(proxy[0],proxy[1])
            opener = urllib2.build_opener(cookies,proxyHandler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')]
            #urllib2.install_opener(opener)
            t1 = time.time()
            
            try:
                #req = urllib2.urlopen("http://www.baidu.com", timeout=self.timeout)
                req = opener.open(self.testUrl, timeout=self.timeout)
                #print "urlopen is ok...."
                result = req.read()
                #print "read html...."
                timeused = time.time() - t1
                pos = result.find(self.testStr)
                #print "pos is %s" %pos
                
                if (pos > -1):
                    checkedProxyList.append((proxy[0],proxy[1],proxy[2],timeused))
                    #print "ok ip: %s %s %s %s" %(proxy[0],proxy[1],proxy[2],timeused)
                else:
                    continue
                
            except Exception,e:
                print e.message
                continue
                       
    def sort(self):
        sorted(checkedProxyList,cmp=lambda x,y:cmp(x[3],y[3]))
                 
    def run(self):
        self.checkProxy()
        self.sort()
                
if __name__ == "__main__":
    getThreads = []
    checkThreads = []
    
    #��ÿ��Ŀ����վ����һ���̸߳���ץȡ����
    for i in range(len(targets)):
        t = ProxyGet(targets[i])
        getThreads.append(t)
        
    for i in range(len(getThreads)):
        getThreads[i].start()
        
    for i in range(len(getThreads)):
        getThreads[i].join()        
        
    print ".......................�ܹ�ץȡ��%s������......................." %len(rawProxyList)    
    
    
    #����20���̸߳���У�飬��ץȡ���Ĵ���ֳ�20�ݣ�ÿ���߳�У��һ��
    for i in range(20):
        t = ProxyCheck(rawProxyList[((len(rawProxyList)+19)/20) * i:((len(rawProxyList)+19)/20) * (i+1)])
        checkThreads.append(t)
    
    for i in range(len(checkThreads)):
        checkThreads[i].start()
        
    
    for i in range(len(checkThreads)):
        checkThreads[i].join()
        
     
    print ".......................�ܹ���%s������ͨ��У��......................." %len(checkedProxyList)    
        
    #�־û�    
    f= open("D:\\t1.txt",'w+')
    for proxy in checkedProxyList:
        print "checked proxy is: %s:%s\t%s\t%s\n" %(proxy[0],proxy[1],proxy[2],proxy[3])
        f.write("%s:%s\t%s\t%s\n"%(proxy[0],proxy[1],proxy[2],proxy[3]))
    f.close()  