import urllib2
from bs4 import BeautifulSoup
import csv
import urllib2
from bs4 import BeautifulSoup
import csv

# for terminal counting
a=0

# the id we need to start from
i = 67
while i < 149950:

	# the url i targeted data from + the id parameter stringfied
	url = 'http://www.example.com/any.php?id='+ str(i)


	# using urllib2 to get the html page
	try :
		page = urllib2.urlopen(url)

		# parse the html page to BeautifulSoup to work on it
		the_parser = BeautifulSoup(page, 'html.parser')

		# getting the targeted data inputs
		name = the_parser.find('input', {'id': 'Trainee_Name'}).get('value')

		

		telephone = the_parser.find('input', {'id': 'Trainee_Telephone'}).get('value')

		national_id = the_parser.find('input', {'id': 'Trainee_NationalID'}).get('value')

		email_address = the_parser.find('input', {'id': 'Trainee_Email'}).get('value')


		def mTest():
			mobile = the_parser.find('input', {'id': 'Trainee_Mobile'}).get('value')

			if  mobile[0] != "0":
				mobile = "+20" + mobile
				# return mobile
			else:
				mobile = "+2" + mobile
			

			if mobile[4] == "0" :
				#append  vodafone numbers to csv 
				with open('voda_data.csv', 'a') as csv_file:
					 writer = csv.writer(csv_file)
					 writer.writerow([i,name.encode('utf-8').strip(), mobile.encode('utf-8').strip(), telephone.encode('utf-8').strip(),national_id.encode('utf-8').strip(),email_address])

			if mobile[4] == "1" :
				#append etisalat numbers to csv 
				with open('etisalat_data.csv', 'a') as csv_file:
					 writer = csv.writer(csv_file)
					 writer.writerow([i,name.encode('utf-8').strip(), mobile.encode('utf-8').strip(), telephone.encode('utf-8').strip(),national_id.encode('utf-8').strip(),email_address])

			if mobile[4] == "2" :
				#append orange numbers to csv 
				with open('orange_data.csv', 'a') as csv_file:
					 writer = csv.writer(csv_file)
					 writer.writerow([i,name.encode('utf-8').strip(), mobile.encode('utf-8').strip(), telephone.encode('utf-8').strip(),national_id.encode('utf-8').strip(),email_address])

			if mobile[4] == "5" :
				#append we numbers to csv 
				with open('we_data.csv', 'a') as csv_file:
					 writer = csv.writer(csv_file)
					 writer.writerow([i,name.encode('utf-8').strip(), mobile.encode('utf-8').strip(), telephone.encode('utf-8').strip(),national_id.encode('utf-8').strip(),email_address])

			else :
				#append rest to csv 
				with open('other_data.csv', 'a') as csv_file:
					 writer = csv.writer(csv_file)
					 writer.writerow([i,name.encode('utf-8').strip(), mobile.encode('utf-8').strip(), telephone.encode('utf-8').strip(),national_id.encode('utf-8').strip(),email_address])	 
					 
			# return mobile
		mTest()
	# to move on if it found an error
 	except:
		i += 1
	# loop raising
	i += 1
	# the terminal counter
	a+=1

	# for terminal colors
	class bcolors:
	    OKBLUE = '\033[94m'
	    OKGREEN = '\033[92m'
	    FAIL = '\033[91m'
	    ENDC = '\033[0m'
	    BOLD = '\033[1m'
	# the view in terminal
	print bcolors.BOLD + bcolors.FAIL + "[+] "+ bcolors.OKBLUE + str(a) + bcolors.OKGREEN + " Success...!" + bcolors.ENDC
	# print name + ' + ' + mTest() + ' + ' + telephone + ' + ' + national_id + ' + ' + email_address 

# for terminal counting
a=0

# the id we need to start from
# i target this range of id's from 37 to 148800
i = 67
while i < 148800:


	# the url i targeted data from + the id parameter stringfied
	url = 'http://www.example.com/any.php?id='+ str(i)


	# using urllib2 to get the html page
	try :
		page = urllib2.urlopen(url)

		# parse the html page to BeautifulSoup to work on it
		the_parser = BeautifulSoup(page, 'html.parser')

		# html file has 5 inputs with the id's i selected
		# getting the targeted data inputs value
		name = the_parser.find('input', {'id': 'example_Name'}).get('value')

		mobile = the_parser.find('input', {'id': 'example_Mobile'}).get('value')

		telephone = the_parser.find('input', {'id': 'example_Telephone'}).get('value')

		national_id = the_parser.find('input', {'id': 'example_NationalID'}).get('value')

		email_address = the_parser.find('input', {'id': 'example_Email'}).get('value')


		#append  to csv 
		with open('data.csv', 'a') as csv_file:
		 writer = csv.writer(csv_file)
		 writer.writerow([i,name.encode('utf-8').strip(), mobile.encode('utf-8').strip(), telephone.encode('utf-8').strip(),national_id.encode('utf-8').strip(),email_address])

	# to move on if it found an error
 	except:
		i += 1
	# loop raising
	i += 1
	# the terminal counter
	a+=1

	# for terminal colors
	class bcolors:
	    OKBLUE = '\033[94m'
	    OKGREEN = '\033[92m'
	    FAIL = '\033[91m'
	    ENDC = '\033[0m'
	    BOLD = '\033[1m'
	# the view in terminal
	print bcolors.BOLD + bcolors.FAIL + "[+] "+ bcolors.OKBLUE + str(a) + bcolors.OKGREEN + " Success...!" + bcolors.ENDC

# print name + ' + ' + mobile + ' + ' + telephone + ' + ' + national_id + ' + ' + email_address 


