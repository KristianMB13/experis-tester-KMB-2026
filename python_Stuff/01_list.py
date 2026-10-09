product1Name = "Green Tea"
product2Name = "Black Tea"
product3Name = "White Tea"

# print(product1Name)
# print(product2Name)
# print(product3Name)


productNames = ["Green Tea", "Black Tea", "White Tea"]



#print(productNames[0])
#print(productNames[1])
#print(productNames[2])


# for productName in productNames:
#     print(productName)

# print(productNames[3]) # This will raise an IndexError since there is no index 3 in the list 


# for i in range(3):
#     print(f"{i+1}. {productNames[i]}")

# for item in mixed_list:
#     print(item)

mixed_list = ["name", 25]

productNames.append("Brown Tea")
productNames.insert(2, "Yellow Tea" )

productNames[0] = "Purple Tea" 

# for productName in productNames:
#     print(productName)


# print(len(productNames)) 
# print(min(productNames)) 
# print(max(productNames)) 

#  print(productNames[1:3])

#  print(productNames[::-1])

print("White Tea" in productNames)
print("Orange Tea" not in productNames)
