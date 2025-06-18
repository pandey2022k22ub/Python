
cities = ["New York", "Los Angeles", "Chicago"]
insert_city = input("Enter a city to insert: ")
cities.append(insert_city)  
delete_city = input("Enter a city to delete: ")
if delete_city in cities:
    cities.remove(delete_city)
else:
    print(f"{delete_city} not found in the list of cities.")        


print("The list of cities is:", cities) 
