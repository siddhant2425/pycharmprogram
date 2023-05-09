




class product:
    Product_company="Tcs"
    def __init__(self,prdid,prdname,prdqty):
        self.prdid=prdid
        self.prdname=prdname
        self.prdqty=prdqty
        self.price=500

    @classmethod
    def product_company_cal(cls):
        cls.Product_company="Tcs.Ltd"

    @staticmethod
    def total_qty_price(p,q):
        qty_price=p*q
        return qty_price

    def show(self):
        print("product id::",self.prdid)
        print("product name::",self.prdname)
        print("product quantity::",self.prdqty)
        print("product price::",self.price)
        tqpc=self.total_qty_price(self.price,self.prdqty)
        print("total quantity::",tqpc)
        print("company Name Before::",product.Product_company)
        self.product_company_cal()
        print("company Name After::", product.Product_company)


obj=product(101,'copper',100)
obj.show()
