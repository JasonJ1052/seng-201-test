---
title: More practice
description: Additional samples for you to practice on.
weight: 15
---

Use these files to practice your debugging skills with the debugger. Look for the keyword `BUG` in the files on how to expose the error.

All of these files have simple, one-line fixes.

1. [`fibonacci.py`](fibonacci.py)
    {{< card code=true header="`fibonacci.py` expected output" lang="bash" >}}
This program tells you what the nth Fibonacci number is.
Enter a number for n: 4
Fibonacci number 4 is: 3

This program tells you what the nth Fibonacci number is.
Enter a number for n: 7
Fibonacci number 7 is: 13
{{< /card >}}
2. [`discount.py`](discount.py)
    {{< card code=true header="`discount.py` expected output" lang="bash" >}}
Total price after discounts: 2250.0
The most expensive item is: Laptop which costs 1200
{{< /card >}}
3. [`inventory.py`](inventory.py)
    {{< card code=true header="`inventory.py` expected output" lang="bash" >}}
Inventory Management System
1. Add item
2. Remove item
3. Check stock
4. Exit
Choose an option: 1
Enter item name: apple
Enter quantity: 10
Added 10 of apple. Total: 10

Inventory Management System
1. Add item
2. Remove item
3. Check stock
4. Exit
Choose an option: 2
Enter item name: apple
Enter quantity to remove: 15
Error: Not enough stock of apple to remove.   <--- note change!

Inventory Management System
1. Add item
2. Remove item
3. Check stock
4. Exit
Choose an option: 1
Enter item name: orange
Enter quantity: 10
Added 10 of orange. Total: 10

Inventory Management System
1. Add item
2. Remove item
3. Check stock
4. Exit
Choose an option: 2
Enter item name: orange
Enter quantity to remove: 10
Removed 10 of orange. Remaining: 0
orange is out of stock.         <--- note change!
{{< /card >}}