import pymongo

client = pymongo.MongoClient("mongodb+srv://USERNAME:PASSWORD@cluster0.nxzc2vh.mongodb.net/?retryWrites=true&w=majority")
db = client['storefront']
collection = db['items']

# Creating prompt loop to keep menu open for user
prompt = 0
while prompt <= 1:

    # How to add to database collection, "posts"
    # Requesting user input
    print("""
    Welcome to your inventory database, created by Shalofty.
    I can help you track items throughout your store or warehouse.
    Which of the following would you like to do?
    To Add items type: ADD
    To Search for items type: SEARCH
    """)
    menuSelect = input(">>>")
    menuSelect = menuSelect.upper()


    def addItem():

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

        # Verify data to user
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
            post = {'_id': upC, 'Name': itemName, "Brand": itemBrand, "Weight": itemWeight, "Quant": itemQuant,
                    "Ingredient": mainIngr}
            collection.insert_one(post)
        else:
            print("You decided not to commit the item to the database.")

    def itemSearch():

        # Collecting user input to use for the search
        print("""
        How would you like to search:
        Name, Ingredient, Brand
        """)
        searchtype = input(">>>")
        searchtype = str(searchtype).capitalize()

        print("""
        What would you like to search for:
        """)
        searchitem = input(">>>")
        searchitem = str(searchitem).upper()

        # Formatting user input to match args for find_one
        if searchtype == "NAME" or "INGREDIENT" or "BRAND":
            searchoutput = collection.find_one({searchtype: searchitem})
            print("Congratulations! We found an item that matches your search: " + "'" + searchoutput["Name"] + "'")

        for items in collection.find():

            print("ID: " + items["_id"])
            print("Name: " + items["Name"])
            print("Main Ingredient: " + items["Ingredient"])
            print("Brand: " + items["Brand"])
            print("Weight or Quantity: " + items["Weight"])
            items["Quant"] = str(items["Quant"])
            print("In stock: " + items["Quant"])


    # Comparing startingTask input statement from user
    # Adding items to the database
    if menuSelect == "ADD":
        addItem()

    # Searching through items in the database
    elif menuSelect == "SEARCH":
        itemSearch()

    elif menuSelect == "EXIT":
        prompt += 1

    else:
        print("Error. Search feature under construction.")

client.close()
