import random
name = ["Aayush", "Abin", "Abishek", "Ashish", "John", "Keshab", "Kushal", "Sonu"]
num_items = len(name)
random_choice = random.randint(0, num_items - 1)
payee = name[random_choice]
print(f"The payee is: {payee}")

