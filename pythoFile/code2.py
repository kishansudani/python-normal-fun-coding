class Product:
    def __init__(self, productName, productType, uintPrice, qtyOnHand):
        self.producatName = productName
        self.producatType = productType
        self.uintPrice = uintPrice
        self.qtyOnHand = qtyOnHand


class Store:
    def __init__(self, productList):
        self.productList = productList

    def purchaseProduct(self, producatName, qtyTobepurchased):
        for i in self.productList:
            if i.producatName == producatName and i.qtyOnHand > 0:
                if (i.qtyOnHand > qtyTobepurchased):
                    cal = i.qtyOnHand
                    i.qtyOnHand = i.qtyOnHand - qtyTobepurchased
                    return i.uintPrice * qtyTobepurchased
                elif (i.qtyOnHand < qtyTobepurchased):
                    val = i.qtyTobepurchased * i.uintPrice
                    i.qtyOnHand = 0
                    return val
            else:
                return None


if __name__ == "__main__":
    lenproductList = int(
        input('Enter Number of product you want to store in list : '))
    productList = []
    store = Store(productList)
    for _ in range(lenproductList):
        productName = input('Enter product name : ')
        productType = input('Enter product type : ')
        uintPrice = int(input('Enter product price : '))
        qtyOnHand = int(input('Enter product qtyOnHand : '))
        product = Product(productName, productType, uintPrice, qtyOnHand)
        store.productList.append(product)
    nameOfProducat = input('Enter the name of product you want to purchase : ')
    qtyOfProduct = int(
        input('Enter the qty of producat you want to purchase : '))
    print(store.purchaseProduct(nameOfProducat, qtyOfProduct))
