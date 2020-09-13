#!/bin/python

# Just some examples from a course about Comprehensions
# Run each example as a separate file

## Example 1 ## 
###############
#Normal 
float_list = []
for i in range(100):
  float_list.append(i*100.0)

#Comprehesion
float_list = [i*100.0 for i in range(100)]

## Example 2 ##
###############
def big_process_incoming_data(data_list):
  temp = []
  for datum in data_list:
    temp.append(datum//2*67 -5)
  return temp

# Comprehension Version
def process_incoming_data(data_list):
  return [datum//2*67 -5 for datum in data_list]

if __name__ == "__main__":
  data_list = [0, 5, 10 , 15]
  print (process_incoming_data(data_list) == big_process_incoming_data(data_list))

## Example 3 ## 
###############
float_dict = {}
for i in range (10):
  float_dict[i] = i * 100.0

#dictionary comprehension key:value

float_dict = {i:i*100.0 for i in range(10)}

def saturation_level(data_dict):
  temp = {}
  for key, value in data_dict.items():
    temp[key] = (value**3)/(2**value)
  return temp

def sat_level_comp(data_dict):
  return {k:v**3/2**v for k, v in data_dict.items()}

if __name__ == "__main__":
  hydration_levels = {"arc1": 23, "arc2": 64, "arc3": 104}
  print (saturation_level(hydration_levels) == sat_level_comp(hydration_levels))

## Example 4 ##
###############
#For Loop
float_list = []
for i in range (100):
  if i % 2 == 0:
    float_list.append(i*100.0)
  else:
    float_list.append(-1)
#Comprehension
float_list = [i*100 if i % 2 == 0 else -1 for i in range (100)]

#Snippet 
def find_usable_data(data_list):
  temp = []
  for datum in data_list:
    if datum > 90 and datum % 2 == 0:
	 temp.append(datum)
    else:
	 temp.append(-100)
  return temp

def find_usable_data_comp(data_list):
  return [datum if datum > 90 and datum % 2 == 0 else -100 for datum in data_list]

if __name__ == "__main__":
  num_list = [0,5,100,500,700]
  print(find_usable_data(num_list) == find_usable_data_comp(num_list))

## Example 5 ##
###############
#Loop Version
loat_list = []
for i in range(100):
  for j in range(10):
    float_list.append(i * j)

#Comprehesion Version
float_list = [i*j for i in range (100) for j in range (10)]

def calculator_value(data_list, divisors_list):
  temp = []
  for datum in data_list:
    for divisor in divisors_list:
	 temp.append(datum / divisor#!
  return temp

def cal_val(data_list, div_list):
  return [datum/divisor for datum in data_list for divisor in div_list]

if __name__ == "__main__":

  data = [10,20,30,40,50,60,70]
  divs = [5,10,11,12,10,15,3]

  print (calculator_value(data, divs) == cal_val(data, divs))

## Example 6 ##
###############
# Comphrenensions and Map Functions

numbers = [1.0, 2.0, 3.0, 4.0]

def my_operation(i):
    return i * 2

# Map Function
doubled_list = map(my_operation, numbers)
list(doubled_list)

# Returns an iterable map object:
# results = map(corrected_value, data_list) 
# For example <map object at 0x7ff9987783a0>

#List Comprehesion
doubled_list = [my_operation(i) for i in numbers]

def corrected_value(value):
    return value * 32

if __name__ == "__main__":
    data_list = [1,2,3]
    # For a Map
    old_results = map(corrected_value, data_list)
    #for i in results:
    #    print (i)
    # OR
    #print (list(results))
    results = [corrected_value(datum) for datum in data_list]
    print (list(old_results) == results)

## Example 7 ##
###############

from math import cos, radians

def cos_correction(value, angle):
    return value * cos(radians(angle))

def old_adjust_for_angle(data_list):
    temp = []
    for datum in data_list:
        for j in [0, 15, 30, 45, 60, 90]:
            temp.append(cos_correction(datum, j))
    return temp

def adjust_for_angle(data_list):
    return [cos_correction(datum, angle) for datum in data_list for angle in [0, 15, 30, 45, 60, 90]]

if __name__ == "__main__":
    my_list = [100, 500]
    print (old_adjust_for_angle(my_list))
    print (adjust_for_angle(my_list))
    print (old_adjust_for_angle(my_list) == adjust_for_angle(my_list))
