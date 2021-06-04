#sezer create

from skpy import Skype
import subprocess
from optparse import OptionParser

def sendMessage(user,password,skypn,msg):
	sk = Skype(user, password)
	ch = sk.contacts[skypn].chat
	ch.sendMsg(msg)

def getdate():
	proc = subprocess.Popen('timedatectl | grep "Local time:" | awk \'{print $3}\' ',stdout=subprocess.PIPE,shell=True)
	(out, err) = proc.communicate()
	out = out.decode('utf-8').strip()
	return out

def checkdate():
	gymDate = ['monday','tuesday','Thursday','Fri']
	currentday  = getdate()
	for xday in gymDate:
		if xday == currentday:
			return True
			break

if __name__ == '__main__':
    try:
        optParser = OptionParser()
        optParser.add_option('-u', '--username', dest='u', type=str, default=None, help='username from get skype')
        optParser.add_option('-p', '--password', dest='p', type=str, default=None, help='password from get skype')
        optParser.add_option('-s', '--skypname', dest='n', type=str, default=None, help='skypname from get skype')
        optParser.add_option('-m', '--message', dest='msg', type=str, default=None, help='enter the send for username')

        options, args = optParser.parse_args()
        if options.u is not None:
           if checkdate():
              sendMessage(options.u,options.p,options.n,options.msg)
        else:
            optParser.print_help()
    except Exception as e:
        print(e)
    
