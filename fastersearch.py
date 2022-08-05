import requests
import threading as th
from rich import print
import time
import argparse
import textwrap
import os

# Creating an interface
parser = argparse.ArgumentParser(description="FasterSearch is a beautifull script for the DirSearch",
formatter_class = argparse.RawDescriptionHelpFormatter,
epilog=textwrap.dedent('''Exemption:\n
fastersearch.py -u http://example.com -s <status(200,403...) Enter "all" for all != 404>
'''))

#help
def help():
    from rich import print
    print("\n[bold]fastersearch.py -u and -s missing check the [-h] or [--help] to display the help command[bold]")
    os.system("python fastersearch.py -h")
    return ''

parser.add_argument('-u','--url',type=str, help='Enter URL')
parser.add_argument('-s','--code',type=str,help='Enter status you want')
args = parser.parse_args()

url = args.url
code = args.code

def title():
    print('''[bold red]
    ______           __            [blue]_____                      __[/blue]  
   / ____/___ ______/ /____  _____[blue]/ ___/___  ____ ___________/ /_ [/blue]
  / /_  / __ `/ ___/ __/ _ \/ ___/[blue]\__ \/ _ \/ __ `/ ___/ ___/ __ \\\\[/blue]
 / __/ / /_/ (__  ) /_/  __/ /   [blue]___/ /  __/ /_/ / /  / /__/ / / /[/blue]
/_/    \__,_/____/\__/\___/_/   [blue]/____/\___/\__,_/_/   \___/_/ /_/[/blue]


    [/bold red]''')


def search(from_,to_,code=code,url=url):
    try:
        if __name__ == '__main__':
            wd = open('wordlist.txt','r')              
            x = 0
            content = wd.readlines()
            directory = content[from_:to_]
            if code == '':
                code = 'all'
            if url[-1] == '/':
                url = url[0:-1]                                       
            for word in directory:
                url_c = url+'/'+word[0:-1]
                req = requests.get(url_c)
                x += 1
                if code == 'all':
                    if  req.status_code != 404:
                        print('[ '+str(req.status_code)+' ]  '+ url+' ----> /'+word)
                        #print(str(x)+'/1837\n')
                    #else:
                    #    print(word)
                else:
                    if  req.status_code == int(code):
                        print('[ '+str(req.status_code)+' ]  '+ url+' ----> /'+word)
                        #print(str(x)+'/1837\n')
                #print('Sto a: '+str(x)+'/1837')
    except:
        nothing = 'nothing'

def timeout():
    time.sleep(35)
    quit()

def DirSearch():
    try:    
        if __name__ == '__main__':
            title()
            print('[bold green3][  [orange1]Scan...[/orange1]  ][/bold green3]')
            th.Thread(target=timeout).start()
            th.Thread(target=search,args=(0,56)).start()    #1
            th.Thread(target=search,args=(57,112)).start()
            th.Thread(target=search,args=(113,168)).start()
            th.Thread(target=search,args=(169,224)).start()
            th.Thread(target=search,args=(225,280)).start()    #5
            th.Thread(target=search,args=(281,336)).start()
            th.Thread(target=search,args=(337,392)).start()
            th.Thread(target=search,args=(393,448)).start()
            th.Thread(target=search,args=(449,504)).start()
            th.Thread(target=search,args=(505,560)).start()    #10
            th.Thread(target=search,args=(561,616)).start()
            th.Thread(target=search,args=(167,672)).start()
            th.Thread(target=search,args=(673,728)).start()
            th.Thread(target=search,args=(729,784)).start()
            th.Thread(target=search,args=(785,840)).start()    #15
            th.Thread(target=search,args=(841,896)).start()
            th.Thread(target=search,args=(897,952)).start()
            th.Thread(target=search,args=(953,1008)).start()
            th.Thread(target=search,args=(1009,1064)).start()
            th.Thread(target=search,args=(1065,1120)).start()    #20
            th.Thread(target=search,args=(1121,1176)).start()
            th.Thread(target=search,args=(1177,1232)).start()
            th.Thread(target=search,args=(1233,1288)).start()
            th.Thread(target=search,args=(1289,1344)).start()
            th.Thread(target=search,args=(1345,1400)).start()    #25
            th.Thread(target=search,args=(1401,1456)).start()
            th.Thread(target=search,args=(1457,1512)).start()
            th.Thread(target=search,args=(1513,1568)).start()
            th.Thread(target=search,args=(1569,1624)).start()
            th.Thread(target=search,args=(1625,1680)).start()    #30
            th.Thread(target=search,args=(1681,1736)).start()
            th.Thread(target=search,args=(1737,1792)).start()
    except:
        print('[bright_red]Error[/bright_red]')

DirSearch()