import csv


class Inventory:

    def __init__(self):
        self.product = []


    def readCsvFile(self, filename):
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader( csvfile, delimiter=',' )


            linecount=0
            for row in csvreader:
                if linecount == 0:
                    linecount += 1
                else:
                    dummy_dict = {}
                    dummy_dict['name'] = row[0]
                    dummy_dict['price'] = float( row[1] )

                    self.product.append( dummy_dict )


    def printProductCatalog(self):
        count = 0
        print( "id  product  price" )
        for product in self.product:
            print( f"{count}. {product['name']} {product['price']}" )
            count += 1

class Billing:
    def __init__(self):
        self.amount=0
        self.id=0
        self.quantity=0
        self.bill=""
        self.productCatalog=Inventory()

    def generateBill(self):
        self.productCatalog.readCsvFile("list_of_products.csv")
        check="y"

        self.bill="productname\tquantity\tprice\n"
        while(check!="n"):
            self.productCatalog.printProductCatalog()
            self.id=int(input("enter the id of the product: "))
            self.quantity=int(input("enter the quantity:"))

            price=self.quantity*self.productCatalog.product[self.id]['price']
            self.amount+=price

            self.bill+=f"{self.productCatalog.product[self.id]['name']}\t{self.quantity}\t{price}\n"
            check=input("press n to generate bill")
        self.bill+=f"total={self.amount}"
        print(self.bill)
        return self.amount





class Money:
    def __init__(self):

        self.total=0
        self.given=0



    def change_return(self, total, given):
        statement = "change in return:\n"
        self.given=given
        self.total=total




        remaining=self.given-self.total

        while remaining > 0:
            if remaining >= 100:
                quotient = remaining // 100
                remaining %= 100

                statement += f"{quotient}*100\n"
            elif 100 > remaining >= 50:
                quotient = remaining // 50
                remaining %= 50

                statement += f"{quotient}*50\n"

            elif 50 > remaining >= 20:
                quotient = remaining // 20
                remaining %= 20

                statement += f"{quotient}*20\n"
            elif 20 > remaining >= 10:
                quotient = remaining // 10
                remaining %= 10

                statement += f"{quotient}*10\n"
            elif 10 > remaining >= 5:
                quotient = remaining // 5
                remaining %= 5

                statement += f"{quotient}*5\n"
            elif 5 > remaining >= 2:
                quotient = remaining // 2
                remaining %= 2

                statement += f"{quotient}*2\n"
            else:
                quotient = remaining // 1
                remaining %= 1

                statement += f"{quotient}*1\n"

        return statement






bill=Billing()


total=bill.generateBill()
print(f"Bill amount is: {total}")
given=int(input("enter the given amount"))

money=Money()
print(money.change_return(total, given))

