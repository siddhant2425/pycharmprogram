

class product:
    product_company='wipro'
    def __init__(self,prdid,prdname,prdqty):
        self.prdid=prdid
        self.prdname=prdname
        self.prdqty=prdqty
        self.price=500
    @classmethod
    def company_name_cal(cls):
         cls.product_company='wiproLtd'

    def show(self):
        print("product id::",self.prdid)
        print("product name::",self.prdname)
        print("product qty::",self.prdqty)
        print("product price::",self.price)
        tqpc=self.total_qty_price_cal(self.price,self.prdqty)
        print("TQPC::",tqpc)

    @staticmethod
    def total_qty_price_cal(p,q):
         qty_price=p*q
         return qty_price

obj=product(101,'copper',450)
obj.show()
