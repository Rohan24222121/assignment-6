def ds(roll_no, name):
    # Adding values to data structures
    my_list = [roll_no, name]
    my_tuple = (roll_no, name)
    my_set = {roll_no, name}
    my_dict = {"roll_no": roll_no, "name": name}

    # Printing the initial data structures
    print("Initial Data Structures:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Modifying values during runtime
    new_roll_no = input("Enter new roll number: ")
    new_name = input("Enter new name: ")

    # Modifying the values in data structures
    my_list[0] = new_roll_no
    my_list[1] = new_name

    # Tuple is immutable, so create a new tuple with modified values
    my_tuple = (new_roll_no, new_name)

    # Remove the old values and add the modified values in the set
    my_set.remove(roll_no)
    my_set.add(new_roll_no)
    my_set.remove(name)
    my_set.add(new_name)

    # Update the values in the dictionary
    my_dict["roll_no"] = new_roll_no
    my_dict["name"] = new_name

    # Printing the modified data structures
    print("Modified Data Structures:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Deleting the data structures
    del my_list
    del my_tuple
    del my_set
    del my_dict

    # Trying to access the deleted data structures will raise an error
    print("Data structures deleted!")

# Example usage
ds("123", "John")
