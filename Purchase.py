"""verify if user logged in"""
if hidden empty {
		display ErrorPage.html //how to do this?
}
else(traverse loggedin.csv){
	with open('loggedin.csv', 'rb') as usersfile:
		compare = csv.reader(usersfile)
			for row in compare
				if(hidden.value==row)
					"""Step 2"""
				else
					"""Continue"""
}

"""Step 2""" //should be separate def function so we can include it in the for loop 
def step2():
	