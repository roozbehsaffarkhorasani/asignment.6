from pyfiglet import Figlet
import qrcode
while True:
def ShowMenu():
    print(' 1-Add product \n 2-Edit product \n 3-Delete product \n 4-Creat QrCode \n 5-Show list \n 6-Buy \n 7-Exit \n 8-Search')
def AddProduct():
    productid=1006
    mydict={}
    mydict['id']=productid
    mydict['name']=input(('Enter a name of your product:'))
    mydict['price']=input(('Enter the price of your product:'))
    mydict['count']=int(input(('Enter the number of your stock: ')))
    dictlist.append(mydict)
    print("Your producted added successfully")
    productid+=1
def EditProduct():
    edition=input('Enter the name of the product that you wanna edit:')
    for i in range(len(dictlist)):
        if edition==dictlist[i]['name']:
            editing =int(input("What do you want to edit ? \n1-Product's ID \n 2-Product's name \n 3-Product's price \n 4-Product's count\n :"))
    if editing==1:
        new=input('Enter the id you want:')
        dictlist[i]['id']=new
        print('Your product updated successfully',dictlist[i])
    elif editing==2:
        new=input('Enter the name you want:')
        dictlist[i]['name']=new
        print('Your product updated successfully',dictlist[i]) 
    elif editing==3:
        new=input('Enter the new price :')
        dictlist[i]['price']=new
        print('Your product updated successfully',dictlist[i])       
    elif editing==4:
        new=input('Enter the new count of the product:')
        dictlist[i]['count']=new
        print('Your product updated successfully',dictlist[i])     
def DeleteProduct():
    delete=input('Enter the name of the product that you wanna delete:')
    for i in range(len(dictlist)):
        if delete==dictlist[i]['name']:
            del dictlist[i]
            break
    print("this product deleted successfully")  
def ShowQrcode():
    productqr=input('Enter the ID of the product:')
    for i in range(len(dictlist)):
        if productqr==dictlist[i]['id']:
          myqr=qrcode.make(dictlist[i])
          myqr.save(f'qrcode{i}.png')
          print('QrCode created')
          break
def newchance():
    ShowMenu()
    choice = int(input('Please choose a number : '))
myfile=open('database.txt', 'r')
data = myfile.read()
editing=0
count=0
dictlist=[]
product_list = data.split('\n')
for i in range(len(product_list)):
    product_info=product_list[i].split(',')
    mydict={}
    mydict['id']=product_info[0]
    mydict['name']=product_info[1]
    mydict['price']=product_info[2]
    mydict['count']=product_info[3]
    dictlist.append(mydict)
print(dictlist)
f = Figlet(font='standard')
print(f.renderText('Ramtin store'))
ShowMenu()
choice = int(input('Please choose a number : '))
if choice == 1:
    AddProduct()
    newchance()
elif choice == 2:
    EditProduct()
    newchance()     
elif choice == 3:
    DeleteProduct()
    newchance()   
elif choice == 4:
    ShowQrcode()
    newchance()
elif choice == 5:
    for i in range(len(dictlist)):
        print(dictlist[i])
elif choice == 6:
    buy=input('Enter the products id: ')
    for i in range(len(dictlist)):
        if buy == dictlist[i]['id']:
            count=int(input("Enter the number of the product: "))
            if count == dictlist[i]['count']:
                print('yes')
elif choice == 7:
    myfile=open('database.txt', 'a')
    myfile.write(dictlist)
elif choice == 8:
    search=input('Enter the name of the product that you are lookin for:')
    while search==dictlist[i]['name']:
        print(dictlist[i])
        break