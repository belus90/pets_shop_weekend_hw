# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return(shop["name"])


def get_total_cash(shop):
    return(shop["admin"]["total_cash"])
    # print(sum)
# # def add_or_remove_cash(add):


def add_or_remove_cash(shop, amount):
    shop["admin"]["total_cash"] += amount


def get_pets_sold(shop):
    return(shop["admin"]["pets_sold"])


def increase_pets_sold(shop, amount):
    shop["admin"]["pets_sold"] += amount


def get_stock_count(shop):
    return len(shop["pets"])


def get_pets_by_breed(shop, breed_to_find):
    found_pets = []
    for pet in shop["pets"]:
        if pet["breed"] == breed_to_find:
            found_pets.append(pet)
    return found_pets


def find_pet_by_name(shop, name_to_find):
    for pet in shop["pets"]:
        if pet["name"] == name_to_find:
            return pet


def remove_pet_by_name(shop, name_to_remove):
    pet_to_remove = find_pet_by_name(shop, name_to_remove)
    return shop["pets"].remove(pet_to_remove)


def add_pet_to_stock(shop, new_pet):
    shop["pets"].append(new_pet)


def get_customer_cash(customer):
    return customer["cash"]


def remove_customer_cash(custumer, cash):
    custumer["cash"] -= cash


def get_customer_pet_count(custumer):
    return len(custumer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(custumer, new_pet):
    if(custumer["cash"] >= new_pet["price"]):
        return True
    else:
        return False


def sell_pet_to_customer(shop, pet, customer):
    if(pet != None):
        if(customer_can_afford_pet(customer, pet)):
            add_pet_to_customer(customer, pet)
            increase_pets_sold(shop, 1)
            remove_customer_cash(customer, pet["price"])
            add_or_remove_cash(shop, pet["price"])
