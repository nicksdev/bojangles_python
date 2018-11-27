# Main file
import json
import logging



logging.basicConfig(filename='info.log', filemode='w', level=logging.INFO)


json_data = open('map.json')
x = json.load(json_data)
json_data.close()
print(x)
print(type(x))




print("Welcome to the land of Bojangles, what do you wish to do? \n")

u_input = input()
u_verb = u_input.split()[0]
u_action = u_input.split()[1:len(u_input.split())]



logging.info("Input Verb = " + u_verb)
logging.info("Input Actions = ")
logging.info(u_action)


# print("Input Verb = " + u_verb)
# print("Input Actions = ")
# print(u_action)
