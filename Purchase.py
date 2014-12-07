<<<<<<< HEAD
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import cgi, cgitb, csv 

print "Content-Type: text/html;charset=utf-8"
print
cgitb.enable() 

def addRow(item, price, quantity):
	amount = price*quantity 
	row = """<tr>
					<td>%s</td>
					<td>%s</td>
					<td>%s</td>
					<td>%s</td>
			</tr>"""%(item, price, quantity, amount)
	return row 

nestpr=300000
buildingpr=4100000
ballotspr=0.05
nestq=1
buildingq=1
ballotsq=10000
form = cgi.FieldStorage() 
namenaked = form.getvalue('user') 
namestr = str(namenaked)
name = "'" + namestr + "'" 
print namenaked, namestr, name 
with open('LoggedIn.csv', 'r') as names:
	compare = csv.reader(names, delimiter=",")
	rows = list(compare) 
	print rows
	rows1 = []
	print any(namestr in row for row in rows1)
	print any(name in row for row in rows1)
	if(any(namestr in row for row in rows1) or any(name in row for row in rows1)):
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
		html = """<html>
		<center>
		<style type="text/css" >
		body
		{
		background:url(../image/white-blanket-647343.jpeg) no-repeat center;
		}
		</style>
		<img src="../image/bleeding_martletcircle.png" alt="Logo" style="width:304px;height:228px">
<br> <br>

<table align="center" cellspacing="40">	
<center>	
     <tr id="menu">
 	<td><a href="../home_page.html">     <IMG SRC="../image/Home_page.png" alt="Homepage">      </a></td>
	<td><a href="../catalogue.html">      <IMG SRC="../image/Catalouge.png" alt="Catalogue">                </a></td>
	<td><a href="../login.html" target="_blank">       <IMG SRC="../image/login.png" alt="Login">                  </a>  </td>
   </tr>
</table>
</center>
<br> <center> INVOICE for: """ 
		html = html+namenaked 
		htmlextra = """ <table border="1"><th>
				<td>Price ($)</td>
				<td>Quantity</td>
				<td>Cost ($)</td>
			</th>"""
		html=html+htmlextra
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
		with open('inventory.csv', 'wb') as invfile:
			reader = csv.writer(invfile, delimiter=',')
			reader.writerow(['nest', nestq, nestpr])
			reader.writerow(['building',  buildingq, buildingpr])
			reader.writerow(['ballots', ballotsq, ballotspr])
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
		<a href="http://cgi.cs.mcgill.ca/~ytaher1/home_page.html">Return to where the heart is</a><br>
		<a href="http://cgi.cs.mcgill.ca/~ytaher1/catalogue.html">Buy more stuff</a>
		</body></center>"""
		html=html+links
		htmlfinal = """</html>"""
		html=html+htmlfinal
		print html

	else: 	
		notlogged = """<html> <header><h1>ERROR 2342384-3453143143143143143143143143141212121212199</h1></header> \
		<body> 
		  <p> We're sorry, you  are currently not logged in. Please select one of the following options:			<ul>
		<li><a href="http://cgi.cs.mcgill.ca/~ytaher1/login.html">Login</a></li>
		<li><a href="http://cgi.cs.mcgill.ca/~ytaher1/register_test.html">Register</a</li>
		<li><a href="http://cgi.cs.mcgill.ca/~ytaher1/catalogue.html">Return to Catalogue</a></li>
			</ul>	    	
		</p>
		</html>"""
		print notlogged






=======
"""verify if user logged in"""
#!/usr/bin/env python
print("Content-Type: text/html")
print()
import cgi, cgitb, os, urllib
from HTML Parser import HTMLParser """use this to read through html text, don't think it's necessary though if we just take the form data"""

"""create instance of FieldStorage"""
form = cgi.FieldStorage()
value = form.getlist("checkbox") """for some reason traverse over checkboxes to see which ones we operate on?"""
username = form.get(hidden,'empty')

if username='empty' {
	f = open('ErrorPage.html', 'w')
	message = """<html>

	<body>

	<h1>ERROR 134</h1>

	<p>We're sorry, you  are currently not logged in. Please select one of the following options:</p>
	<p>
		<ul>
			<li><a href="loginpage.com">Login</a></li>
			<li><a href="Registerpage.com">Register</a</li>
			<li><a href="Cataloguepage.com">Return to Catalogue</a></li>

		</ul>	
    
	</p> 

	</body>
	</html>"""
	f.write(message)
	f.close() 
	"""export the file f to the website"""
}
"""otherwise can't I just assume the username is logged in?"""
else(traverse loggedin.csv){ //search for username, if match then let submit button be clickable, wait for input 
	try:
		f = open('loggedin.csv', 'rb') 
	except: 
		cgitb.handler() 
	with open('loggedin.csv', 'rb') as usersfile:
			compare = csv.reader(usersfile)
			for row in compare
				if(username==row)
					"""Let submit button be clickable"""
					calcInvoice(username)
					break
				else
					"""Continue, keep checking the excel file"""
}

"""Step 2""" //should be separate def function so we can include it in the for loop 
def calcInvoice(user u):
	//Invoice:
	items = form.getlist(item) """assume this is the list of items the person is buying"""
	"""checks = form.getlist(checkbox)"""
	invoicelist = []
	invitems = [] 
	with open('inventory.csv') as inv:
					invreader = csv.reader(inv, delimiter=',')
					for row in invreader
						newitemname = row[0]
						invitems.append(newitemname) 


	for item in items:
		if item in invitems 
			//check the the number of items requested is lesser than the number of this item in the inv.csv
			//else print("I'm sorry we don't have enough of one of the items you've requested, you'll have to resubmit the form") 
			invoicelist.append(invitem)
				
		for checkitem in checks
			make sure value of item<quantity from csv file
			add it's name to invoice name list, display P ^ Qin 2nd table column
			add it's value to total price, multiplied by quantit  
					After all items tabulated, subtract their values from the inventory csv
				
	calculate tax
	final value is total
	Links to home and catalogue pages at end of invoice 

"""use this to output tables to html from the script after processing
	ie final receipt! And the new inventory list?"""
def htmlTable(table):
	print '<table>'
  	for sublist in table:
    print '  <tr><td>'
    print '    </td><td>'.join(sublist)
    print '  </td></tr>'
  print '</table>'

def row_major(alist, sublen):
	return [alist[i:i+sublen] for i in range(0, len(alist), sublen)]

def col_major(alist, sublen):
  numrows = (len(alist)+sublen-1) // sublen 
  return [alist[i::sublen] for i in range(numrows)]

//fieldstorage:
//form = cgi.FieldStorage() """note it's instatiatable only once"""
//to get items:
//items = form.getlist('item') 
//to operate on:
//for item in items:
	//Do something
>>>>>>> 0db8eb78a7e278364f91447c933f2f95f6b36c03
