#BubbleSort Function
def BubbleSort (arrVals):
    limit = len(arrVals)
    Sorted = False
    while not Sorted:
        Sorted = True
        for i in range( limit-1 ):
            if arrVals[i] > arrVals[i+1]:
                arrVals[i], arrVals[i+1] = arrVals[i+1], arrVals[i]
                Sorted = False
    if Sorted == True:
        return (arrVals)

#SelectionSort Function
def SelectionSort(arrVals):
    LimitI = len( arrVals ) - 1
    LimitJ = len( arrVals )
    for i in range(LimitI):
        itemToMove = i
        for j in range(i+1, LimitJ):
            if arrVals[j] < arrVals[itemToMove]:
                itemToMove = j
        arrVals[i], arrVals[itemToMove] = arrVals[itemToMove], arrVals[i]
    return (arrVals)

#InsertionSort Function
def InsertionSort(arrVals):
    LimitI = len( arrVals ) 
    LimitJ = len( arrVals )
    for i in range(LimitI):
        itemToMove = i
        for j in range(i+1, LimitJ):
            if arrVals[j] > arrVals[itemToMove]:
                itemToMove = j
        arrVals.insert(0,arrVals[itemToMove])
        arrVals.pop(itemToMove+1)
    return (arrVals)

#BinarySearch Function
def binarySearch (sortedArr, searchItem):
    bottom = 0
    top = len(sortedArr) - 1
    middle = (bottom + top) // 2
    while bottom < top and sortedArr[middle] != searchItem:
        if sortedArr[middle] < searchItem:
            bottom = middle + 1
        else:
            top = middle - 1
        middle = (bottom + top) // 2
    if sortedArr[middle] == searchItem:
        return middle
    else:
        return -1

#Indirect Array Function


numList = [ 7, 15, 21, 34, 378234, 11,88, 3 ]
print(SelectionSort(numList))

#dicionary assignment

file_name = input("Please enter the file name:")
try:
    
    if file_name == "fruitlist.txt":
      fruits = open("fruitlist.txt", "r")  
      file = fruits.read()
      print(file)

except Exception:
    print("file not found")


def remove_space(tmpFile):
  if "," in file:
    tmpFile = tmpFile.split(",")

  tmpFile = [item.replace(" ", "") for item in tmpFile]

  tmpFile_upper = [names.upper() for names in tmpFile]
  return (tmpFile_upper)


def makeDictionary(tmpFile_upper):
  dict = {}
  num = -1
  for i in tmpFile_upper:
    num = num + 1
    x = str(i)
    dict2 = {}
    for j in x:
      for n in x:
        dict2Val = tmpFile_upper[num].count(j)
        dict2[j] = dict2Val
    value = dict2
    dict[i] = value
  return (dict)


def charCount(tmpFile):
  list = sorted(str(tmpFile))
  dic = {}
  for i in list:
    dic[i] = list.count(i)
  if i not in list:
    del dic[i]
  del dic['[']
  del dic["'"]
  del dic[","]
  del dic[']']
  del dic[' ']
  return (dic)
  
arrangedList = remove_space(file)
fullDict = makeDictionary(arrangedList)
charCountDict = charCount(arrangedList)

print(arrangedList)
print("")
print(fullDict)
print("")
print(charCountDict)

fruits.close()
#closing the file

