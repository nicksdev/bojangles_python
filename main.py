# Main file
import json
import logging

logging.basicConfig(filename='info.log', filemode='w', level=logging.INFO)


temp_data = open('map.json')
mapdata = json.load(temp_data)
temp_data.close()

# room = mapdata['room1']
# print(room)
# print(room['name'])
# print(room.keys())
# print(room.values())
#
# print(type(mapdata))


print("Welcome to the land of Bojangles, what do you wish to do? \n")


#FUNCTION LIBRARY

def loadroom(room):
    roomdata = mapdata[room]
    #print('Loading Room: ' + roomdata['name'])
    logging.info('Loading Room: ' + roomdata['name'])
    print(roomdata['description'])
    print('You can see the following exits: ')
    print(' '.join(roomdata['exit']))
    print('What would you like to do now?')

#Initialise room1


location = 'room1'

loadroom(location)


u_input = input()
u_verb = u_input.split()[0]
u_action = u_input.split()[1:len(u_input.split())]

logging.info("Input Verb = " + u_verb)
logging.info("Actions = %s" % ' ' .join(map(str, u_action)))

if u_verb == "go":
    print("You go somewhere")
    roomdata = mapdata[location]
    #print(location)
    #print(u_action[0])
    print(roomdata['exit2'][u_action[0]])
    loadroom(roomdata['exit2'][u_action[0]])

else:
    print("I don't recognise that action")



