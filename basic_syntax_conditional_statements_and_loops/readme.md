Lab: Basic Syntax, Conditional Statements, and Loops



1. Number Definer

Write a program that reads a floating-point number and:
- prints "zero" if the number is zero
- prints "positive" or "negative"
- adds "small" if the absolute value of the number is less than 1 and it is not 0, or "large" if it exceeds 1 000 000


2. Largest of Three Numbers

Write a program that receives three whole numbers and prints the largest one.


3. Word Reverse

Write a program that receives a single word, reverses it, and prints it.


4. Even Numbers

Write a program that receives a number n on the first line. On the following n lines, it receives different integer numbers.
If the program receives an odd number, print "{num} is odd!" and end the program. Otherwise, if all numbers given are even, print "All numbers are even.".
  
  
5. Number Between 1 and 100

Write a program that reads different floating-point numbers from the console.
 When it receives a number between 1 and 100 inclusive, the program should stop reading and should print "The number {number} is between 1 and 100".
  
  
6. Shopping

Write a program that reads an integer number representing a budget. On the following lines, it reads integer numbers representing the prices of each product you should buy until it receives the command "End".
During the iterations, if there is not enough budget left to buy the next product, it prints "You went in overdraft!" and end the program.
Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."
  
  
7. Patterns

Write a program that receives a number and creates the following pattern. The number represents the largest count of stars on one row.


8. Drink Something

Kids drink toddy, teens drink coke, young adults drink beer, and adults drink whisky. Create a program that receives a person's age and prints what he/she drinks.
Rules:
- A kid is defined as someone under or at the age of 14.
- A teen is defined as someone under or at the age of 18.
- A young adult is defined as someone under or at the age of 21.
- An adult is defined as someone above the age of 21.
Note: All the values are inclusive except the last one!


9. Chat Codes

Peter is a programming enthusiast who wants to create a chat where people will send messages via number codes. He starts by creating a program for only four messages. 
Create a program that receives the n number of messages sent. On the following n lines, it will receive integer numbers. For each number, the program should print a different message:
- If the number is 88 - "Hello"
- If the number is 86 - "How are you?"
- If the number is not 88 nor 86, and it is below 88 - "GREAT!"
- If the number is over 88 - "Bye."


10. Maximum Multiple

On the first line, you will be given a positive number, which will serve as a divisor. On the second line, you will receive a positive number that will be the boundary. You should find the largest integer N, that is:
- divisible by the given divisor
- less than or equal to the given bound
- greater than 0
Note: it is guaranteed that N is found.


11. Orders

You work at a coffee shop, and your job is to place orders to the distributors. Thus, you want to know the price of each order. On the first line, you will receive integer N - the number of orders the shop will receive. For each order, you will receive the following information:
- Price per capsule - a floating-point number in the range [0.01…100.00]
- Days - integer in the range [1…31]
- Capsules, needed per day - integer in the range [1…2000]
For each order, you should print a single line in the following format:
"The price for the coffee is: ${price}"
If you do not receive a correct order (one or more of the values are not in the given range), you should ignore it and move to the next one.
After you go through all orders, you need to print the total price in the following format:
"Total: ${total_price}"
Both the price of a coffee and the total price must be formatted to the second decimal place. 
