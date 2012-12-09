#!/usr/bin/python
# -*- coding: utf-8 -*-

# SIRISERVER PLUGIN MAKER V.2.0.
# (c) 2012 sullenlook.eu
# by SullenLook <sullenlook@sullenlook.eu>
# http://heroin.sullenlook.eu
# --- FREE SIRISERVER @ ---
# http://siri.sullenlook.eu
# --- SIRISERVER FACEBOOK GROUP ---
# http://facebook.sullenlook.eu]

import time
import os

start = '''\
#!/usr/bin/python
# -*- coding: utf-8 -*-

# SIRISERVER PLUGIN
# (c) 2012 sullenlook.eu
# by SullenLook <sullenlook@sullenlook.eu>
# http://heroin.sullenlook.eu
#
# --- FREE SIRISERVER @ ---
# http://siri.sullenlook.eu
# --- SIRISERVER FACEBOOK GROUP ---
# http://facebook.sullenlook.eu]
#
# erstellt am: ZEIT
# mit SullenLook's SiriServer Plugin Maker
# von http://github.com/sullenlook

from plugin import *

class smalltalk(Plugin):

'''

end = '''\
    def st_fuck(self, speech, language):
  if language == 'de-DE':
	    self.say(u"BBB.")
	else:
	    self.say(u"bbb.")
	self.complete_request()
  
'''

endrandomzwei = '''\
    def st_whatups(self, speech, language):
	if language == 'de-DE':
	    rep = ["BBB","DDD"]
	    self.say(random.choice(rep)
	self.complete_request()
'''

endrandomdrei = '''\
    def st_whatups(self, speech, language):
	if language == 'de-DE':
	    rep = ["BBB","DDD","FFF"]
	    self.say(random.choice(rep)   
	self.complete_request()
'''

einarg = '''\
    @register("de-DE", ".*AAA.*")
    @register("en-US", ".*aaa.*")
'''

zweiarg = '''\
    @register("de-DE", "(.*AAA.*)|(.*CCC.*)")
    @register("en-US", "(.*aaa.*)|(.*ccc.*)")
'''

zweiargDE = '''\
    @register("de-DE", "(.*AAA.*)|(.*CCC.*)")
'''

dreiarg = '''\
    @register("de-DE", "(.*AAA.*)|(.*CCC.*)|(.*EEE.*)")
    @register("en-US", "(.*aaa.*)|(.*ccc.*)|(.*eee.*)")
'''

#######################################################

lang = raw_input('Sprach auswahl: de-DE oder de-DE/en-US ?')
if lang == "de":
	argz = raw_input('1, 2 oder 3 Befehle?')
	if argz == "1":
		endz = raw_input('1, 2 oder 3 Antworten?')
		if endz == "1":
			str1 = raw_input('Einen Befehl oder eine Frage eingeben:')
			str3 = str1
			str2 = raw_input('Aussage oder Antwort eingeben:')
			str4 = str2
			plugin = (start + einarg + end).replace('AAA',str1).replace('BBB',str2).replace('aaa',str3).replace('bbb',str4).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))
		elif  endz == "2":
			str1 = raw_input('Einen Befehl oder eine Frage eingeben:')
			str3 = str1
			str2 = raw_input('Aussage oder Antwort eingeben:')
			str4 = str2
			str6 = raw_input('Zweite Aussage oder zweite Antwort eingeben:')
			plugin = (start + einarg + endrandomzwei).replace('AAA',str1).replace('BBB',str2).replace('DDD',str6).replace('aaa',str3).replace('bbb',str4).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))
		else:
			str1 = raw_input('Einen Befehl oder eine Frage eingeben:')
			str3 = str1
			str2 = raw_input('Aussage oder Antwort eingeben:')
			str4 = str2
			str6 = raw_input('Zweite Aussage oder zweite Antwort eingeben:')
			str11 = raw_input('Dritte Aussage oder dritte Antwort eingeben:')
			plugin = (start + einarg + endrandomdrei).replace('AAA',str1).replace('BBB',str2).replace('DDD',str6).replace('FFF',str11).replace('aaa',str3).replace('bbb',str4).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))

	elif  argz == "2":
		endz = raw_input('1, 2 oder 3 Antworten?')
		if endz == "1":
			str1 = raw_input('Ersten Befehl oder Frage eingeben:')
			str3 = str1
			str5 = raw_input('Zweiten Befehl oder zweite Frage eingeben:')
			str2 = raw_input('Aussage oder Antwort eingeben:')
			str4 = str2
			plugin = (start + zweiargDE + end).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S')).replace('AAA',str1).replace('BBB',str2).replace('CCC',str5).replace('aaa',str3).replace('bbb',str4).replace('ccc',str5).replace('CCC',str5)
		elif  endz == "2":
			str1 = raw_input('Ersten Befehl oder Frage eingeben:')
			str3 = str1
			str5 = raw_input('Zweiten Befehl oder zweite Frage eingeben:')
			str2 = raw_input('Aussage oder Antwort eingeben:')
			str4 = str2
			str6 = raw_input('Zweite Aussage oder zweite Antwort eingeben:')
			plugin = (start + zweiargDE + endrandomzwei).replace('AAA',str1).replace('BBB',str2).replace('CCC',str5).replace('DDD',str6).replace('aaa',str3).replace('bbb',str4).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))
		else:
			str1 = raw_input('Ersten Befehl oder Frage eingeben:')
			str3 = str1
			str5 = raw_input('Zweiten Befehl oder zweite Frage eingeben:')
			str2 = raw_input('Aussage oder Antwort eingeben:')
			str4 = str2
			str6 = raw_input('Zweite Aussage oder zweite Antwort eingeben:')
			str11 = raw_input('Dritte Aussage oder dritte Antwort eingeben:')
			plugin = (start + zweiargDE + endrandomdrei).replace('AAA',str1).replace('BBB',str2).replace('CCC',str5).replace('DDD',str6).replace('FFF',str11).replace('aaa',str3).replace('bbb',str4).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))

	else:
		endz = raw_input('1, 2 oder 3 Antworten?')
		if endz == "1":
			str1 = raw_input('Ersten Befehl oder Frage eingeben:')
			str3 = str1 
			str5 = raw_input('Zweiten Befehl oder zweite Frage eingeben:')
			str8 = raw_input('Dritten Befehl oder dritte Frage eingeben:')
			str2 = raw_input('Aussage oder Antwort eingeben:')
			str4 = str2
			plugin = (start + dreiarg + end).replace('AAA',str1).replace('BBB',str2).replace('CCC',str5).replace('EEE',str8).replace('aaa',str3).replace('bbb',str4).replace('ccc',str5).replace('eee',str8).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))
		elif  endz == "2":
			str1 = raw_input('Ersten Befehl oder Frage eingeben:')
			str3 = str1
			str5 = raw_input('Zweiten Befehl oder zweite Frage eingeben:')
			str8 = raw_input('Dritten Befehl oder dritte Frage eingeben:')
			str2 = raw_input('Aussage oder Antwort eingeben:')
			str4 = str2
			str6 = raw_input('Zweite Aussage oder zweite Antwort eingeben:')
			plugin = (start + dreiarg + endrandomzwei).replace('AAA',str1).replace('BBB',str2).replace('CCC',str5).replace('DDD',str6).replace('EEE',str8).replace('aaa',str3).replace('bbb',str4).replace('ccc',str5).replace('eee',str8).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))
		else:
			str1 = raw_input('Ersten Befehl oder Frage eingeben:')
			str3 = str1
			str5 = raw_input('Zweiten Befehl oder zweite Frage eingeben:')
			str8 = raw_input('Dritten Befehl oder dritte Frage eingeben:')
			str2 = raw_input('Aussage oder Antwort eingeben:')
			str4 = str2
			str6 = raw_input('Zweite Aussage oder zweite Antwort eingeben:')
			str11 = raw_input('Dritte Aussage oder dritte Antwort eingeben:')
			plugin = (start + dreiarg + endrandomdrei).replace('AAA',str1).replace('BBB',str2).replace('CCC',str5).replace('DDD',str6).replace('EEE',str8).replace('FFF',str11).replace('aaa',str3).replace('bbb',str4).replace('ccc',str5).replace('ddd',str6).replace('eee',str8).replace('fff',str11).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))

else:
	argz = raw_input('1, 2 oder 3 Befehle?')
	if argz == "1":
		str1 = raw_input('Einen Befehl oder eine Frage eingeben:')
		str3 = raw_input('Enter a question or a command:')
		str2 = raw_input('Aussage oder Antwort eingeben:')
		str4 = raw_input('Enter a statement or answer:')
		plugin = (start + einarg + end).replace('AAA',str1).replace('BBB',str2).replace('aaa',str3).replace('bbb',str4).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))
	elif argz == "3":
		str1 = raw_input('Einen Befehl oder eine Frage eingeben:')
		str3 = raw_input('Enter a question or a command:')
		str5 = raw_input('Einen 2. Befehl oder eine 2. Frage eingeben:')
		str7 = raw_input('Enter a second question or a second command:')
		str8 = raw_input('Einen 3. Befehl oder eine 3. Frage eingeben:')
		str9 = raw_input('Enter a third question or a third command:')
		str2 = raw_input('Aussage oder Antwort eingeben:')
		str4 = raw_input('Enter a statement or answer:')
		plugin = (start + dreiarg + end).replace('AAA',str1).replace('BBB',str2).replace('CCC',str5).replace('EEE',str8).replace('aaa',str3).replace('bbb',str4).replace('ccc',str7).replace('eee',str9).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))
	else:
		str1 = raw_input('Einen Befehl oder eine Frage eingeben:')
		str3 = raw_input('Enter a question or a command:')
		str5 = raw_input('Einen 2. Befehl oder eine 2. Frage eingeben:')
		str7 = raw_input('Enter a second question or a second command:')
		str2 = raw_input('Aussage oder Antwort eingeben:')
		str4 = raw_input('Enter a statement or answer:')
		plugin = (start + zweiarg + end).replace('AAA',str1).replace('BBB',str2).replace('CCC',str5).replace('aaa',str3).replace('bbb',str4).replace('ccc',str7).replace('ZEIT',time.strftime('%d.%m.%Y %H:%M:%S'))

print ""
print ""
print time.strftime('%d.%m.%Y %H:%M:%S')
print "--------------------------------------------"
print "--------- neues Plugin erstellt ------------"
print "--------------------------------------------"
dateiname = "__init__.py"
server = "/SiriServerCore/"
pfad = "/SiriServerCore/plugins/" # anpassen!!! 
ordner = pfad + time.strftime('%Y%m%d%H%M%S')
os.mkdir(ordner)
verzeichnis = ordner + dateiname
f = file(ordner + '/__init__.py', 'w')
f.write(plugin)
f = file('__init__.py')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line,
f.close()

print "--------------------------------------------"
print ""
print 'Erfolgreich den Befehl "{0}" und'.format(str1)		
print 'die Antwort "{0}" hinzugefügt!'.format(str2)				
print ""
print "--------------------------------------------"
print ""
print "Das neue Plugin wurde gespeichert unter:"
print ""
print ordner
print ""
print "--------------------------------------------"
