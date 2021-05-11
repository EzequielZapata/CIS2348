# Ezequiel Zapata PSID: 001863257

# Final Project part 2 Query the user of an item by asking for manufacturer and item type with a single query.
# The program will then read the csv file and output the item to the user.
from datetime import date

# the part of the program that reads the manufacturerlist.csv file
def readFromManufacturerList():
    inventory = []
    list1 = []
    with open("ManufacturerList(2).csv", "r") as f:
        for l in f:
            l = l.split(",")
            list1 = list(l)
            list1.remove('\n')
            inventory.append(list1)
    return inventory

# the part of the program that reads the pricelist.csv file
def readFromPriceList():
    price_list = []
    list1 = []
    with open("PriceList(2).csv", "r") as f:
        for l in f:
            l = l.split(",")
            list1 = list(l)
            list1.remove('\n')
            price_list.append(list1)
    return price_list

# the part of the program that reads the servicedateslist.csv file
def readFromServiceDatesList():
    dateList = []
    list1 = []
    with open("ServiceDatesList(2).csv", "r") as f:
        for l in f:
            l = l.split(",")
            list1 = list(l)
            list1.remove('\n')
            dateList.append(list1)
    return dateList
# creating a class that will identify the item that the user inputs when we query the user
class Interactive_Inventory:
    def query(self, manufacturer, item_type):
        flag=False
        datalist=readFromManufacturerList()
        pricelist = readFromPriceList()
        servicelist = readFromServiceDatesList()
        today = date.today()
        day = today.strftime("%d")
        mon = today.strftime("%m")
        year = today.strftime("%Y")
        day=int(day)
        mon=int(mon)
        year=int(year)
        id=""
        man=""
        type=""
        price=""
        for a in datalist:
            if manufacturer == a[1] and item_type == a[2]  and len(a)==3:
                id = a[0]
                man = a[1]
                type = a[2]
                for s in servicelist:
                    if id == s[0]:
                        dt=s[1].split("/")
                        d1=int(dt[0])
                        m1= int(dt[1])
                        y1= int(dt[2])
                        if y1>year:
                            flag = True
                        elif y1==year:
                            if m1>mon:
                                flag=True
                            elif m1==mon:
                                if d1>=day:
                                    flag=True

        for p in pricelist:
            if id==p[0]:
                price=p[1]
# This part of the class will output the item id, manufacturer, item type, and the price to the user from the csv files
        if flag == True:
            print("Your item ID: ", id, "\tManufacturer Name:", man, "\tItem Type:", type, "\t Price:", price)
        if flag == False:
            print("No such Item in Inventory") # this will output if the user's input is not an item on the lists
        for a in datalist:
            if item_type==a[2] and id!=a[0] and len(a)==3:
                flag=False
                id=a[0]
                for s in servicelist:
                    if id == s[0]:
                        dt = s[1].split("/")
                        d1 = int(dt[0])
                        m1 = int(dt[1])
                        y1 = int(dt[2])
                        if y1 > year:
                            flag = True
                        elif y1 == year:
                            if m1 > mon:
                                flag = True
                            elif m1 == mon:
                                if d1 >= day:
                                    flag = True
                for p in pricelist:                     # for this part the output was to show the user of another item from the list they should consider.
                    if flag==True and id==p[0]:
                        print("You may also consider:\n item ID: ", a[0], "\tManufacturer Name:", a[1], "\tItem Type:", a[2], "\t Price:", p[1])

# outputting the from the 3 csv files
def main():
    print(readFromManufacturerList())
    print(readFromPriceList())
    print(readFromServiceDatesList())

# querying the user the prompts that the program needs to find their item and will ask to correct the input if they put in the wrong format
flag=False
while flag == False:
    print("Write the Manufacturer name and item type below:")
    inp=input()
    if inp=="q":
        break
    inp = inp.split(" ")
    length=len(inp)
    if inp!="q" and length>=2:
        manufacturer = inp[len(inp) - 2]
        type = inp[len(inp) - 1]
        obj = Interactive_Inventory()
        obj.query(manufacturer, type)
    if inp!="q":
        while length<2:
            print("Please write the input in correct format:")
            inp = input()
            inp = inp.split(" ")
            length = len(inp)
            if length>=2:
                manufacturer = inp[len(inp) - 2]
                type = inp[len(inp) - 1]
                obj = Interactive_Inventory()
                obj.query(manufacturer, type)
