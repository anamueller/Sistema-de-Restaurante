username = input("Username:")#seven
password = input("Password:")#finalexam
import pprint
import csv

if username != 'seven' or password != 'finalexam':
  print("\nUsername or password invalid.\n")
if username == 'seven' and password == 'finalexam':
  print("\nType what you want to navigate through; meals, customers, orders, or if you want to edit the existing meals and customers type edit meal or edit customer(for you to edit the customer lsit or meals list you first need to add items to those lists):")
  option = input()
  if option == 'edit customer':
    editordel = ""
    reader = csv.reader(open('customer.csv', 'r'))
    dcustomer = {}
    dcustomer.clear()
    for row in reader:
      k, v = row
      dcustomer[k] = v
    while editordel != 'stop':
      print("\nDo you want to edit a customer or delete it? If you want to exit the program type stop.")
      editordel = input()
      if editordel == 'delete':
        pretty = pprint.PrettyPrinter(width=40)
        pretty.pprint(dcustomer)
        print("\nYou chose to delete a customer, type the customer's name: ")
        mname = str(input())
        print("\n", mname, "has been deleted from customers list.")
        dcustomer.pop(mname)
      if editordel == 'edit':
        pretty = pprint.PrettyPrinter(width=30)
        pretty.pprint(dcustomer)
        print("\nYou chose to edit a customer, type the customer's name: ")
        mname = str(input())
        print("\n", mname, "was chosen, type the new name:")
        newname = input()
        print("\nType the new adress:")
        newaddress = input()
        dcustomer.pop(mname)
        dcustomer[newname] = newaddress
        print(mname, "has been updated to", newname, newaddress)
    for keys in dcustomer:
      fileObj = open('customer.csv', 'w')
      name = keys
      address = dcustomer[keys]
      linha = "{},{}\n".format(name,address)
      fileObj.write(linha)
      fileObj.close()
  if option == 'edit meal':
    editordel = ""
    reader = csv.reader(open('meals.csv', 'r'))
    dmeals = {}
    dmeals.clear()
    for row in reader:
      k, v = row
      dmeals[k] = v
    while editordel != 'stop':
      print("\nDo you want to edit a meal or delete it? If you want to exit the program type stop.")
      editordel = input()
      if editordel == 'delete':
        pretty = pprint.PrettyPrinter(width=40)
        pretty.pprint(dmeals)
        print("\nYou chose to delete a meal, type the meal name: ")
        mname = str(input())
        print("\n", mname, "has been deleted from meals.")
        dmeals.pop(mname)
      if editordel == 'edit':
        pretty = pprint.PrettyPrinter(width=30)
        pretty.pprint(dmeals)
        print("\nYou chose to edit a meal, type the meal name: ")
        mname = str(input())
        print("\n", mname, "was chosen, type the new name:")
        newname = input()
        print("\nType the new price:")
        newprice = input()
        dmeals.pop(mname)
        dmeals[newname] = newprice + " euros"
        print(mname, "has been updated to", newname, newprice, "euros")
    for keys in dmeals:
      fileObj = open('meals.csv', 'w')
      name = keys
      price = dmeals[keys]
      linha = "{},{}\n".format(name,price)
      fileObj.write(linha)
      fileObj.close()
  if option == 'meals':
    class meals:
      def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    name = []
    choice = ""
    fileObj = open('meals.csv','a+')
    while choice != 'stop':
      print("\nType 'add' to add a new meal, 'list' to see all the meals, 'stop' to stop the program, or 'index' to find a specific meal:")
      choice = input()
      if choice == 'stop':
        print("\nOkay bye :)")
      if choice == 'list':
        fileObj = open('meals.csv','r')
        print(fileObj.read())
        fileObj.close()
      if choice == 'list':
        if len(name) == 0:
          print("\nNo meal has been added yet")
      if choice == 'add':
        fileObj = open('meals.csv','a')
        print("\nEnter a name for the meal:")
        meals_name = input()
        name.append(meals_name)
        print("\nEnter the price:")
        meals_price = input()
        fileObj.write(meals_name + ',')
        fileObj.write(" " + meals_price + " euros" "\n")
        fileObj.close()
      if choice == 'index':
        print("\nYou want to find a specific meal, type the meal number id(starts with 0 then 1 then 2 etc):")
        fileObj = open('meals.csv','r')
        print(fileObj.read())
        meal_id = int(input())
        f=open('meals.csv')
        lines=f.readlines()
        print(lines[meal_id])
        fileObj.close()
  if option == 'customers':
    class meals:
      def __init__(self, idc, namec, address):
        self.idc = idc
        self.namec = namec
        self.address = address
    namec = []
    choice = ""
    fileObj = open('customer.csv','a+')
    while choice != 'stop':
      print("\nType 'add' to add a new customer, 'list' to see all the customers, 'stop' to stop the program, or 'index' to find a specific customer:")
      choice = input()
      if choice == 'stop':
        print("\nOkay bye :)")
      if choice == 'list':
        fileObj = open('customer.csv','r')
        print(fileObj.read())
        fileObj.close()
      if choice == 'list':
        if len(namec) == 0:
          print("\nNo customer has been added yet")
      if choice == 'add':
        fileObj = open('customer.csv','a')
        print("\nEnter a name for the customer:")
        customer_name = input()
        namec.append(customer_name)
        print("\nEnter the customer adress:")
        adress = input()
        fileObj.write(customer_name + ', ')
        fileObj.write(adress + "\n")
      if choice == 'index':
        print("\nYou want to find a specific customer, type the customer number id (starts with 0 then 1 then 2 etc):")
        fileObj = open('customer.csv','r')
        idc = int(input())
        f=open('customer.csv')
        lines=f.readlines()
        print(lines[idc])
        fileObj.close()
  if option == 'orders':
    mid = []
    choice = ""
    orderdic ={}
    x = 1
    while choice != 'stop':
      print("\nTo add an order type 'add',to list all the undelivered orders type 'list undelivered', 'edit' to edit if an order has been delivered, or 'stop' to stop the program.")
      choice = input()
      if choice == 'add':
        print("\nType the meal id:")
        mid = input()
        print("\nType the customer id:")
        cid = input()
        print("\nWas the order delivered?(Yes or no):")
        delivered = input("")
        orderdic[x]= "Meal id:"+mid + ", " + "Customer id:"+cid + ", " + "delivered? "+delivered
        x = x + 1
      if choice == 'edit':
        print("\nWhat order do you want to edit?(Type the order ID):")
        pretty = pprint.PrettyPrinter(width=50)
        pretty.pprint(orderdic)
        ec = int(input())
        orderdic[ec] ="Meal id:"+mid + ", " + "Customer id:"+cid + ", " + "delivered? " + 'yes'
        print("\nThe order has been updated from not delivered to delivered")
        print(orderdic[ec])
      if choice == 'list undelivered':
        y = 1
        x = 37
        for value in orderdic:
          if orderdic[y][x] == 'n':
            pretty = pprint.PrettyPrinter(width=50)
            pretty.pprint(orderdic[y])
            y = y + 1