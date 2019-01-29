"""This is Calender"""

from time import sleep, strftime

user_name = raw_input("What Your Name: ")

calender = {}

def welcome():
  print "Welcome %s to our Calender." %user_name
  print "Calender Starting...."
  sleep(1)
  print "Today is        : " + strftime("%A %B %d, %Y")
  print "Current Time is : " + strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do..??"
  
def start_calender():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calender.keys()) < 1:
        print "Calender Empty"
      else:
        print calender
    elif user_choice == "U":
      date = raw_input ("What Date..?")
      update = raw_input ("Enter an Update: ")
      calender[date] = update
      print "Calender being updated..."
      sleep(1)
      print "Updating successfull.."
      print calender
    elif user_choice == "A":
      event = raw_input ("Enter an Event: ")
      date = raw_input ("Enter a Date with this following format (MM/DD/YYYY) : ")
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "Invalid Date..."
        try_again = raw_input("Try Again? Y for Yes, N for No")
        try_again = try_again.upper
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calender[date] = event
        print "Calender being added...."
        sleep(1)
        print "Adding Successfull.."
        print calender
    elif user_choice == "D":
      if len(calender.keys()) < 1:
        print "Calender Empty"
      else:
        event = raw_input ("What event you want to Delete..?? ")
        for date in calender.keys():
          if event == calender[date]:
            del calender[date]
            print "Event being deleted...."
            sleep(1)
            print "Deleting Successfull..."
          else:
            print "Incorrect Even.. "
    elif user_choice == "X":
      start = False
    else:
      print "Invalid.."
      start = False
      
start_calender()      
      
          
          
        
      
        
        
