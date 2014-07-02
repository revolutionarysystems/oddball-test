print "."
import sys
import urllib

print "."
import setPath
reload(setPath)
import HttpCall
reload(HttpCall)

from java.io import File
from java.util import Date


uri = "http://localhost:8080"
service = "/oddball-service"
#uri = "http://localhost:8090"
#service = "/redirect"


sessions = ["ab10", "ab11", "ab12", "ab13", "ab14", "ab15", "ab16", "ab17", "ab18", "ab19", "ab20", "ab21", "ab22"]
users = ["a111", "a123", "b234", "c345", "d456", "e567", "mikeytest"]
subscriptions = ["eCK-1000", "eCK-1001", "eCK-1002", "eCK-1003", "eCK-1004", "eCK-1005"]
sampleData = [
#        '{ "case":"1000"  }',
        '{ "case":"1000", "whatsit": {}, "accountId": "testbug"  }',
        '{ "browser":"chrome", "device": {"platform": "Win32","screen": {"availWidth": "1600","availHeight": "870"},"pixelRatio": "1"}, "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "{accountId}"  }',
#        '{ "browser":"chrome", "device": {"platform": "Win32","screen": {},"pixelRatio": "1"}, "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "revsys-master-account"  }',
#        '{ "browser":"chrome", "platform":"Win", "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "{accountId}"  }',
#        '{ "browser":"firefox", "platform":"Win32", "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "{accountId}"       }',
#        '{ "browser":"safari", "platform":"ios", "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "{accountId}"       }',
#        '{ "browser":"safari", "platform":"Android", "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "{accountId}"       }',
#        '{ "browser":"safari", "platform":"MacOS", "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "{accountId}"       }',
#        '{ "browser":"chrome", "platform":"Win32", "screen": {"availWidth": 1600}, "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "{accountId}"       }',
#        '{ "browser":"chrome", "platform":"Win32", "screen": {"availWidth": 550}, "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "{accountId}"       }',
#        '{ "browser":"chrome", "platform":"Win64", "availWidth": 550, "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "{accountId}"     }',
#        '{ "browser":"chrome", "platform":"Win64", "screen": {"availWidth": 500}, "sessionId": "{sessionId}", "userId": "{userId}", "accountId": "{accountId}"       }',
        ]

#clearData = {"ruleSet":"ECBase", "action":"clear"}
#HttpCall.callHttpGET(uri, service+"/"+clearData["ruleSet"]+"/clear", {}).strip()

retrieveData = {"ruleSet":"ECBase"}
fullUri = uri+service+"/"+retrieveData["ruleSet"]+"/bin/reload"
print fullUri
res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/bin/reload",{}).strip()
print res

print


print Date()
for i in range(0):
    for case in sampleData:
        data = {"ruleSet":"ECBase", "case":case.replace('{sessionId}', sessions[8 * i%len(sessions)]).replace('{userId}', users[i%len(users)]).replace('{accountId}', subscriptions[i%len(subscriptions)])}
        res=HttpCall.callHttpGET(uri, service+"/"+data["ruleSet"], data).strip()
        print res
print
print Date()
    
def accountCases(account):
    retrieveData = {"ruleSet":"ECBase"}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/case", {"account":account}).strip()
    return res

def sessionCases(account, session):
    retrieveData = {"ruleSet":"ECBase", "sessionId":session}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/sessionId/"+retrieveData["sessionId"], {"account":account}).strip()
    return res

def userCases(account, user):
    retrieveData = {"ruleSet":"ECBase", "userId":user}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/userId/"+retrieveData["userId"], {"account":account}).strip()
    return res

def sessions(account):
    retrieveData = {"ruleSet":"ECBase"}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/sessionId/", {"account":account}).strip()
    return res


def users(account):
    retrieveData = {"ruleSet":"ECBase"}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/userId/", {"account":account}).strip()
    return res

def query1(account):
    retrieveData = {"ruleSet":"ECBase", "query":'{ "case.browser": "firefox" }'}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/query/", {"query":retrieveData["query"], "account":account}).strip()
    return res

def queryPlatform(account, platform):
    retrieveData = {"ruleSet":"ECBase", "query":'{ "case.device.platform": '+platform+' }'}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/query/", {"query":retrieveData["query"], "account":account}).strip()
    return res

def query2(account):
    retrieveData = {"ruleSet":"ECBase", "query":'{ "tags": "WinXX", "case.userId" : "mikeytest"}'}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/query/", {"query":retrieveData["query"], "account":account}).strip()
    return res

def query3(account):
    mins_ago=Date().getTime() - 18 * 60 * 1000
    retrieveData = {"ruleSet":"ECBase", "query":'{ "tags": "WinXX", "case.userId" : "mikeytest", "timeStamp": { "$gt": "'+str(mins_ago)+'"} }'}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/query/", {"query":retrieveData["query"], "account":account}).strip()
    return res

def queryRecent(account, mins):
    mins_ago=Date().getTime() - mins * 60 * 1000
    retrieveData = {"ruleSet":"ECBase", "query":'{ "timeStamp": { "$gt": "'+str(mins_ago)+'"} }'}
    print retrieveData["query"]
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/query/", {"query":retrieveData["query"], "account":account}).strip()
    return res
def bins(account):
    retrieveData = {"ruleSet":"ECBase"}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/bin/",{"account":account}).strip()
    return res

def binCases(account, bin):
    retrieveData = {"ruleSet":"ECBase","bin":bin}
    res = HttpCall.callHttpGET(uri, service+"/"+retrieveData["ruleSet"]+"/bin/"+retrieveData["bin"],{"account":account}).strip()
    return res


def evalJSON(json):
    null = None
    false = 0
    true = 1
    return eval(json)

def show(casesStr):
    for case in evalJSON(casesStr):
        print case
    print

print "Cases"
show(accountCases("revsys-master-account"))
print "Sessions"
sessions = sessions("echo-central-master-user")
for session in evalJSON(sessions):
    print "Session = ", session
    show(sessionCases("echo-central-master-user", session))
print "Users"
users = users("echo-central-master-user")
for user in evalJSON(users):
    print "User = ", user
    #show(userCases("echo-central-master-user", user))
#print query1("eCK-1000")
#print query2("eCK-1005")

print "Windows"
#show(queryPlatform("echo-central-master-user", '"Win32"'))
print "Linux"
show(queryPlatform("echo-central-master-user", '{ "$regex": "Linux.*" }' ))

print "Windows - RevSys"
show(queryPlatform("revsys-master-account", '"Win32"'))


show(queryRecent("echo-central-master-account", 5))
show(queryRecent("echo-central-master-user", 5))
show(queryRecent("revsys-master-account", 5))
#show(queryRecent("_all", 5))
#print bins("eCK-1005")
#print binCases("eCK-1005", "Mybin4")
