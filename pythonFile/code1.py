from collections import OrderedDict


class Table:
    def __init__(self, tableNo, waiterName, status):
        self.tableNo = tableNo
        self.waiterName = waiterName
        self.status = status


def findwaiterWiseTotalNoOfTable(self, listOfTable):
    dictnary = {}
   for _ in listOfTable:
        if _.waiterName in dictnary:
            dictnary[_.waiterName] += 1
        else:
            dictnary[_.waiterName] = 1
    return dictnary

def findwaiterNameByTableNo(self, listOfTable, tableNo):
    for _ in listOfTable:
        if tableNo == _.tableNo:
            return _.waiterName
    return None

if __name__ == '__main__':
    totalNoOfTable = int(
        input("How many table object you would like to add to list of object : "))
    listOfObject = []
    for _ in range(totalNoOfTable):
        tableNo = int(input('Enter table No : '))
        waiterName = input('Enter waiter Name : ')
        status = input('Enter status of table : ')
        table = Table(tableNo, waiterName, status)
        listOfObject.append(table)
    forTableNo = int(input('Table No for reservation : '))
    listVal = findwaiterWiseTotalNoOfTable(listOfObject)
    dict1 = OrderedDict(sorted(listVal.items()))
    val = findwaiterNameByTableNo(listOfObject, forTableNo)
    for _ in dict1:
        print(f'{_}-{dict1[_]}')
    if val == None:
        print('No Table Found')
    else:
        print(val)
