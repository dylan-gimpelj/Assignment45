#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi, cgitb, csv, webbrowser, urllib2

print "Content-Type: text/plain;charset=utf-8"
print
cgitb.enable() 

def addRow(item, price, quantity):
	amount = price*quantity 
	row = """<tr>
					<td>%s</td>
					<td>%s</td>
					<td>%s</td>
					<td>%s</td>
			</tr>""" %(item, price, quantity, amount)
	return row 
nestpr=5
buildingpr=10
ballotspr=2
nestq=1
buildingq=1
ballotsq=1000
form = cgi.FieldStorage()
namenaked = form.getvalue('user')
name = "['" + form.getvalue('user') + "']"

with open('LoggedIn.csv', 'r') as names:
	compare = csv.reader(names)
	rows = list(compare) 
	rows1 = []
	for row in rows:
		member = str(row)
		rows1.append(member)
	if name in rows1:
		buildingamount = form.getvalue('build')
		nestamount = form.getvalue('thenest')
		ballotsamount = form.getvalue('ballot')
		buildingamount = int(buildingamount)
		nestamount = int(nestamount)
		ballotsamount = int(ballotsamount)
		check = form.getlist('checkbox')
		print check 
		addnest=""
		addbuilding=""
		addballots=""
		nestcst=0
		ballotcst=0
		buildingcst=0
		htmlhead = "INVOICE for " + namenaked + ":"
		print htmlhead
		html = """<html>
		<table>
			<th>
				<td>Item</td>
				<td>Price</td>
				<td>Quantity</td>
			</th>"""

		if "nest" in check:
			nestcst=nestpr*nestamount
			nestq = nestq-nestamount
			addnest = addRow("THE NEST CAFE", nestpr, nestq)
			html = html+addnest
			print html
			print addnest
		if "ballots" in check:
			ballotcst=ballotspr*ballotsamount
			ballotsq=ballotsq-ballotsamount
			addballots = addRow("GA BALLOTS", ballotspr, ballotsq)
			html = html+addballots
			print html
			print addballots
		if "building" in check:
			buildingcst=buildingpr*buildingamount
			buildingq=buildingq-buildingamount 
			addbuilding = addRow("SSMU BROWN BUILIDNG", buildingpr, buildingq)
			html=html+addbuilding
			print html  
			print addbuilding
		with open('inventory.csv', 'wb') as invfile:
			reader = csv.writer(invfile, delimiter=',')
			reader.writerow(['nest', nestpr, nestq])
			reader.writerow(['building', buildingpr, buildingq])
			reader.writerow(['ballots', ballotspr, ballotsq])
		subtotal = buildingcst+ballotcst+nestcst
		print subtotal
		tax = subtotal * .13
		print tax
		total = subtotal+tax
		print total
		htmlsubtotal= """ <tr>
		<td>subtotal</td>
		<td></td>
		<td></td>
		<td>%s</td> </tr>"""%(subtotal)
		htmltax = """<tr>
		<td>tax</td>
		<td></td>
		<td></td>
		<td>%s</td> </tr>"""%(tax)
		htmltotal = """<tr>
		<td>total</td>
		<td></td>
		<td></td>
		<td>%s</td> </tr>"""%(total)
		html = html+htmltax
		html = html+htmlsubtotal
		html=html+htmltotal
		htmlend = """</table> """
		html=html+htmlend
		linkhome = """<body>
		<a href="http://cgi.cs.mcgill.ca/~dgimpe/">GO HOME</a>
		</body>"""
		html=html+linkhome
		htmlfinal = """</html>"""
		html=html+htmlfinal
		print html
		f = open('purchasepage.html', 'w')
		f.write(html)
		f.close()
		webbrowser.open(cgi.cs.mcgill.ca/~dgimpe/,new=0)
		print "Location: http://cgi.cs.mcgill.ca/~dgimpe/cgi-bin/purchasepage.html"
	else: 
		print "ARK! You need to be logged in to submit a purchase."


print "The end of the script!"

