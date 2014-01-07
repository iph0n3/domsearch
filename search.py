#-*-coding: utf-8 -*-
#@author: Titans
#@date: 2013/09/18


import os
import re
import sys

class SearchDir():
	def __init__(self):
		pass

	def run(self, path='', deepth=0):
		files, path = self.search(path)
		#self.domxss(path, files)
		
		filesnew = []
		for i in range(0, len(path)):
			pathnew = path[i]
			file = files[i]
			for j in file:
				filesnew.append(pathnew + '\\'+ j)
		
		self.domxss(filesnew)
		raw_input('[+] print any key to end>')

	def search(self, path='', deepth=0):
		dir = []
		path = []
		for dirpath, subpath, files in os.walk(os.getcwd()):
			path.append(dirpath)
			dir.append(files)	
		return dir, path


	def domxss(self,files):
		vuls = []
		curpath = os.getcwd()
		payloads_get = [
				'document.location', 
				'document.URL', 
				'document.URLUnencoded', 
				'document.referrer', 
				'window.location',
				'location.href',
				'location',
				'document.cookie',
				
				]
		payloads_eval = [
				'document.write', 
				'document.writeln', 
				'document.body.innerHtml', 
				'eval',
				'window.execScript', 
				'window.setInterval',
				'window.setTimeout',
				'window.open', 
				'innerHTML',
				'outerHTML',
				]
		swfs = []   #添加swf文件的检测
		for file in files:
			
			f = open(file, 'r')
			content = f.read()
			f.flush()
			f.close()
			danger_g = []
			danger_e = []
			print file

			if '.swf' in file:   #添加swf文件的检测
				swfs.append(file)

			print '[+] Now checking %s'%file
			for p_get in payloads_get:
			
				if re.search(p_get, content, re.I) != None:
					danger_g.append(p_get)		
			if len(danger_g) >0:		
				for p_eval in payloads_eval:
					if re.search(p_eval, content, re.I):	
						danger_e.append(p_eval)

			if len(danger_e) >0 and ('search.py' not in file):
				get = ''
				for i in danger_g:
					get = get + ' ' + i	
				evl = ''
				for i in danger_e:
					evl = evl + ' ' + i
				vul = file.replace(curpath+ '\\', '') + '\n==%s  \n==%s'%(get, evl)
				vuls.append(vul)
			else:
				pass
		f = open('1.txt', 'w+')
		for vul in vuls:
			result = '=============================\n' + vul
			print result
			f.write(result+ '\n')
		f.close()
		#下面是swf文件
		f_swf = open('swf.txt', 'w+')
		for swf in swfs:
			print swf
			f_swf.write(swf +'\n')
		f_swf.close()


			
			

if __name__ == '__main__':
	global myself
	myself = sys.argv[0].replace(os.getcwd()+ '\\','')
	
	search = SearchDir()
	search.run(os.getcwd())




	
	
	# print files

#if __name__ == '__main__':
