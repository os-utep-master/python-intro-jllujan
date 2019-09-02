#Jose Lujan
#ID: 80572649
#CS4375 lab 1
import re

#Open File
read_file = open("speech.txt", "r")

#Creates list
dict = {}
list = []

#Reads each line,counts each word and sorts the list in order
with open("speech.txt", 'r') as input_file:
	for line in input_file:
		words = filter(None, re.split("[.,'!?:;\- \n\"]+", line))
		for item in words:
			if item.lower() not in dict:
				dict[item.lower()] = 1
				list.append(item.lower())
			else:
				dict[item.lower()] += 1
list.sort()

#Creates file where the output will be saved
output_file = open("speech_output.txt", 'w')
for item in list:
	output_file.write(item + " " + str(dict[item]) + "\n")
output_file.close()