#Question 4(i)
# Create a list of five of your favorite foods. Write a Python program to:
# Add two more items to the list.
# Remove one item from the list.
# Print the updated list.

fav_foods = ["Rice", "Irish potatoes", "Matooke", "Yams", "Posho"]
fav_foods.extend(["Spaghetti", "Sweet potatoes"])
fav_foods.remove("Posho")
print(fav_foods)


#Question 4(ii)
# Given the list numbers = [2, 5, 8, 10, 3, 6], write a Python program to:
# Print the first and last elements of the list.
# Print the list in reverse order.
# Calculate and print the sum of all the elements in the list.

numbers = [2, 5, 8, 10, 3, 6]
print(numbers[0])
print(numbers[-1])
print(numbers[::-1])
total_sum = sum(numbers)
print(f"The sum of all numbers in the list is: {total_sum}")