#!/usr/bin/env python3
from datetime import datetime
import csv
from matplotlib import pyplot as plt
# import numpy as np
# import math

class RunHany:
	def __init__(self, time, distance, pace,time_taken, max):
		self.time= time
		self.distance = distance
		self.pace = pace
		self.time_taken = time_taken

	def get_time(self):
		self.time = input("Enter your time: ")
		if self.valid_number(self.time) and (int(self.time) <=60):
			return float(self.time)
		else:
			print("Please enter a valid time: ")
			return self.get_time()

	def get_distance(self):
		for i in range(10):
			r= f'option_{i}'
			print(r)
		list_of_options = ['mhata', 
		'zaytuna bay',
		'location3',
		]
		option_1 = ['1:mhata']
		option_2 = ['2:zaytuna bay']
		options = {'from':option_1,'to':option_2}
		choice = input("Choose from the three options.1. Choose what list. 2. Input your own list.3.Mix and match from lists + your own input.")
		if choice=='1':
			print('list_of_options')
		elif choice=='2':
			print('input your own list: so you will have a loop start+destination')
			self.distance = input("Enter your distance")
			if self.valid_number(self.distance):
				return float(self.distance)
			else:
				print("Please enter a valid distance: ")
				return self.get_distance()
		elif choice=='3':
			print('list_of_options + add yours')
		
		# maybe create another function to validate distance.
		# self.distance = input("Enter your distance")
		# if self.valid_number(self.distance):
		# 	return float(self.distance)
		# else:
		# 	print("Please enter a valid distance: ")
		# 	return self.get_distance()
	def get_time_taken(self):
		self.time_taken = input("Enter the current time am/pm: ")
		# fix this conditional statement
		if self.valid_number(self.time_taken):
			return float(self.time_taken)
		else:
			print("Please enter a valid time_taken: ")
			return self.get_time_taken()

	def pace_calculation(self):
		x = self.get_time()
		y = self.get_distance()
		total_time = x 
		total_distance = y
		pace = total_time/total_distance
		return pace
	def file_name(self):
		Time = datetime.now()
		Current_Time_min = Time.strftime("%M")
		Current_Time_hr = Time.strftime("%H")
		time_to_run = int(Current_Time_min) + 20
		filename_time = Current_Time_hr + ":" + str(time_to_run)

		Cu_DateTime = datetime.now()
		Date = Cu_DateTime.strftime("%Y-%m-%d")

		filename ="Date:"+str(Date)
		return filename

	def write_csv(self):
		# time for running 
		Time = datetime.now()
		Current_Time_min = Time.strftime("%M")
		Current_Time_hr = Time.strftime("%H")
		time_to_run = int(Current_Time_min) + 20
		filename_time = Current_Time_hr + ":" + str(time_to_run)
		# get file_name
		filename = self.file_name()
		# get rows
		row_contents = self.get_rows()
		# write to csv
		with open(filename+'.csv', 'w', newline='') as csvfile:
			filewriter = csv.writer(csvfile)
			# add a field for future notes
			# also add a list of the common distances to choose from
			# add a list of options
			# that is a list of distances you would have
			filewriter.writerow(['Time/min', 'Distance/miles','Time_Taken','Pace'])
			filewriter.writerows(row_contents)
			# else:
			# 	print("autofill")
				# # get rows
				# row_contents = self.get_rows()
				# # write to csv
				# with open(filename+'.csv', 'w', newline='') as csvfile:
				# 	filewriter = csv.writer(csvfile)
				# 	# add a field for future notes
				# 	# also add a list of the common distances to choose from
				# 	# add a list of options
				# 	# that is a list of distances you would have
				# 	filewriter.writerow(['Time/min', 'Distance/miles','Time_Taken','Pace'])
				# 	filewriter.writerows(row_contents)

	def get_rows(self):
		numbering = ['first','second', 'third', 'fourth', 'fifth']
		row_contents = []
		x_y_list = []
		while len(row_contents) < len(numbering):
			ans = input("Choose to continue adding or stop:(c for continue)")
			if ans == 'c':
				time = self.get_time()
				distance = self.get_distance()
				time_taken= self.get_time_taken()
				total_time = time
				total_distance = distance
				pace = total_time/total_distance
				# what is another approach to do this ? use a dictionary ?
				str_x = str(int(time))
				str_y = str(int(distance))
				str_z = str(int(time_taken))
				str_pace = str(int(pace))
				x_y_list.append([str_x, str_y, str_z, pace])
				# x_y_list.append(str_x)
				# x_y_list.append(str_y)
				# x_y_list.append(str_z)
				# x_y_list.append(pace)
				print(x_y_list)
				# if I want to add more columns I need to change the value for i + range
				row_contents=[x_y_list[i:i+4] for i in range(0,len(x_y_list),4)]
			else:
				print("autofill")
				break


		return row_contents

	# this is all wrong 
	def monthly_csv(self):
		# one file for the whole month
		filename = self.file_name()
		row_contents = self.write_csv()
		do_it = self.map_it()
		with open(filename+'.csv','r+')as file: 
			csvFile = csv.reader(file) 
			# here is the problem
			# you could use enumerate don't forget about that and also zip in a for loop
			for lines in csvFile: 
				with open('Monthly '+filename+'.csv','w')as csvfile:
					filewriter = csv.writer(csvfile)
					filewriter.writerow(['Time/min', 'Distance/miles','Month' ])
					filewriter.writerows(lines)

	def append_csv(self):
		filename = self.file_name()
		row_contents= self.get_rows()

		with open(filename+'.csv', 'a', newline='') as csvfile:
			filewriter = csv.writer(csvfile)
			filewriter.writerow(row_contents)


	# def map_it(self):
	# 	x = np.arange(0, math.pi*2, 0.05)
	# 	y = np.tan(x)

	# 	plt.plot(x,y)
	# 	plt.xlabel("angle")
	# 	plt.ylabel("Tan value")
	# 	plt.title('Tan wave')
	# 	return plt.show()

	def valid_number(self,str_number):
		try:
			number = int(str_number)
		except:
			return False

		return number
	def main(self):
		ans = input("Choose to write or append to a csv file:(w/a) ")
		if ans=='w':
			writing_csv = self.write_csv()
		elif ans=='a':
			appending_csv = self.append_csv()
		else:
			print("Nothing chosen!")




start = RunHany(17, 5, 2, 13,500)
start.main()
