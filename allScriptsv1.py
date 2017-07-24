#!C:\Python27\python.exe -u

import cgi
import glob
import os, sys
import re
import time
from datetime import datetime
import json

print 'Content-type: text/json; charset=utf-8\n\n'

form = cgi.FieldStorage()
tx = form["tx"].value

if (tx == "getNextNumber"):
	try:
		f1 = open("currentNumber.txt")
		nextNumber = eval(f1.read()) + 1
		f1.close()
		f2 = open("currentNumber.txt","w")
		f2.write(str(nextNumber))
		f2.close()
		print str(nextNumber)
	except:
		print '{ "outcome" : "error", "message" : "getNextNumber error" } '

if (tx == "getPHOv1"):
	try:
		patID = form["patID"].value
		print '{ "files": [ '
		files = os.listdir("json/photos")
		files = ['json/photos/'+elt for elt in files ]
		files.sort(key=os.path.getmtime)
		files.reverse()
		comma = False
		ctr = 0
		for filename in files:
		    if filename.split('_')[1] == patID:
		    	if comma:
		    		print ','
		    	print '{ "code" : "%s" '%filename.split('_')[1]
		    	print ', "file" : "%s" '%filename.split('.')[0].split('/')[2]
 		   	mdate = os.path.getmtime(filename)
 		   	print ', "date" : "%s"'%time.strftime("%Y-%m-%d", time.localtime(mdate))
 		   	print ', "time" : "%s"'%time.strftime("%H:%M", time.localtime(mdate))
 		   	print " } "
 		   	comma = True
 		   	ctr = ctr + 1   
		print '], "count" : '+str(ctr)+' }'
	except:
		print '{ "outcome" : "error", "message" : "getPHOv1 error" } '

if (tx == "uploadPhoto3"):
	try:
		patID = form['patID'].value
		fileitem = form['file'].value
		fn = "F_"+patID+"_"+str(int(round(time.time() * 1000)))
		fh = open('json/photos/' + fn + ".jpg", "wb")
		fh.write(fileitem.split(',')[1].decode('base64'))
		fh.close()
		print '{ "outcome" : "success", "message" : "file uploaded" } '
	except:
		print '{ "outcome" : "error", "message" : "uploadPhoto3 error" } '

if (tx == "getLABOSv1"):
	try:
		clinID = form["clinID"].value
		print '{ "labos": [ '
		files = os.listdir("json/labos")
		files = ['json/labos/'+elt for elt in files ]
		comma = False
		ctr = 0
		for filename in files:
		    if comma:
		    	print ','
		    print '{ "code" : "%s" '%filename.split('_')[1]
		    print ', "file" : "%s" '%filename.split('.')[0].split('/')[2]		    
		    json_data = open(filename, 'r')
		    data = json.load(json_data)
		    print ', "num" : "%s" '%data["num"].encode('utf-8')
		    print ', "nompre" : "%s" '%data["nompre"].encode('utf-8')
		    print ', "labo" : "%s" '%data["labo"].encode('utf-8')
		    print ', "envoye" : "%s" '%data["envoye"].encode('utf-8')
		    print ', "retour" : "%s" '%data["retour"].encode('utf-8')
		    print ', "rdv" : "%s" '%data["rdv"].encode('utf-8')
		    print ', "note" : "%s" '%data["note"].encode('utf-8')
		    print ', "recu" : "%s" '%data["recu"].encode('utf-8')
		    json_data.close()    
		    mdate = os.path.getmtime(filename)
		    print ', "date" : "%s"'%time.strftime("%Y-%m-%d", time.localtime(mdate))
		    print ', "time" : "%s"'%time.strftime("%H:%M", time.localtime(mdate))
		    print " } "
		    comma = True
		    ctr = ctr + 1    
		print '], "count" : '+str(ctr)+' }'
	except:
		print '{ "outcome" : "error", "message" : "getLABOSv1 error" } '

if (tx == "getPATv1"):
	try:
		clinID = form["clinID"].value
		print '{ "patients": [ '
		files = os.listdir("json/patients")
		files = ['json/patients/'+elt for elt in files ]
		comma = False
		ctr = 0
		for filename in files:
		    if comma:
		    	print ','
		    print '{ "code" : "%s" '%filename.split('_')[1]
		    print ', "file" : "%s" '%filename.split('.')[0].split('/')[2]		    
		    json_data = open(filename, 'r')
		    data = json.load(json_data)
		    print ', "id" : "%s" '%data["id"].encode('utf-8')
		    print ', "first" : "%s" '%data["first"].encode('utf-8')
		    print ', "last" : "%s" '%data["last"].encode('utf-8')
		    print ', "NAM" : "%s" '%data["NAM"]
		    print ', "birth" : "%s" '%data["birth"]
		    if 'alert' in data:
		    	print ', "alert" : "%s" '%data["alert"].encode('utf-8')
		    else:
		    	print ', "alert" : "" '
		    if 'alertD' in data:
		    	print ', "alertD" : "%s" '%data["alertD"].encode('utf-8')
		    else:
		    	print ', "alertD" : "" '
		    if 'suivi' in data:
		    	print ', "suivi" : "%s" '%data["suivi"].encode('utf-8')
		    else:
		    	print ', "suivi" : "" '
		    if 'suiviD' in data:
		    	print ', "suiviD" : "%s" '%data["suiviD"].encode('utf-8')
		    else:
		    	print ', "suiviD" : "" '
		    if 'labo' in data:
		    	print ', "labo" : "%s" '%data["labo"].encode('utf-8')
		    else:
		    	print ', "labo" : "" '
		    if 'laboD' in data:
		    	print ', "laboD" : "%s" '%data["laboD"].encode('utf-8')
		    else:
		    	print ', "laboD" : "" '
		    json_data.close()    
		    mdate = os.path.getmtime(filename)
		    print ', "date" : "%s"'%time.strftime("%Y-%m-%d", time.localtime(mdate))
		    print ', "time" : "%s"'%time.strftime("%H:%M", time.localtime(mdate))
		    print " } "
		    comma = True
		    ctr = ctr + 1    
		print '], "count" : '+str(ctr)+' }'
	except:
		print '{ "outcome" : "error", "message" : "getPATv1 error" } '

if (tx == "getANTv1"):
	try:
		patID = form["patID"].value
		print '{ "files": [ '
		files = os.listdir("json/antecedents")
		files = ['json/antecedents/'+elt for elt in files ]
		files.sort(key=os.path.getmtime)
		files.reverse()
		comma = False
		ctr = 0
		for filename in files:
		    if filename.split('_')[1] == patID:
		    	if comma:
		    		print ','
		    	print '{ "code" : "%s" '%filename.split('_')[1]
		    	print ', "file" : "%s" '%filename.split('.')[0].split('/')[2]    
		    	json_data = open(filename, 'r')
		    	data = json.load(json_data)
		    	print ', "client" : "%s" '%data["qHeader"]["qClient"].encode('utf-8')
		    	print ', "first" : "%s" '%data["qHeader"]["qFirst"].encode('utf-8')
		    	print ', "last" : "%s" '%data["qHeader"]["qLast"].encode('utf-8')
		    	print ', "prot" : "%s" '%data["qHeader"]["firstJSON"]
		    	print ', "treated" : "%s" '%data["qHeader"]["qTreated"]
		    	json_data.close()    
		    	mdate = os.path.getmtime(filename)
		    	print ', "date" : "%s"'%time.strftime("%Y-%m-%d", time.localtime(mdate))
		    	print ', "time" : "%s"'%time.strftime("%H:%M", time.localtime(mdate))
		    	print " } "
		    	comma = True
		    	ctr = ctr + 1    
		print '], "count" : '+str(ctr)+' }'
	except:
		print '{ "outcome" : "error", "message" : "getANTv1 error" } '

if (tx == "getALLsub"):
	try:
		subFolder = form['sub'].value
		patID = form["patID"].value
		print '{ "files": [ '
		files = os.listdir('json/'+subFolder)
		files = ['json/'+subFolder+'/'+elt for elt in files ]
		flist = [ ]
		for filename in files:
		    if filename.split('_')[1] == patID:    
		    	json_data = open(filename, 'r')
		    	data = json.load(json_data)
		    	json_data.close()
		    	try:
		    		aTime = data["time"]
		    	except:
		    		aTime = "00:00"    	
		    	flist.append((data["date"],aTime,filename.split('.')[0].split('/')[2]))
		slist = sorted(flist, key=lambda flist: (flist[0],flist[1],flist[2]), reverse=True)
		comma = False
		ctr = 0
		for atra in slist:
			if comma:
				print ','
			print '{ "date" : "%s" '%atra[0]
			print ', "time" : "%s" '%atra[1]
			print ', "file" : "%s" '%atra[2]
			print " } "
			comma = True
			ctr = ctr + 1    
		print '], "count" : '+str(ctr)+' }'
	except:
		print '{ "outcome" : "error", "message" : "getALLsub error" } '

if (tx == "getDOCv2"):
	try:
		patID = form["patID"].value
		print '{ "files": [ '
		files = os.listdir("json/documents")
		files = ['json/documents/'+elt for elt in files ]
		files.sort(key=os.path.getmtime)
		files.reverse()
		comma = False
		ctr = 0
		for filename in files:
		    if filename.split('_')[1] == patID:
		    	if comma:
		    		print ','
		    	print '{ "code" : "%s" '%filename.split('_')[1]
		    	print ', "file" : "%s" '%filename.split('.')[0].split('/')[2]
		    	mdate = os.path.getmtime(filename)
		    	print ', "date" : "%s"'%time.strftime("%Y-%m-%d", time.localtime(mdate))
		    	print ', "time" : "%s"'%time.strftime("%H:%M", time.localtime(mdate))
		    	print " } "
		    	comma = True
		    	ctr = ctr + 1    
		print '], "count" : '+str(ctr)+' }'
	except:
		print '{ "outcome" : "error", "message" : "getDOCv2 error" } '

if (tx == "getEXAv1"):
	try:
		patID = form["patID"].value
		print '{ "files": [ '
		files = os.listdir("json/examens")
		files = ['json/examens/'+elt for elt in files ]
		files.sort(key=os.path.getmtime)
		files.reverse()
		comma = False
		ctr = 0
		for filename in files:
		    if filename.split('_')[1] == patID:
		    	if comma:
		    		print ','
		    	print '{ "code" : "%s" '%filename.split('_')[1]
		    	print ', "file" : "%s" '%filename.split('.')[0].split('/')[2]
		    	json_data = open(filename, 'r')
		    	data = json.load(json_data)
		    	print ', "client" : "%s" '%data["qHeader"]["qClient"].encode('utf-8')
		    	print ', "first" : "%s" '%data["qHeader"]["qFirst"].encode('utf-8')
		    	print ', "last" : "%s" '%data["qHeader"]["qLast"].encode('utf-8')
		    	print ', "prot" : "%s" '%data["qHeader"]["firstJSON"]
		    	print ', "treated" : "%s" '%data["qHeader"]["qTreated"]
		    	json_data.close()
		    	mdate = os.path.getmtime(filename)
		    	print ', "date" : "%s"'%time.strftime("%Y-%m-%d", time.localtime(mdate))
		    	print ', "time" : "%s"'%time.strftime("%H:%M", time.localtime(mdate))
		    	print " } "
		    	comma = True
		    	ctr = ctr + 1    
		print '], "count" : '+str(ctr)+' }'
	except:
		print '{ "outcome" : "error", "message" : "getEXAv1 error" } '

if (tx == "getFile"):
	try:
		pKey = form["pKey"].value
		prot = form["prot"].value
		extID = form["extID"].value
		lang = form["lang"].value
		file = open("protCohort/"+extID+".json")
		data = file.read()
		print data
		file.close()
	except:
		print '{ "outcome" : "error", "message" : "getFile error" } '

if (tx == "getJSONsub"):
	try:
		subFolder = form["sub"].value
		qCode = form["code"].value
		file = open("json/"+subFolder+"/"+qCode+".json")
		data = file.read()
		print data
		file.close()
	except:
		print '{ "outcome" : "error", "message" : "getJSONsub error" } '

if (tx == "uploadJSONP"):
	try:
		fName = form['name'].value
		subName = form['sub'].value
		jsonString = form['json'].value
		logFile = open('json/'+subName+'/'+fName+'.json', 'w')
		logFile.write(jsonString)
		logFile.close()
		print '{ "outcome" : "success", "message" : "file uploaded" } '
	except:
		print '{ "outcome" : "error", "message" : "uploadJSONP error" } '

if (tx == "uploadJSONsub"):
	try:
		subFolder = form['sub'].value
		fName = form['name'].value
		jsonString = form['json'].value
		logFile = open("json/"+subFolder+"/"+fName+'.json', 'w')
		logFile.write(jsonString)
		logFile.close()
		print '{ "outcome" : "success", "message" : "file uploaded" } '
	except:
		print '{ "outcome" : "error", "message" : "uploadJSONsub error" } '

if (tx == "uploadDOC"):
	#try:
	import msvcrt
	msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
	msvcrt.setmode (1, os.O_BINARY) # stdout = 1
	fileitem = form['file']
	patID = form["dPatID"].value
	fn = "D_"+patID+"_"+str(int(round(time.time() * 1000)))
	if fileitem.filename:
		open('json/documents/' + fn + ".pdf", 'wb').write(fileitem.file.read())
	#fh = open('json/documents/' + fn + ".pdf", "wb").write(fileitem.read())
	#fh.close()
	print '{ "outcome" : "success", "message" : "file uploaded" } '
	#except:
	#	print '{ "outcome" : "error", "message" : "uploadDOC error" } '