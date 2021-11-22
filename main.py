from TrainDatabase import users
from TrainDatabase import buses
from TrainDatabase import colleges
from TrainDatabase import trains

import random
import time



buses = buses.bus_stops
colleges = colleges.collegetown_bus
trains = trains.destinations
final_price = ""
TRAIN_PER_MILE = .45
BUS_PER_MILE = 1.25
COLLEGE_PER_MILE = .25

train_help = "\n1. New York City, NY\n2. Washington, D.C.\n3. Philadelphia, PA\n4. Pittsburgh, PA\n5. Newark, NJ\n6. Boston, MA\n7. Richmond, VA\n8. Charlotte, NC\n9. Atlanta, GA\n10. Nashville TN\n"

bus_help = "\n1. Fells Point\n2. Towson Mall\n3. Downtown\n4. White Marsh Mall\n5. Good Samaritan Hospital\n6. Sinai Hospital\n7. M&T Bank Stadium\n8. Camden Yards\n9. Hopkins Hospital\n10. Mondawmin Mall\n"

college_help = "\n1. Morgan State University\n2. Towson University\n3. Johns Hopkins University\n4. Goucher College\n5. University of Maryland Baltimore County\n6. Baltimore City Community College\n7. Coppin State University\n8. University of Baltimore\n9. Loyola University of Maryland\n10. Maryland Institute College of Art\n"

#New User
def new_user():
  global final_price
  global train_help
  global bus_help
  global college_help

  new_user_id = random.randint(200000, 900000)
  name = input("Welcome to the Sharker Train System Kiosk Machine! What is your full name? ")
  newUser = users.User(name, new_user_id)
  newUser.createUser()
  time.sleep(1.5)
  print("\nHello", name, "you are now registered for the Sharker Train Software. You're user id is", newUser.id)
  time.sleep(2)



  print("\nThere are three services offered. The train service for long distance, the bus service for inner-Baltimore travel, and the Baltimore Collegetown Student Service.\n")
  time.sleep(3)
  service = int(input("Which service do you want to use? Type '1' for train service, '2' for Baltimore Bus service, or '3' for Baltimore Collegetown: "))

  if service == 1:
    print("\nCities you can travel to are:\n" + train_help)
    time.sleep(2)
    print("\n")
    destination = int(input("Enter the number of the city you want to travel to: (ex. '1' for New York City) "))

    distance = (trains[destination]['distance'])
    city = (trains[destination]['city'])
    print("\nYou are traveling to", city + ". The amount of miles to travel to", city, "are", distance, "miles.")
    time.sleep(2)
  
    if newUser.isEligibleForDiscount():
      final_price = (TRAIN_PER_MILE * distance) * .75
      print("\nYou qualified for a 25% discount!")
      time.sleep(2)
    else:
      final_price = TRAIN_PER_MILE * distance
      
  elif service == 2:
    print("\nBaltimore bus destinations available are:\n" + bus_help)
    time.sleep(3)
    print('\n')
    destination = int(input("Enter the number of the Baltimore destination you want to travel to: (ex. '1' for Fells Point) "))

    distance = (buses[destination]['distance'])
    bus_stop = (buses[destination]['destination'])
    print("\nYou are traveling to", bus_stop + ". The amount of miles to travel to", bus_stop, "are", distance, "miles.")
    time.sleep(2)

    if newUser.isEligibleForDiscount():
      final_price = (BUS_PER_MILE * distance) * .75
      print("\nYou qualified for a 25% discount!")
      time.sleep(2)
    else:
      final_price = BUS_PER_MILE * distance
  
  elif service == 3:
    print("\nBaltimore collegetown shuttle destinations available are:\n" + college_help)
    time.sleep(3)
    destination = int(input("Enter the number of the college you want to travel to: (ex. '1' for Morgan State University) "))

    distance = (colleges[destination]['distance'])
    college = (colleges[destination]['school'])
    print("\nYou are traveling to", college + ". The amount of miles to travel to", college, "are", distance, "miles.")
    time.sleep(2)
  
    if newUser.isEligibleForDiscount():
      final_price = (COLLEGE_PER_MILE * distance) * .75
      print("\nYou qualified for a 25% discount!")
      time.sleep(2)
    else:
      final_price = COLLEGE_PER_MILE * distance

  newUser.updateMiles(distance)
  print("\nAfter your trip, your total miles traveled will be", newUser.getMiles(), "miles.")
  time.sleep(2)
  print("\nThe final cost for your trip will be $" + str(final_price))
  time.sleep(1)
  

#Existing User
def existing_user():
  user_names = {}
  user_ids = {}
  trainusers = users.trainusers
  user_names = trainusers['name']
  user_ids = trainusers['id']
  user_miles = trainusers['Miles']
  name_list = list(user_names.values())
  id_list = list(user_ids.values())
  mile_list = list(user_miles.values())
  entryType = input("Do you want to sign in by your name or id?  Type 'name' or 'id': ")
  print("\n")
  
  if entryType.lower() == "name":
    userName = input("What is your name? ")
    print("\n")
    if userName in name_list:
      key = name_list.index(userName)
      time.sleep(1)
      print("Welcome back", userName + "!")
      print("\n")
      time.sleep(1)
      user = users.User(userName, id_list[key])
      user.Miles = mile_list[key]

    else:
      print("You are not found in the database, please create an account: ")
      new_user()
      return

  elif entryType.lower() == "id":
    userID = int(input("What is your ID?: "))
    if userID in id_list:
      key = id_list.index(userID)
      print("Welcome back", str(userID) + "!")
      print("\n")
      time.sleep(1)
      user = users.User(name_list[key], userID)
      user.Miles = mile_list[key]
      
    else:
      print("You are not found in the database, please create an account: ")
      new_user()
      return

  else:
    print("You have put in an incorrect entry.")
    return
  
  service = int(input("Which service do you want to use? Type '1' for train service, '2' for Baltimore Bus service, or '3' for Baltimore Collegetown: "))

  if service == 1:
    print("Cities you can travel to are:\n" + train_help)
    destination = int(input("Enter the number of the city you want to travel to: (ex. '1' for New York City) "))


    distance = (trains[destination]['distance'])
    city = (trains[destination]['city'])
    print("\nYou are traveling to", city + ". The amount of miles to travel to", city, "are", distance, "miles.")
    time.sleep(2)
  
    if user.isEligibleForDiscount():
      final_price = (TRAIN_PER_MILE * distance) * .75
      print("You qualified for a 25% discount!")
    else:
      final_price = TRAIN_PER_MILE * distance

  elif service == 2:
    print("Baltimore bus destinations available are:\n" + bus_help)
    destination = int(input("Enter the number of the Baltimore destination you want to travel to: (ex. '1' for Fells Point) "))

    distance = (buses[destination]['distance'])
    bus_stop = (buses[destination]['destination'])
    print("\nYou are traveling to", bus_stop + ". The amount of miles to travel to", bus_stop, "are", distance, "miles.")
    time.sleep(2)

    if user.isEligibleForDiscount():
      final_price = (BUS_PER_MILE * distance) * .75
      print("You qualified for a 25% discount!")
    else:
      final_price = BUS_PER_MILE * distance
  
  elif service == 3:
    print("Baltimore collegetown shuttle destinations available are:\n" + college_help)
    destination = int(input("Enter the number of the college you want to travel to: (ex. '1' for Morgan State University) "))

    distance = (colleges[destination]['distance'])
    college = (colleges[destination]['school'])
    print("\nYou are traveling to", college + ". The amount of miles to travel to", college, "are", distance, "miles.")
    time.sleep(2)
  
    if user.isEligibleForDiscount():
      final_price = (COLLEGE_PER_MILE * distance) * .75
      print("\nYou qualified for a 25% discount!")
    else:
      final_price = COLLEGE_PER_MILE * distance

  user.updateMiles(distance)
  print("\nAfter your trip, your total miles traveled will be", user.getMiles(), "miles.")
  time.sleep(2)
  print("\nThe final cost for your trip will be $" + str(final_price))

#Greet the user and ask if they are new or existing, if new direct them to the new function, if exisitng direct them to the existing function
userType = input("Hello! Are you a new user? Type y for yes or n for no: ")
print("\n")
if userType.lower() == "y":
  new_user()
elif userType.lower() == "n":
  existing_user()
else:
  print("You entered an invalid answer. Please type \"y\" for yes, or \"n\" for no.")
  userType = input("Hello! are you a new user? Type y for yes or n for no: ")
  if userType.lower() == "y":
    new_user()
  elif userType.lower() == "n":
    existing_user()
print("\nThank you for riding with the Sharker Train System! ")






