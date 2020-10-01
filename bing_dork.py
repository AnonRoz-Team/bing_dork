#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
#Maklum kalo berantakan ster
G = '\033[0;32m'
Y = '\033[0;33m'
C = '\033[0;36m'
W = '\033[0;37m'
R = '\033[0;31m'
import requests,os,sys
from bs4 import BeautifulSoup
def logo():
	os.system('clear')
	print '''%s
    ____  _
   / __ )(_)___  ____ _   %sCoded by D4RKSH4D0WS%s
  / __  / / __ \/ __ `/   %sIG @anonroz_team%s
 / /_/ / / / / / /_/ /    %sFB gg.gg/AnonRoz-Team%s
/_____/_/_/ /_/\__, /     Bing Dorker
              /____/
'''%(C,W,C,W,C,W,C)
def main():
	try:
		logo()
		print '%s[%s1%s] Single\n%s[%s2%s] Mass'%(W,G,W,W,G,W)
		chc=raw_input('\n%s[%s?%s] Choice : '%(W,R,W))
		if chc == '1':single()
		elif chc == '2':mass()
		else:exit('bye goblok')
	except requests.exceptions.ConnectionError:exit('%s[%s!%s] Check internet'%(W,R,W))
	except IOError:exit('%s[%s×%s] File does not exist'%(W,R,W))
	except KeyboardInterrupt:exit('\n%s[%s!%s] Exit'%(W,R,W))
def single():
	logo()
	dork=raw_input('%s[%s?%s] Input dork : '%(W,G,W))
	page=raw_input('%s[%s?%s] Input page : '%(W,G,W))
	c=0
	print
	for taek in range(int(page)):
		c+=11
		res=requests.get('http://www.bing.com/search?q='+dork+'&first='+str(c),headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
		soup=BeautifulSoup(res.text,'html.parser').find_all('ol')
		if 'There are no results for' in str(soup):print '%s[%s!%s] There are no results for %s'%(W,R,W,dork);continue
		for crot in soup:
			try:
				for site in crot.find_all('a'):
					if '/search?q' in site['href']:continue
					else:print '    '+site['href'];open('1','a+').write(site['href']+'\n')
			except:break
	same=[]
	if os.path.exists('1')==False:exit('\n%s[%s!%s] There are no results'%(W,R,W))
	for domain in open('1').read().split('\n'):
		if 'bing' in domain:continue
		elif 'microsoft' in domain:continue
		elif 'exploit-db' in domain:continue
		elif domain in same:continue
		else:same.append(domain);open('results.txt','a+').write(domain+'\n')
	os.system('rm -rf 1')
	print '\n%s[%s*%s] Result filter menu\n\n    %s[%s1%s] Full path\n    %s[%s2%s] Just domain'%(W,R,W,W,G,W,W,G,W)
	chc=raw_input('\n%s[%s?%s] Choice : '%(W,R,W))
	if chc == '1':exit('\n%s[%s✓%s] Done, saved in results.txt'%(W,G,W))
	elif chc == '2':
		for site in open('results.txt').read().split('\n'):
			try:
				#print site.split('/')[0]+'//'+site.split('/')[2]
				open('results_domain.txt','a+').write(site.split('/')[0]+'//'+site.split('/')[2]+'\n')
			except:break
		exit('\n%s[%s✓%s] Done, saved in results_domain.txt'%(W,G,W))
	else:exit('\n%s[%s✓%s] Done, saved in results.txt'%(W,G,W))
def mass():
	logo()
	file=open(raw_input('%s[%s?%s] Input file : '%(W,G,W))).read().splitlines()
	page=raw_input('%s[%s?%s] Input page : '%(W,G,W))
	c=0
	for dork in file:
		print '\n%s[%s!%s] %sProccess dork %s%s\n'%(W,Y,W,Y,dork,W)
		for taek in range(int(page)):
			c+=11
			res=requests.get('http://www.bing.com/search?q='+dork+'&first='+str(c), headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
			soup=BeautifulSoup(res.content, 'html.parser').find_all('ol')
			if 'There are no results for' in str(soup):print '%s[%s!%s] There are no results for %s'%(W,R,W,dork);continue
			for crot in soup:
				try:
					for site in crot.find_all('a'):
						if '/search?q' in site['href']:continue
						else:print '    '+site['href'];open('1','a+').write(site['href']+'\n')
				except:break
	same=[]
	if os.path.exists('1')==False:exit('\n%s[%s!%s] There are no results'%(W,R,W))
	for domain in open('1').read().split('\n'):
		if 'bing' in domain:continue
		elif 'microsoft' in domain:continue
		elif 'exploit-db' in domain:continue
		elif domain in same:continue
		else:same.append(domain);open('results.txt','a+').write(domain+'\n')
	os.system('rm -rf 1')
	print '\n%s[%s*%s] Result filter menu\n\n    %s[%s1%s] Full path\n    %s[%s2%s] Just domain'%(W,R,W,W,G,W,W,G,W)
	chc=raw_input('\n%s[%s?%s] Choice : '%(W,R,W))
	if chc == '1':exit('\n%s[%s✓%s] Done, saved in results.txt'%(W,G,W))
	elif chc == '2':
		for site in open('results.txt').read().split('\n'):
			try:
				#print '    '+site.split('/')[0]+'//'+site.split('/')[2]
				open('results_domain.txt','a+').write(site.split('/')[0]+'//'+site.split('/')[2]+'\n')
			except:break
		exit('\n%s[%s✓%s] Done, saved in results_domain.txt'%(W,G,W))
	else:exit('\n%s[%s✓%s] Done, saved in results.txt'%(W,G,W))
if __name__=='__main__':
	main()
