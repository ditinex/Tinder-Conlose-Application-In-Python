# Change table names and column names accordingly
# My tables are `users` and `proposal` with column `proposal_id`,`romeo_id` and `juliet_id`

import mysql.connector

class Tinder:
	current_user_id = '';
	def __init__(self):
		#Connect to the DB
		self.conn = mysql.connector.connect(host="localhost",user="root",password="",database="tinder")
		self.mycursor = self.conn.cursor()
		self.program_menu()

	def program_menu(self):
		program_input = input("""Hi What would you like to do ?
			1.	Enter 1 to Create an account
			2.	Enter 2 to Login
			3.	Anything else to exit\n""")

		if program_input == '1':
			self.register()
		elif program_input == '2':
			self.login()
		else:
			print("Thank for using Tinder! Come back again.")


	def register(self):
		name = input('Name: ')
		email = input('Email: ')
		password = input('Password: ')
		age = input('Age: ')
		gender = input('Gender: ')
		city = input('City: ')
		error = 0;
		#FIX issue 1. Duplicate Registration
		self.mycursor.execute("""SELECT `user_id` FROM `users` WHERE `email`='{}'""".format(email))
		checking_duplicat = self.mycursor.fetchall();
		if len(checking_duplicat) > 0:
			error = 'Email Id Already Exists !'
		#FIX validate email
		if '@' not in email:
			error = 'Invalid Email Id.'
		#FIX Password must be greater than 4 charecter
		if len(password) < 4:
			error = 'Password must be greater than 4 character.'

		if error == 0:
			self.mycursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`age`,`gender`,`city`,`password`) 
			VALUES (NULL,'{}','{}','{}','{}','{}','{}')""".format(name,email,age,gender,city,password))
			self.conn.commit()
			print("Registration Successfull !")
		else:
			print("Error : ",error)

		self.program_menu()

	def login(self):
		email = input('Email: ')
		password = input('Password: ')

		self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))

		user_list = self.mycursor.fetchall()

		counter = 0
		for i in user_list:
			counter+=1
			current_user = i
		if counter>0:
			self.current_user_id = current_user[0]
			print("Welcome ",current_user[1])
			self.user_menu()
		else:
			print("Incorrect")

	def user_menu(self):
		self.auth()
		user_input = input("""How would you like to proceed ?
			1.	View all users
			2.	View Proposals
			3.	View Request
			4.	View Matches
			5.	Anything else to logout\n""")
		if user_input == '1':
			self.view_users()
		elif user_input == '2':
			self.view_proposal()
		elif user_input=='3':
			self.view_requests()
		elif user_input=='4':
			self.view_matches()
		else:
			print("Logout")
			self.logout()

	def view_users(self):
		self.auth()
		#FIX ISSUE 2. Already proposed users will not be shown in the list
		self.mycursor.execute("""SELECT `user_id`,`name`,`gender`,`age`,`city` FROM `users` WHERE `user_id` NOT LIKE '{}' AND `user_id` NOT IN(SELECT `juliet_id` FROM `proposal` WHERE `romeo_id`='{}')""".format(self.current_user_id,self.current_user_id))
		all_users_list = self.mycursor.fetchall()
		for i in all_users_list:
			print('--------------------------------------------')
			print(i[1],i[2],i[3],i[4],sep=' | ')
			#NEW Propose or Pass style for each user
			yes_or_no = input("""Enter Choice :
				1 - Propose
				2 - Pass 
				3 - Menu \n""")
			if yes_or_no == '1':
				self.propose(self.current_user_id,i[0])
			elif yes_or_no == '3':
				break
		
		self.user_menu()

	def propose(self,romeo_id,juliet_id):
		self.mycursor.execute("""INSERT INTO `proposal` SET `romeo_id`='{}',`juliet_id`='{}'""".format(romeo_id,juliet_id))
		self.conn.commit()
		print("Proposed Successfully !")

	def view_proposal(self):
		self.auth()
		self.mycursor.execute("""SELECT u.`name`,u.`gender`,u.`city`,u.`age` FROM `proposal` p JOIN `users` u ON p.`juliet_id` = u.`user_id` WHERE p.`romeo_id` LIKE '{}'""".format(self.current_user_id))
		proposed_user_list = self.mycursor.fetchall()
		for i in proposed_user_list:
			print(i[0],i[1],i[2],i[3],sep=' | ')
			print("-----------------------------------------------")
		self.user_menu()

	def view_requests(self):
		self.auth()
		self.mycursor.execute("""SELECT u.`name`,u.`gender`,u.`city`,u.`age` FROM `proposal` p JOIN `users` u ON p.`romeo_id` = u.`user_id` WHERE p.`juliet_id` LIKE '{}'""".format(self.current_user_id))
		request_user_list = self.mycursor.fetchall()
		for i in request_user_list:
			print(i[0],i[1],i[2],i[3],sep=' | ')
			print("-----------------------------------------------")
		self.user_menu()

	def view_matches(self):
		self.auth()
		# tripple subquery
		self.mycursor.execute("""SELECT `name`,`gender`,`age`,`city` FROM `users` WHERE `user_id` IN (SELECT `juliet_id` FROM `proposal` WHERE `romeo_id` LIKE '{}' AND `juliet_id` IN (SELECT `romeo_id` FROM `proposal` WHERE `juliet_id` LIKE '{}'))""".format(self.current_user_id,self.current_user_id))
		matched_user = self.mycursor.fetchall()
		for i in matched_user:
			print(i[0],i[1],i[2],i[3],sep=' | ')
			print("-----------------------------------------------")
		self.user_menu()

	def auth(self):
		#FIX ISSUE 3. Authentication
		if self.current_user_id == '':
			print("Session Expired !")
			self.program_menu()

	def logout(self):
		#FIX ISSUE 4. Logout
		self.current_user_id=''
		self.program_menu()



ob = Tinder()
