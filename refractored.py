#!/usr/bin/env python3
from datetime import datetime
import csv


class Run:
	def __init__(self, time, distance, pace,time_taken, max):
		self.time= time
		self.distance = distance
		self.pace = pace
		self.time_taken = time_taken
		self.locations = ['Central-Military-Club','Zaituna-Bay','Meito Cafe & Lounge']
		self.links = ['https://goo.gl/maps/2kjp9TVDrMhz3LD7A']
		self.coordinates = ["""33°54'11.0"N 35°29'56.5"E""" ]

	def get_time(self):
		self.time = input("Enter the time it took to finish the run: ")
		if self.valid_number(self.time) and (int(self.time) <=60):
			return float(self.time)
		else:
			print("Please enter a valid time: ")
			return self.get_time()
	def get_location(self):
		print("1.Choose from a list of locations.")
		print("2.Input your own location.")
		choice = self.get_int_input("choose from the list above: ", list(range(1,4)))
		list_locations = []
		if choice == 1: # choosing from the list
			print(f"you chose number {choice}")
			for i, loc in enumerate(self.locations):
				print(f'{i}: {loc}')
			valid_inputs = list(range(len(self.locations)))
			start= self.get_int_input("choose starting location: ", valid_inputs)
			end = self.get_int_input("choose ending location: ", valid_inputs)
			starting = self.locations[start]
			ending = self.locations[end]
			print(f'the run is from {starting} to {ending}')
			distances_covered= self.find_distance(starting,ending)
			print(f'The covered distance was: {distances_covered} km')
			return starting,ending,distances_covered
		if choice == 2: # entereing your own locations
			print(f"you chose number {choice}")
			# TODO: append list_locations based on what users enters and keep it this way
			# Change it inside code, change it inside of here
			start= input("enter starting location: ")
			end = input("enter ending location: ")
			print(f'the run is from {start} to {end}')
	def get_distance(self):

		self.distance = int(input("Enter the distance covered: "))
		if self.valid_number(self.distance):
			return float(self.distance)
		else:
			return self.get_distance()
	def jog_time(self):
		"""
		The time at which this jog was made.
		"""
		ans = input("Enter your own time or take current time?(own) ")
		if ans == 'own':
			self.time_taken = input("Enter what time you ran am/pm: ")
			# fix this conditional statement
			if self.valid_number(self.time_taken):
				return float(self.time_taken)
			else:
				return self.get_time_taken()
		else:
			pass
			# current_time = self.get_time
			# return current_time

	def find_distance(self,start,end):
		# TODO: JSON file for new locations
		distances_covered = {

				"Central-Military-Club_to_Zaituna-Bay":3.1,
				"b_to_c":6,
				"c_to_d":10

		}
		# look up the distance in the dict
		# Python dictionary method get() returns a value for the given key. If key is not available then returns default value None.
		my_distance = distances_covered.get(start + '_to_' + end)
		if my_distance is None:
		# that means it didn't find the distance in the dict
		# so we try to find the reverse
			my_distance = distances_covered.get(end + '_to_' + start)

		if my_distance:
		# if we found the reverse distance or the distance
			print(f"found distance : {start} -> {end} = {my_distance} km")
			return my_distance
		else:
		# if the distance is still none ..
		# that means the distance is not stored at all
			print("Error: couldn't find a stored distance!")
			return self.get_distance()

		# imagine if you have a 100 of distances
		# find a way to use the dictionary
	def get_rows(self):
		row_contents = []
		# this returns an int or a float
		time_covered = self.get_time()
		# this returns a string
		start,end,distances_covered = self.get_location()
		locations = start+ '->' + end
		# this returns a int/ float
		time_taken= self.jog_time()
		# first approach 
		row_contents.extend([time_covered, distances_covered,locations,time_taken, time_covered/distances_covered])
		return row_contents
	def get_fields(self):
		# TODO: add more "guards"
		fields_content = input("Add a new field or leave empty: ")
		return fields_content

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
		filename = self.file_name()
		while True:
			ans = input("Add data ?(y/n) ")
			if ans=='y':
				new_field = self.get_fields()
				row_contents= self.get_rows()
				with open(filename+'.csv', 'a', newline='') as csvfile:
					filewriter = csv.writer(csvfile)
					filewriter.writerow(['Time/min', 'Distance/km','Locations','Time_Taken','Pace',new_field])
					filewriter.writerows([row_contents])
			elif ans =='n':
				break
	def valid_number(self,str_number):
		try:
			number = int(str_number)
		except:
			return False
		return number
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
	def main(self):
		writing_csv = self.write_csv()


start = Run(17, 5, 2, 13,500)
start.main()		    


