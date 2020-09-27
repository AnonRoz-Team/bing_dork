#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#Maklum kalo berantakan ster
G0 = '\033[0;32m'
Y0 = '\033[0;33m'
C0 = '\033[0;36m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
import requests,os,sys
from bs4 import BeautifulSoup
def logo():
	os.system('clear')
	print '''%s
    ____  _                    __           __  
   / __ )(_)___  ____ _   ____/ /___  _____/ /__  %sCoded by D4RKSH4D0WS%s
  / __  / / __ \/ __ `/  / __  / __ \/ ___/ //_/  %sIG @anonroz_team%s
 / /_/ / / / / / /_/ /  / /_/ / /_/ / /  / ,<     %sFB gg.gg/AnonRoz-Team%s
/_____/_/_/ /_/\__, /   \__,_/\____/_/  /_/|_|    Ngedork lah anjim
              /____/
'''%(C0,W0,C0,W0,C0,W0,C0)
def main():
	try:
		logo()
		print '%s[%s1%s] Single\n%s[%s2%s] Mass'%(W0,G0,W0,W0,G0,W0)
		chc=raw_input('\n%s[%s?%s] Choice : '%(W0,R0,W0))
		if chc == '1':single()
		elif chc == '2':mass()
		else:exit('bye goblok')
	except requests.exceptions.ConnectionError:exit('%s[%s!%s] Check internet'%(W0,R0,W0))
	except IOError:exit('%s[%s×%s] File does not exist'%(W0,R0,W0))
	except KeyboardInterrupt:exit('\n%s[%s!%s] Exit'%(W0,R0,W0))
def single():
	logo()
	dork=raw_input('%s[%s?%s] Input dork : '%(W0,G0,W0))
	page=raw_input('%s[%s?%s] Input page : '%(W0,G0,W0))
	c=0
	print
	for taek in range(int(page)):
		c+=11
		res=requests.get('http://www.bing.com/search?q='+dork+'&first='+str(c),headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
		soup=BeautifulSoup(res.text,'html.parser').find_all('ol')
		if len(soup)==2:print '%s[%s!%s] There are no results for %s'%(W0,R0,W0,dork);continue
		for crot in soup:
			try:
				for site in crot.find_all('a'):
					if '/search?q' in site['href']:continue
					else:print '    '+site['href'];open('1','a+').write(site['href']+'\n')
			except:break
	same=[]
	if os.path.exists('1')==False:exit('\n%s[%s!%s] There are no results'%(W0,R0,W0))
	for domain in open('1').read().split('\n'):
		if 'bing' in domain:continue
		elif 'microsoft' in domain:continue
		elif 'exploit-db' in domain:continue
		elif domain in same:continue
		else:same.append(domain);open('results.txt','a+').write(domain+'\n')
	os.system('rm -rf 1')
	print '\n%s[%s*%s] Result filter menu\n\n    %s[%s1%s] Full path\n    %s[%s2%s] Just domain'%(W0,R0,W0,W0,G0,W0,W0,G0,W0)
	chc=raw_input('\n%s[%s?%s] Choice : '%(W0,R0,W0))
	if chc == '1':exit('\n%s[%s✓%s] Done, saved in results.txt'%(W0,G0,W0))
	elif chc == '2':
		for site in open('results.txt').read().split('\n'):
			try:
				#print site.split('/')[0]+'//'+site.split('/')[2]
				open('results_domain.txt','a+').write(site.split('/')[0]+'//'+site.split('/')[2]+'\n')
			except:break
		exit('\n%s[%s✓%s] Done, saved in results_domain.txt'%(W0,G0,W0))
	else:exit('\n%s[%s✓%s] Done, saved in results.txt'%(W0,G0,W0))
def mass():
	logo()
	file=open(raw_input('%s[%s?%s] Input file : '%(W0,G0,W0))).read().splitlines()
	page=raw_input('%s[%s?%s] Input page : '%(W0,G0,W0))
	c=0
	for dork in file:
		print '\n%s[%s!%s] %sProccess dork %s%s\n'%(W0,Y0,W0,Y0,dork,W0)
		for taek in range(int(page)):
			c+=11
			res=requests.get('http://www.bing.com/search?q='+dork+'&first='+str(c), headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
			soup=BeautifulSoup(res.content, 'html.parser').find_all('ol')
			#if len(soup)==2:print '%s[%s!%s] There are no results for %s'%(W0,R0,W0,dork);continue
			for crot in soup:
				try:
					for site in crot.find_all('a'):
						if '/search?q' in site['href']:continue
						else:print '    '+site['href'];open('1','a+').write(site['href']+'\n')
				except:break
	same=[]
	if os.path.exists('1')==False:exit('\n%s[%s!%s] There are no results'%(W0,R0,W0))
	for domain in open('1').read().split('\n'):
		if 'bing' in domain:continue
		elif 'microsoft' in domain:continue
		elif 'exploit-db' in domain:continue
		elif domain in same:continue
		else:same.append(domain);open('results.txt','a+').write(domain+'\n')
	os.system('rm -rf 1')
	print '\n%s[%s*%s] Result filter menu\n\n    %s[%s1%s] Full path\n    %s[%s2%s] Just domain'%(W0,R0,W0,W0,G0,W0,W0,G0,W0)
	chc=raw_input('\n%s[%s?%s] Choice : '%(W0,R0,W0))
	if chc == '1':exit('\n%s[%s✓%s] Done, saved in results.txt'%(W0,G0,W0))
	elif chc == '2':
		for site in open('results.txt').read().split('\n'):
			try:
				#print '    '+site.split('/')[0]+'//'+site.split('/')[2]
				open('results_domain.txt','a+').write(site.split('/')[0]+'//'+site.split('/')[2]+'\n')
			except:break
		exit('\n%s[%s✓%s] Done, saved in results_domain.txt'%(W0,G0,W0))
	else:exit('\n%s[%s✓%s] Done, saved in results.txt'%(W0,G0,W0))
if __name__=='__main__':
	main()
