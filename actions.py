# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "twiqstore.io"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have,\
and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for st in stores:
        print("- %s" %st.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for st in stores:
        
        if st.name.lower() == store_name.lower():
            return st
    
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()


    choice = input("Pick a store by typing its name.\
Or type \"checkout\" to pay your bills and say your goodbyes.\n").lower()

    if choice == "checkout":
        return False
    else:
        sstore = get_store(choice) # storing the result if there's a store.
        if sstore:
            print("==============================")
            # pick_products(Cart(), sstore)
            return sstore
        else:    
            print("No store with that name. Please try again")



def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    prd_names = {} # {product name: product object}

    print("%s :\n" %(picked_store.name))

    for prd in picked_store.products:
        print("%s \n" %(prd)) # or try use prd.__str__()
        prd_names[prd.name.lower()] = prd
        # prd_names.append(prd.name.lower())

    print("==DEBUG==")
    print("prd_names dict: %s" %prd_names)    
    print("==DEBUG==\n")

    print("""
    type an item you'd like to add in your cart
    by typing the product name exactly as it was spelled
    type 'back' to return back to the main menu
    where you can check out. 
    """)

    while True:
        choice = input()
        if choice in prd_names:
            cart.add_to_cart(prd_names[choice])

        elif choice == "back":
            return False
            # break, maybe? im not sure
        else:
            print("\n invalid product. Please pick only from the above items.\n")


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    while True:
        stor = pick_store()
        if stor == False:
            break
        
        prods = pick_products(cart, stor)
        # if prods != False:

    cart.checkout()




def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
