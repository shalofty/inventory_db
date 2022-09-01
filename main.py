import pymongo

client = pymongo.MongoClient("mongodb+srv://shalofty:<PASSWORD>@cluster0.nxzc2vh.mongodb.net/?retryWrites=true&w=majority")
db = client['storefront']
collection = db['items']

# How to add to database collection, "posts"
# Requesting user input
print("""
Welcome to your inventory database, created by Shalofty.
I can help you track items throughout your store or warehouse.
Which of the following would you like to do?
To Add items type: ADD
To Search for items type: SEARCH
""")
startingTask = input(">>>")
startingTask = startingTask.upper()

# Comparing startingTask input statement from user
# Adding items to the database
if startingTask == "ADD":

    print("""
    You've chose to add items to the database.
    Please note, each item should have the following attributes:
    Name, Brand, Weight or Capsule Quantity, Quantity, Main Ingredients, UPC
    """)

    itemName = input("Item name: ")
    itemName = itemName.upper()

    itemBrand = input("Item brand: ")
    itemBrand = itemBrand.upper()

    itemWeight = input("Item weight or capsule quantity: ")
    itemWeight = itemWeight.upper()

    itemQuant = input("Item quantity: ")
    itemQuant = int(itemQuant)

    mainIngr = input("Main ingredient: ")
    mainIngr = mainIngr.upper()

    upC = input("UPC: ")
    upC = str(upC)

    # Pushing to database
    print(itemName)
    print(itemBrand)
    print(itemWeight)
    print(itemQuant)
    print(mainIngr)
    print(upC)
    print("Would you like to save this item to the database? (Y/N")
    pushPost = input(">>>")
    pushPost = pushPost.upper()

    # Committing item to the database
    if pushPost == "YES" or "Y":
        post = {'_id': upC, 'Name': itemName, "Brand": itemBrand, "Weight": itemWeight, "Quant": itemQuant, "Ingredient": mainIngr}
        collection.insert_one(post)
    else:
        print("You decided not to commit the item to the database.")

# Searching through items in the database
elif startingTask == "SEARCH":

    print("""
    You've chosen to search the database.
    How would you like to search?
    To Search by name type: NAME
    To search by brand type: BRAND
    To search by ingredient type: ING
    """)
    searchType = input(">>>")
    searchType = searchType.upper()

    if searchType == "NAME":

        print("What is it you're searching for?")
        searchInput = input(">>>")
        searchInput = str(searchInput)
        searchOutput = collection.find_one({"Name": searchInput.upper()})
        print("Congratulations! We found an item that matches your search: " + "'" + searchOutput["Name"] + "'")

        for item in collection.find():
            print("ID: " + item["_id"])
            print("Name: " + item["Name"])
            print("Main Ingredient: " + item["Ingredient"])
            print("Brand: " + item["Brand"])
            print("Weight or Quantity: " + item["Weight"])
            item["Quant"] = str(item["Quant"])
            print("In stock: " + item["Quant"])

    elif searchType == "BRAND":

        print("What is it you're searching for?")
        searchInput = input(">>>")
        searchInput = str(searchInput)
        searchOutput = collection.find_one({"Brand": searchInput.upper()})
        print("Congratulations! We found brands that match your search: " + "'" + searchOutput["Brand"] + "'")

        for item in collection.find():
            print("ID: " + item["_id"])
            print("Name: " + item["Name"])
            print("Main Ingredient: " + item["Ingredient"])
            print("Brand: " + item["Brand"])
            print("Weight or Quantity: " + item["Weight"])
            item["Quant"] = str(item["Quant"])
            print("In stock: " + item["Quant"])

    elif searchType == "ING" or "INGREDIENT":

        print("What is it you're searching for?")
        searchInput = input(">>>")
        searchInput = str(searchInput)
        searchOutput = collection.find_one({"Ingredient": searchInput.upper()})
        print("Congratulations! We found items that match your search: " + "'" + searchOutput["Ingredient"] + "'")

        for item in collection.find():
            print("ID: " + item["_id"])
            print("Name: " + item["Name"])
            print("Main Ingredient: " + item["Ingredient"])
            print("Brand: " + item["Brand"])
            print("Weight or Quantity: " + item["Weight"])
            item["Quant"] = str(item["Quant"])
            print("In stock: " + item["Quant"])

    else:
        print("searchType if statement end")

else:
    print("Error. Search feature under construction.")

client.close()