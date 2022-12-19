'''Project on textile business management'''
import pickle
import os 
import datetime
import matplotlib.pyplot as plt
import numpy as np
'''--------------------------------------------------------------------------------------------------------------------'''

'''The get_menu_choice function displays the menu and gets a validated choice from the user'''
def get_menu_choice():

    print()
    print('\n\t\t\t WELCOME TO COMFORT MARKETING   ', end = '')
    print('\n\n')
    print('\t\t\t 1. ADD STOCK ')
    print('\t\t\t 2. SEARCH STOCK ')
    print('\t\t\t 3. SHOW STOCK')
    print('\t\t\t 4. UPDATE STOCK')
    print('\t\t\t 5. DELETE STOCK ')
    print('\t\t\t 6. SELL ITEM ')
    print('\t\t\t 7. SALE OF THE DAY')
    print('\t\t\t 8. EXIT')
    print('\n'*2)
    
    choice = int(input("\t\t Enter choice: "))
    '''Validate the user's choice'''
    if choice < 1 or choice > 8:
        choice = int(input('\t\t Enter a valid choice: '))
    return choice


'''The addStock function reads a binary file or creates one if not already created and gets data for the stock from the user''' 
def addStock():

    if os.path.exists('Textile.dat'):
        f = open("Textile.dat", "r+b")
        textile = pickle.load(f)
        t_id = len(textile) + 1
        #To check the duplication of textile id
        for i in textile:
            if i[0] == t_id:
                t_id +=1
    else:
        f = open('Textile.dat', 'wb')
        textile = []
        t_id = 1

    print('\n\t\t\t Textile ID :',t_id)
    t_name = input('\n\t\t\t Enter Item Name: ')
    qty = int(input('\n\t\t\t Enter Quantity: '))
    rate = int(input('\n\t\t\t Enter rate per piece: '))
    amount = qty * rate
    print('\n\t\t\t TOTAL AMOUNT: ', amount)

    textile.append([t_id, t_name, qty, rate, amount])
    f.seek(0,0)
    pickle.dump(textile, f)
    f.close()
    print("\n\t\t\t '''DATA SAVED''' ")

'''searchStock() function reads the already created binary file("Textile.dat") and searches a record in the stock by inputting Item's Name and also displays the updated details'''
def searchStock():

    if os.path.exists("Textile.dat"):
        f = open("Textile.dat", "rb")
        textile = pickle.load(f)
        n = input('\n\t\t\t Enter Item Name (first few letters will work): ')
        found = False

        for t in textile:
            t[4] = t[2] * t[3]
            if n.upper() in t[1].upper():
                print('\n')
                print('-'*67)
                print('%16s'%'TEXTILE ID |','%15s'%'ITEM NAME |','%9s'%'QTY |','%11s'%'RATE |','%12s'%'AMOUNT')
                print('-'*67)
                print('%16s'%t[0],'%15s'%t[1],'%9s'%t[2],'%11s'%t[3],'%12s'%t[4])
                found = True
                break

        if not found:
            print("\n\t\t\t '''Item Not Found!''' ")
        f.close()

    else:
        print("\n\t\t\t '''File Not Found!'''")


'''The showStock() function displays the stock stored in the binary file(Textile.dat) entered by the user'''
def showStock():

    f = open("Textile.dat","rb")
    textile = pickle.load(f)
    print('\n')
    print('-'*67)
    print('%16s'%'TEXTILE ID |','%15s'%'ITEM NAME |','%9s'%'QTY |','%11s'%'RATE |','%12s'%'AMOUNT')
    print('-'*67)

    for t in textile:
        t[4] = t[2] * t[3]
        print('%16s'%t[0],'%15s'%t[1],'%9s'%t[2],'%11s'%t[3],'%12s'%t[4])
    f.close()


'''The updateStock() function updates Quantity and Rate of a particular Item as per the user's choice in the stock if the binary file("Textile.dat") already exists''' 
def updateStock():

    if os.path.exists('Textile.dat'):
        f = open("Textile.dat", "r+b")
        textile = pickle.load(f)
        t_name = input('\n\t\t\t Enter Item Name to be updated (first few letters will work): ')
        found = False
        print('\n')
        print('-'*67)
        print('%16s'%'TEXTILE ID |','%15s'%'ITEM NAME |','%9s'%'QTY |','%11s'%'RATE |','%12s'%'AMOUNT ')
        print('-'*67)

        for t in range(len(textile)):
            textile[t][4] = textile[t][2] * textile[t][3]
            if t_name.lower() in textile[t][1].lower():
                print('%16s'%textile[t][0],'%15s'%textile[t][1],'%9s'%textile[t][2],'%11s'%textile[t][3],'%12s'%textile[t][4])
                print('\n\n')
                q = int(input('Enter Quantity to be updated: '))
                textile[t][2] = q
                p = int(input('Enter rate to be updated: '))
                textile[t][3] = p
                textile[t][4] = textile[t][2] * textile[t][3]
                print("\n\t\t\t '''STOCK UPDATED'''")
                found = True
                break

        if not found:
            print("\n\t\t\t Item Not Found!")
        f.seek(0, 0)
        pickle.dump(textile, f)
        f.close()

    else:
        print('\n\t\t\t File Not Found!')


'''The deleteStock() function first finds the index of the item to be deleted entered by the user and then pops that item's list from the main list textile and then dumps all the remaining data back into the binary file("Textile.dat")'''
def deleteStock():

    if os.path.exists("Textile.dat"):
        f = open("Textile.dat","r+b")
        textile = pickle.load(f)
        showStock()
        n = input('\n\n\t\t\t Enter Item Name (first few letters will work): ')
        found = False
        pos = None

        for i in range(len(textile)):
            textile[i][4] = textile[i][2] * textile[i][3]
            if n.upper() in textile[i][1].upper():
                print('\n')
                print('-'*67)
                print('%16s'%'TEXTILE ID |','%15s'%'ITEM NAME |','%9s'%'QTY |','%11s'%'RATE |','%12s'%'AMOUNT')
                print('-'*67)
                print('%16s'%textile[i][0],'%15s'%textile[i][1],'%9s'%textile[i][2],'%11s'%textile[i][3],'%12s'%textile[i][4])
                pos = i
                found = True
                break

        if not found:
            print("\n\t\t\t '''Item Not Found!'''")
        else:
            textile.pop(pos)
            print('\n\t\t\t ----ITEM DELETED SUCCESSFULLY!---- ')

        f.seek(0,0)
        pickle.dump(textile, f)
        f.close()

    else:
        print("\n\t\t\t '''File Not Found!'''")


'''The get_qty_Rate function returns the Item name, Quantity, Rate of a particular item(t_name) to be used in the sellItem function'''
def get_qty_Rate(textile,t_name):

    found = False
    for i in range(len(textile)):
        if t_name.lower() in textile[i][1].lower():
            pos = i
            found = True
            break

    if found:
        return textile[pos][1], textile[pos][2], textile[pos][3]
    else:
        return None  


'''The sellItem() function stores all the information of the purchased items in a newly created binary file("Transaction.dat") which can be accessed later and it prints the bill'''
def sellItem():

    if os.path.exists('Textile.dat'):
        f = open("Textile.dat", "r+b")
        textile = pickle.load(f)
        again = 'y'
        purchaselist = []

        while again.lower() == 'y':
            showStock()
            n = input('\n\n\t\t\t Enter Item Name (first few letters will work): ')
            status = get_qty_Rate(textile, n)

            if status == None:
                print("\n\t\t\t SORRY! NO SUCH ITEM IN THE STOCK.")
            else:
                print('\n\t\t\t Item Name: ', status[0])
                print('\t\t\t Quantity Available: ', status[1])
                print('\t\t\t Rate: ', status[2])
                q = int(input('\n\t\t\t Enter Quantity to be sold: '))
                d = datetime.datetime.now()
                billd = str(d.day)+'/'+str(d.month)+'/'+str(d.year)+' '+str(d.hour)+':'+str(d.minute)+':'+str(d.second)
                purchaselist.append([status[0], q, status[2], billd])
                
            again = input('\n\t\t\t Want to purchase more Items (y | n) ?: ')

        total = 0
        for i in purchaselist:
            amount = i[1] * i[2]
            total += amount

        '''Updating the quantity in the Main Stock'''
        for p in purchaselist:
            for i in range(len(textile)):
                if p[0] in textile[i][1]:
                    textile[i][2] -= p[1]
                    break
        f.seek(0, 0)
        pickle.dump(textile, f)
        f.close()

        if os.path.exists("Transaction.dat"):
            filein = open("Transaction.dat", "r+b")
            purchase_record = pickle.load(filein)
            filein.seek(0, 0)
            for i in range(len(purchaselist)):
                purchase_record.append([purchaselist[i][0], purchaselist[i][1], purchaselist[i][2], purchaselist[i][3]])
            pickle.dump(purchase_record, filein)
            filein.close()
        else:
            filein = open("Transaction.dat", "wb")
            pickle.dump(purchaselist, filein)
            filein.close() 

        print('\n\n Order No. : 201900331508')
        print('\n ********************BILL INVOICE**********************')
        print('\n\n')
        print(' --------------------------------------------------------')
        print('%20s'%'ITEM NAME |','%10s'%'QUANTITY |','%9s'%'RATE |','%9s'%'AMOUNT')
        print(' --------------------------------------------------------')

        for i in range(len(purchaselist)):
            amount = purchaselist[i][1] * purchaselist[i][2]
            print('%20s'%purchaselist[i][0], '%10s'%purchaselist[i][1], '%9s'%purchaselist[i][2], '%9s'%amount)

        print(" =========================================================")
        print('\t GRANT TOTAL = ',total)
        print(" =========================================================")
        print("\t Bill generated on :",billd)   
        print('\n\n')
        paid = float(input(" Enter amount paid: "))

        def check(p, t):
            if p >=t:
                print(" Amount returned: ", p-t)
            else:    
                while p < t:
                    print(" The Transaction can't be processed ... Amount to be paid is more than the deposited amount.")
                    p = float(input(" Enter valid amount: "))
                    if p >= t:
                        print(" Amount returned: ", p-t)
                        break

        check(paid, total)
        
    else:
        print("\n\t\t\t File Not Found!")


'''The SaleoftheDay() function displays all the details of the items sold in a particular day'''
def SaleoftheDay():

    if os.path.exists('Transaction.dat'):
        f = open('Transaction.dat','rb')
        purchases = pickle.load(f)
        d = datetime.datetime.now()
        cur_date = str(d.day)+"/"+str(d.month)+"/"+str(d.year)
        print("\n\t\t\t TODAY IS : ",cur_date)
        total = 0
        graph_x = []
        graph_y1 = []
        graph_y2 = []
        print('\n\n')
        print(' --------------------------------------------------------')
        print('%20s'%'ITEM NAME |','%10s'%'QUANTITY |','%9s'%'RATE |','%9s'%'AMOUNT')
        print(' --------------------------------------------------------') 

        for p in purchases:
            pos = p[3].index(' ')
            trans_date = p[3][:pos]
            if cur_date == trans_date:
                amount = p[1]*p[2]
                print('%20s'%p[0],'%10s'%p[1],'%9s'%p[2],'%9s'%amount)
                total+=amount
                graph_x.append(p[0])
                graph_y1.append(amount)
                graph_y2.append(p[1])
        #plot 1
        x = np.array(graph_x)
        y = np.array(graph_y2)
        plt.subplot(1, 2, 1)
        plt.bar(x, y, width = 0.4)
        plt.title(" QUANTITY VS ITEM_NAME")
        plt.show()

        #plot 2
        x = np.array(graph_x)
        y = np.array(graph_y1) 
        plt.subplot(1,2,2)
        plt.bar(x, y, width = 0.4, color = "#4CAF50")
        plt.title(" AMOUNT VS ITEM_NAME ")
        plt.show()

        print(" =========================================================")
        print('\t TOTAL AMOUNT FOR DAY = Rs.',total)
        print(" ========================================================= \n\n")
                              
    else:
        print('\n\t\t\t## FILE NOT FOUND ##')


def logic():
  choice = 0
  while choice != 8:
      #Get the user's menu chocie
      choice = get_menu_choice()
      #Process the choice
      if choice == 1:
          addStock()
      elif choice == 2:
          searchStock()
      elif choice == 3:
          showStock()
      elif choice == 4:
          updateStock()
      elif choice == 5:
          deleteStock()
      elif choice == 6:
          sellItem()
      elif choice == 7:
          SaleoftheDay()
