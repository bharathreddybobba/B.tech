from datetime import datetime

name=input("enter your name")
# list of items
lists='''
Rice    rs 50/kg
Weate   rs 25/kg
oil     rs 100/l
maggi   rs 100/kg
Boost   rs 180/kg
colgate rs 100/kg
salt    rs 10/kg
sugar   rs 50/kg
'''
#decelaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':50,'sugar':50,'weate':25,
       'oil':100,'maggi':100,'boost':180,'colgate':
       100,'salt':10}
option=int(input("for list of items press 1"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("enter your items")
        quantity=int(input("enter quantity"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("your item is not available")
    else:
        print("you entered wrong number")
    inp=input("can i bill the items yes or no")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","Bharath supermarket",25*"=")
            print(28 * " ", "suryapet")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ","items",8*"-","quantity",3*" ","price")

            for i in range(len(pricelist)):
                print(i,8*' ',5*' ',ilist[i],3*'',qlist[i],plist[i])
            print(75*"-")
            print(50*"",'totalAmount:','Rs',totalprice)
            print(" gst amount",40*" ",'Rs',gst)
            print(75 * "-")
            print(50 * "", 'finalAmount:', 'Rs', finalamount)
            print(75 * "-")
            print(20 * "", 'Thanks for visiting')
            print(75 * "-")













