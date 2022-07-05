import os
import platform

global listOfStudent 
listOfStudent = ["Ashly", "Ochwada", "Noellah", "Siara"] 

def manageStudents(): 

	x = "#" * 30
	y = "=" * 28
	global bye
	bye = "\n {}\n# {} #\n#  #\n# {} #\n {}".format(x, y, y, x)

	
	print(""" 

  ------------------------------------------------------
 |======================================================| 
 |======== Welcome To Student Management System	========|
 |======================================================|
  ------------------------------------------------------

Enter 1 : To View all Students
Enter 2 : To Add A New Student 
Enter 3 : To Search For A Student 
Enter 4 : To Remove A Student 
		
		""")

	try: # Exceptions For Validation
		userInput = int(input("Please Select An Option From Above: ")) 
	except ValueError:
		exit("\nHello! That's Not A Number") 
	else:
		print("\n") 

		
	if(userInput == 1): 
		print("List Students\n")  
		for students in listOfStudent:
			print("=> {}".format(students))

	elif(userInput == 2): 
		newStd = input("Enter A New Student: ")
		if(newStd in listOfStudent): #This Condition Checking The New Student Is Already In List Ur Not
			print("\nThis Student {} Already In The Database".format(newStd))  #Error Message
		else:	
			listOfStudent.append(newStd)
			print("\n=> New Student {} Successfully Added \n".format(newStd))
			for students in listOfStudent:
				print("=> {}".format(students))	

	elif(userInput == 3): 
		srcStd = input("Enter A Student's Name To Search: ")
		if(srcStd in listOfStudent):
			print("\n=> Record Found Of The Student {}".format(srcStd))
		else:
			print("\n=> No Record Found Of The Student {}".format(srcStd)) 

	elif(userInput == 4): 
		removeStd = input("Enter Student Name To Remove: ")
		if(removeStd in listOfStudent):
			listOfStudent.remove(removeStd)
			print("\n=> Student {} Successfully Deleted \n".format(removeStd))
			for students in listOfStudent:
				print("=> {}".format(students))
		else:
			print("\n=> No Record Found of This Student {}".format(removeStd)) #Error Message
	 
	elif(userInput < 1 or userInput > 4): 
		print("Please Enter Valid Option")	
						

manageStudents()

def tryingAgain(): 
	continueAgain = input("\n want To Try Again Y/n: ")
	if(continueAgain.lower() == 'y'):
		if(platform.system() == "Windows"): #Checking User OS For Clearing The Screen
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		manageStudents()
		# continueAgain()
	else:
		quit(bye) #Print GoodBye Message And Exit The Program

tryingAgain()		

