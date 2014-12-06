#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi, cgitb, csv,

print "Content-Type: text/html;charset=utf-8"
print
cgitb.enable() 
#use this function to add a row of an item bought to the invoice, allows invoice to be a bit more dynamic
def addRow(item, price, quantity):
	amount = price*quantity 
	row = """<tr>
					<td>%s</td>
					<td>%s</td>
					<td>%s</td>
					<td>%s</td>
			</tr>""" %(item, price, quantity, amount)
	return row 
#I couldn't figure out how to store the quantities and prices together which would have made the code a bit prettier
#But basically we know the price and the initial quantity, we take the order from the user and adjust the quantity based on that in the updated Inventory.csv
#What I did was make an html sting that we add each item the user wishes to buy dynamically, then print it at the end in the form of a new webpage.
#There is an if/else that will print out a certain webpage depending on whether the user is logged in, whether the hidden field entry can be found in the LoggedIn.csv file
estpr=300000
buildingpr=4100000
ballotspr=0.05
nestq=1
buildingq=1
ballotsq=10000
form = cgi.FieldStorage() #get user input 
namenaked = form.getvalue('user') #to use at top of invoice
name = "['" + form.getvalue('user') + "']" #to use while traversing LoggedIn.csv
with open('LoggedIn.csv', 'r') as names:
	compare = csv.reader(names)
	rows = list(compare) 
	rows1 = []
	for row in rows: #need this extra step becaues can't compare csv object to name directly
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
		addnest=""
		addbuilding=""
		addballots=""
		nestcst=0
		ballotcst=0
		buildingcst=0
		htmlhead = "INVOICE for " + namenaked + ":"
		print htmlhead
		html = """<html>
		<table border="1">
			<th>
				<td>Price ($)</td>
				<td>Quantity</td>
				<td>Cost ($)</td>
			</th>"""

		if "nest" in check:
			nestcst=nestpr*nestamount
			nestq = nestq-nestamount
			addnest = addRow("THE NEST CAFE", nestpr, nestamount)
			html = html+addnest
		
		if "ballots" in check:
			ballotcst=ballotspr*ballotsamount
			ballotsq=ballotsq-ballotsamount
			addballots = addRow("GA BALLOTS", ballotspr, ballotsamount)
			html = html+addballots

		if "building" in check:
			buildingcst=buildingpr*buildingamount
			buildingq=buildingq-buildingamount 
			addbuilding = addRow("SSMU BROWN BUILIDNG", buildingpr, buildingamount)
			html=html+addbuilding
		#Here we subtract the purchased quantities from the inventory file. 
		with open('inventory.csv', 'wb') as invfile:
			reader = csv.writer(invfile, delimiter=',')
			reader.writerow(['nest', nestpr, nestq])
			reader.writerow(['building', buildingpr, buildingq])
			reader.writerow(['ballots', ballotspr, ballotsq])
		subtotal = buildingcst+ballotcst+nestcst
		tax = subtotal * .13
		total = subtotal+tax
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
		links = """<body>
		<a href="http://cgi.cs.mcgill.ca/~dgimpe/">Return to where the heart is</a><br>
		<a href="http://cgi.cs.mcgill.ca/~yashen/">Buy more stuff</a>
		</body>"""
		html=html+links
		htmlfinal = """</html>"""
		html=html+htmlfinal
		print html
	
	else: 
		
		notlogged = """<html> <header><h1>ERROR 2342384-3453143143143143143143143143141212121212199</h1></header> <p>
		We're sorry, you  are currently not logged in. Please select one of the following options:
		<ul>
		<li><a href="http://cgi.cs.mcgill.ca/~dgimpe/">Login</a></li>
		<li><a href="http://cgi.cs.mcgill.ca/~dgimpe/">Register</a</li>
		<li><a href="http://cgi.cs.mcgill.ca/~dgimpe/">Return to Catalogue</a></li>

		</ul>	
    
		</p>
		</html>"""
		print notlogged


print "The end of the script!"

