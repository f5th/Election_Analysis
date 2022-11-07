my_dictionary = {}

my_dictionary["Arapahoe"] = 422829

print(my_dictionary)

my_dictionary["Denver"] = 463353

my_dictionary["Jefferson"] = 432438

print(my_dictionary)
print(len(my_dictionary))

print(my_dictionary.items())

print(my_dictionary.keys())

print(my_dictionary.values())

print(my_dictionary.get("Denver"))

print(my_dictionary['Arapahoe'])

voting_data = []  # Create List Dictionary

print(type(voting_data))

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})


print(len(voting_data))

voting_data.insert(1,{"county": "El Paso","registered_voters":461149})

print(voting_data)

voting_data.pop(0)

print(voting_data)

voting_data[1] = {"county":"Jefferson", "registered_voters": 432438}

voting_data[2] = {"county":"Denver", "registered_voters": 463353}

print(voting_data)

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})