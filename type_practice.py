# Create variables for first name and last name
# There are 6 variables in total and in each variable I assign a string to it
# By using equal sign, I can assign string to a variable
first_name_1 = "Cherina"
last_name_1 = "Chung"
first_name_2 = "Cally"
last_name_2 = "Kilduff"
first_name_3 = "Minahil"
last_name_3 = "Khan"
# Print full name with a space between first and last name
# full_name is a new variable that combines/ concatenates 2 variable and a string
full_name_1 = first_name_1 + " " + last_name_1
print("Full Name:", full_name_1)
full_name_2 = first_name_2 + " " + last_name_2
print("Full Name:", full_name_2)
full_name_3 = first_name_3 + " " + last_name_3
print("Full Name:", full_name_3)

# Transfer variable values into a list and display the list
# I put variable into square bracket to make it a list
name_list = [full_name_1, full_name_2, full_name_3]
print("Name List:", name_list)

# Step 6: Store variable values in a dictionary using keys 'first' and 'last' and display the dictionary values I put
# my variables into a curly bracket to make it a dictionary. I have used string to identify which position the full
# name lies.
name_dict = {'first': full_name_1, 'middle': full_name_2, 'last': full_name_3}
print("Name Dictionary:", name_dict)

# Step 6: With just one full name
# If we just want one person's full name, we can use this code
name_dict = {'first': first_name_1, 'last': last_name_1}
print("Name Dictionary with just one name:", name_dict)

