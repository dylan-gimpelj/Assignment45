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