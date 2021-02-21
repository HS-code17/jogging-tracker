#!/usr/bin/env python3
from datetime import datetime
import csv
#from matplotlib import pyplot as plt
#from pygeocoder import Geocoder
#import numpy as np
#import math

class Run:
	def __init__(self, time, distance, pace,time_taken, max):
		self.time= time
		self.distance = distance
		self.pace = pace
		self.time_taken = time_taken
		self.start_locations = ['mhata', 'zaytuna bay', 'location3']
		self.end_locations = ['mhata', 'zaytuna bay', 'location3']
	def get_time(self):
		self.time = input("Enter your time: ")
		if self.valid_number(self.time) and (int(self.time) <=60):
			return float(self.time)
		else:
			print("Please enter a valid time: ")
			return self.get_time()

	def get_int_input(self,msg: str, valid_inputs: list[int]):
		"""
		It asks the user for an integer input, and only returns if it matches the
		valid_inputs list
		"""
		while True:
		    try:
		        choice = int(input(msg))

		        if choice in valid_inputs:
		            return choice

		        print("Error: the value has to be from the given choices")

		    except ValueError:
		        print("Error: the input has to be an integer")


	def get_location(self):
		"""
		 asks the user for starting and ending points
		 calculates distance
		 #TODO 
		 Yet in this scenario we have locations stored in a database and need to add latitude and longitude to them. We’ll use a python script to interact with the database. 
		 Then it will communicate with the geocoding api to populate those coordinate fields.
		"""
		# the problem is that I need to convert locations to actual distance
		# from mhata to zaytuna bay ~= 7km
		# from zaytuna bay to mhata ~= 7km

		print("1.Choose from list")
		print("2.Input your own")
		print("3.Mix and match from lists + your own input")

		l = []

		choice = self.get_int_input("choose from the list above: ", list(range(1,4)))

		if choice == 1: # choosing from the list
			print(f"you chose number {choice}")

			for i, loc in enumerate(self.start_locations):
				print(f'{i}: {loc}')

			valid_inputs = list(range(len(self.start_locations)))

			start= self.get_int_input("choose starting point", valid_inputs)
			end = self.get_int_input("choose end point", valid_inputs)
			# TODO: add google distance calculator based on location
			# business_name = 'Zaytuna Bay'
			# print(f'Searching {business_name}')
			# results = Geocoder.geocode(business_name)
			# for result in results:
			#     print (result)
			distance = self.get_distance()
			print(f'the run is from {self.start_locations[start]} to {self.start_locations[end]} and that covered {distance}km')

		elif choice == 2: 
			print(f"you chose number {choice}")
			start = input("Enter starting location: ")
			end = input("Enter ending location: ")
			l.extend([start,end])
			print(l)

		# TODO:
		# create another function to validate distance.
		# self.distance = input("Enter your distance")
		# if self.valid_number(self.distance):
		# 	return float(self.distance)
		# else:
		# 	print("Please enter a valid distance: ")
		# 	return self.get_distance()
	def get_distance(self):
		# TODO
		# if location chosen from one area to another get it's distance
		# also input distance
		self.distance = int(input("Enter the distance covered: "))
		if self.valid_number(self.distance):
			return float(self.distance)
		else:
			return self.get_distance()
	def get_time_taken(self):
		self.time_taken = input("Enter what time you ran am/pm: ")
		# fix this conditional statement
		if self.valid_number(self.time_taken):
			return float(self.time_taken)
		else:
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
		# while True:
		# TODO add a way to create new row content based on user permission
		while True:
			l =[]
			ans = input("Write a new row ?(y/n) ")
			if ans=='y':
				# TODO entering a new field means you need to enter a new row which usually means
				# entering a new variable to get_rows
				new_field = self.get_fields()
				row_contents= self.get_rows()
				with open(filename+'.csv', 'a', newline='') as csvfile:
					filewriter = csv.writer(csvfile)
					filewriter.writerow(['Time/min', 'Distance/miles','Time_Taken','Pace',new_field])
					filewriter.writerows([row_contents])
			elif ans =='n':
				break
			# return new row_content after every succesful loop
		
		# for i in range(5):
		# 	row_contents_[i] = self.get_rows()
		# How to add a field


		# write to csv
		# with open(filename+'.csv', 'w', newline='') as csvfile:
		# 	filewriter = csv.writer(csvfile)
		# 	filewriter.writerow(['Time/min', 'Distance/miles','Time_Taken','Pace'])
		# 	# row_contents= self.get_rows()
		# 	# filewriter.writerows([row_contents])
		# 	filewriter.writerows([row_contents_1, row_contents_2])

			# TODO:
			# add a field for future notes
			# also add a list of the common distances to choose from
			# add a list of options
			# that is a list of distances you would have
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

	def get_fields(self):
		while True:
			ans = input("Add a new field ?(y/n) ")
			if ans == 'y':
				new_field = input("Add field: ")
				return new_field
			else:
				break
				# or pass
	def get_rows(self):
		# TODO: start fixing here.
		numbering = ['first','second', 'third', 'fourth', 'fifth']
		row_contents = []
		x_y_list = []
		# while len(row_contents) < len(numbering):
			# ans = input("Choose to continue adding or stop:(c for continue)")
			# if ans == 'c':
		time = self.get_time()
		distance = self.get_location()
		time_taken= self.get_time_taken()
		total_time = time
		total_distance = self.distance
		pace = total_time/total_distance
		# what is another approach to do this ? use a dictionary ?
		str_x = str(int(time))
		str_y = str(int(total_distance))
		str_z = str(int(time_taken))
		str_pace = str(int(pace))
		row_contents.extend([str_x, str_y, str_z, pace])
		print(row_contents)
				# TODO: make this universal (add more "guards")
				# if I want to add more columns I need to change the value for i + range
				# row_contents=[x_y_list[i:i+4] for i in range(0,len(x_y_list),4)]
			# else:
			# 	print("autofill")
			# 	break

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




start = Run(17, 5, 2, 13,500)
start.main()
