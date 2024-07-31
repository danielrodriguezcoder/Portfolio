__author__ = "Daniel Rodriguez-Demers"
__copyright__ = "Copyright 2024, Daniel Rodriguez-Demers"

__license__ = "GNU GPLv3"
__version__ = "1.0"
__email__ = "wakawa@hotmail.com"
__status__ = "Demo"

# quick app to store items' values and to calculate income

# Listing names and prices of products with a dictionary
my_products = {
    "Bubblegum":2.0, "Toffee":0.2, "Ice Cream":5.0, "Milk chocolate":4.0, "Doughnut":2.5, "Pancake":3.2
}

print("Prices:")
for x,y in my_products.items():
    print(x + ": $" + str(y))

# --- expected output ---
# Bubblegum: $202
# Toffee: $118
# Ice cream: $2250
# Milk chocolate: $1680
# Doughnut: $1075
# Pancake: $80
#
# Income: $7777.0

# Listing sales value per product and total of sales using loops and a dictionary

my_sales = {
    "Bubblegum": 202, "Toffee": 118, "Ice cream": 2250, "Milk chocolate": 1680, "Doughnut": 1075, "Pancake": 80
}
print("Earned amount:")
total = 0.0
for x, y in my_sales.items():
    print(x + ": $" + str(y))
    total += y
print()
print("Income: $" + str(total))
print("Staff expenses:")
staff_expense = int(input())
print("Other expenses:")
other_expense = int(input())
net_income = total - staff_expense - other_expense
print("Net income: $" + str(net_income))

# --- expected output ---
# Earned amount:
# Bubblegum: $202
# Toffee: $118
# Ice cream: $2250
# Milk chocolate: $1680
# Doughnut: $1075
# Pancake: $80
#
# Income: $5405.0
# Staff expenses:
# > 4170
# Other expenses:
# > 220
# Net income: $1015.0
