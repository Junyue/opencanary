from opencanary.modules import CanaryService
from twisted.internet import reactor

from datetime import datetime
from apscheduler.schedulers.twisted import TwistedScheduler
#import logging

#logging.basicConfig(level=logging.INFO,
#        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#        datafmt='%a, %d %b %Y %H:%M:%S',
#        ilename='/var/tmp/opencanary.log',
#        filemode='a')

class CanaryHost(CanaryService):
    NAME = "host"

    def __init__(self, config=None, logger=None):
        CanaryService.__init__(self, config, logger)
        self.hostname = config.getVal('device.node_id')
        self.localip = config.getVal('device.listen_addr')
        self.serverip = config.getVal('server.ip')
        self.last_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self.status = "online"
        self.logtype = logger.LOG_HOST
    def hoststatus(self):
        import json
        hostjson = json.dumps({
            "lasttime": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
            "hostname": self.hostname,
            "ip": self.localip,
            "status": self.status
        })
        try:
            import urllib2
            url = 'http://'+self.serverip+'/host/'
            req  = urllib2.Request(url, hostjson, {'Content-Type':'application/json'})
            f = urllib2.urlopen(req)
            response = f.read()
            #self.logger.log(response)
            f.close()
        except urllib2.URLError, e:
            e = {"Hoststatus urllib2 Error:":str(e)}
            self.logger.error(e)

    def startYourEngines(self):
        sched = TwistedScheduler()
        sched.start()
        if sched.get_job('host_status'):
            pass
        else:
            sched.add_job(self.hoststatus, 'interval', seconds=10, id='host_status')

CanaryServiceFactory = CanaryHost