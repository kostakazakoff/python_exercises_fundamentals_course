# Problem - World Tour
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#0.

You are a world traveler, and your next goal is to make a world tour. To do that, you have to plan out everything first. To start with, you would like to plan out all of your stops where you will have a break.
On the first line, you will be given a string containing all of your stops. Until you receive the command "Travel", you will be given some commands to manipulate that initial string. The commands can be:
"Add Stop:{index}:{string}":
Insert the given string at that index only if the index is valid
"Remove Stop:{start_index}:{end_index}":
Remove the elements of the string from the starting index to the end index (inclusive) if both indices are valid
"Switch:{old_string}:{new_string}":
If the old string is in the initial string, replace it with the new one (all occurrences)
Note: After each command, print the current state of the string if it is valid!
After the "Travel" command, print the following: "Ready for world tour! Planned stops: {string}"
### Input / Constraints
JavaScript: you will receive a list of strings
An index is valid if it is between the first and the last element index (inclusive) (0 ….. Nth) in the sequence.
### Output
Print the proper output messages in the proper cases as described in the problem description

# Problem2 - Destination Mapper
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#1.

Now that you have planned out your tour, you are ready to go! Your next task is to mark all the points on the map that you are going to visit.
You will be given a string representing some places on the map. You have to filter only the valid ones. A valid location is:
Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
After the first "=" or "/" there should be only letters (the first must be upper-case, other letters could be upper or lower-case)
The letters must be at least 3
Example: In the string "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" only the first two locations are valid.
After you have matched all the valid locations, you have to calculate travel points. They are calculated by summing the lengths of all the valid destinations that you have found on the map. 
In the end, on the first line, print: "Destinations: {destinations joined by ', '}". 
On the second line, print "Travel Points: {travel_points}".
### Input / Constraints
You will receive a string representing the locations on the map
JavaScript: you will receive a single parameter: string
### Output
Print the messages described above

# Problem - Plant Discovery
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#2.

You have now returned from your world tour. On your way, you have discovered some new plants, and you want to gather some information about them and create an exhibition to see which plant is highest rated.
On the first line, you will receive a number n. On the next n lines, you will be given some information about the plants that you have discovered in the format: "{plant}<->{rarity}". Store that information because you will need it later. If you receive a plant more than once, update its rarity.
After that, until you receive the command "Exhibition", you will be given some of these commands:
"Rate: {plant} - {rating}" – add the given rating to the plant (store all ratings)
"Update: {plant} - {new_rarity}" – update the rarity of the plant with the new one
"Reset: {plant}" – remove all the ratings of the given plant
Note: If any given plant name is invalid, print "error"
After the command "Exhibition", print the information that you have about the plants in the following format:
"Plants for the exhibition:
- {plant_name1}; Rarity: {rarity}; Rating: {average_rating}
- {plant_name2}; Rarity: {rarity}; Rating: {average_rating}
…
- {plant_nameN}; Rarity: {rarity}; Rating: {average_rating}"
The average rating should be formatted to the second decimal place.
### Input / Constraints
You will receive the input as described above
JavaScript: you will receive a list of strings
### Output
Print the information about all plants as described above

# Problem - Counter-Strike
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2305#0.

Write a program that keeps track of every won battle against an enemy. You will receive initial energy. Afterward, you will start receiving the distance you need to reach an enemy until the "End of battle" command is given, or you run out of energy.
The energy you need for reaching an enemy is equal to the distance you receive. Each time you reach an enemy, you win a battle, and your energy is reduced. Otherwise, if you don't have enough energy to reach an enemy, end the program and print: "Not enough energy! Game ends with {count} won battles and {energy} energy".
Every third won battle increases your energy with the value of your current count of won battles.
Upon receiving the "End of battle" command, print the count of won battles in the following format:
"Won battles: {count}. Energy left: {energy}" 
### Input / Constraints
On the first line, you will receive initial energy – an integer [1-10000].
On the following lines, you will be receiving the distance of an enemy – an integer [1-10000]
### Output
The description contains the proper output messages for each case and the format they should be printed.xsd

# Problem - Shoot for the Win
Write a program that helps you keep track of your shot targets. You will receive a sequence with integers, separated by a single space, representing targets and their value. Afterward, you will be receiving indices until the "End" command is given, and you need to print the targets and the count of shot targets.
Every time you receive an index, you need to shoot the target on that index, if it is possible. 
Every time you shoot a target, its value becomes -1, and it is considered shot. Along with that, you also need to:
Reduce all the other targets, which have greater values than your current target, with its value. 
Increase all the other targets, which have less than or equal value to the shot target, with its value.
Keep in mind that you can't shoot a target, which is already shot. You also can't increase or reduce a target, which is considered shot.
When you receive the "End" command, print the targets in their current state and the count of shot targets in the following format:
"Shot targets: {count} -> {target1} {target2}… {targetn}"
### Input / Constraints
On the first line of input, you will receive a sequence of integers, separated by a single space – the targets sequence.
On the following lines, until the "End" command, you be receiving integers each on a single line – the index of the target to be shot.
### Output
The format of the output is described above in the problem description.

# Problem - Moving Target
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2305#2.

You are at the shooting gallery again, and you need a program that helps you keep track of moving targets. On the first line, you will receive a sequence of targets with their integer values, split by a single space. Then, you will start receiving commands for manipulating the targets until the "End" command. The commands are the following:
### "Shoot {index} {power}"
Shoot the target at the index if it exists by reducing its value by the given power (integer value). 
Remove the target if it is shot. A target is considered shot when its value reaches 0.
### "Add {index} {value}"
Insert a target with the received value at the received index if it exists. 
If not, print: "Invalid placement!"
### "Strike {index} {radius}"
Remove the target at the given index and the ones before and after it depending on the radius.
If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
### "End"
Print the sequence with targets in the following format and end the program:
"{target1}|{target2}…|{targetn}"
### Input / Constraints
On the first line, you will receive the sequence of targets – integer values [1-10000].
On the following lines, until the "End" will be receiving the command described above – strings.
There will never be a case when the "Strike" command would empty the whole sequence.
### Output
Print the appropriate message in case of any command if necessary.
In the end, print the sequence of targets in the format described above.

# Problem1 - Secret Chat
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#0.

You have plenty of free time, so you decide to write a program that conceals and reveals your received messages. Go ahead and type it in!
On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is given, you will receive strings with instructions for different operations that need to be performed upon the concealed message to interpret it and reveal its actual content. There are several types of instructions, split by ":|:"
### "InsertSpace:|:{index}":
Inserts a single space at the given index. The given index will always be valid.
### "Reverse:|:{substring}":
If the message contains the given substring, cut it out, reverse it and add it at the end of the message. 
If not, print "error".
This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
### "ChangeAll:|:{substring}:|:{replacement}":
Changes all occurrences of the given substring with the replacement text.
### Input / Constraints
On the first line, you will receive a string with a message.
On the following lines, you will be receiving commands, split by ":|:".
### Output
After each set of instructions, print the resulting string. 
After the "Reveal" command is received, print this message:
"You have a new text message: {message}"

# Problem - Mirror words
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#1.

The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there. It`s different and a lot more fun! You, of course, are a participant, and you are eager to show the competition that you are the best, so go ahead, learn the rules and win!
On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden word pairs, read them, and mark the ones that are mirror images of each other.
First of all, you have to extract the hidden word pairs. Hidden word pairs are:
- Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
- At least 3 characters long each (without the surrounding symbols)
- Made up of letters only
#### If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a match, and you have to store them somewhere. Examples of mirror words: 
#### #Part##traP# @leveL@@Level@ #sAw##wAs#
- If you don`t find any valid pairs, print: "No word pairs found!"
- If you find valid pairs print their count: "{valid pairs count} word pairs found!"
- If there are no mirror words, print: "No mirror words!"
- If there are mirror words print:
"The mirror words are:
{wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
### Input / Constraints
You will recive a string.
### Output
Print the proper output messages in the proper cases as described in the problem description.
If there are pairs of mirror words, print them in the end, each pair separated by ", ".
Each pair of mirror word must be printed with " <=> " between the words.

# Problem - Need for Speed III
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#2.

You have just bought the latest and greatest computer game – Need for Seed III. Pick your favorite cars and drive them all you want! We know that you can't wait to start playing.
On the first line of the standard input, you will receive an integer n – the number of cars that you can obtain. On the next n lines, the cars themselves will follow with their mileage and fuel available, separated by "|" in the following format:
"{car}|{mileage}|{fuel}"
Then, you will be receiving different commands, each on a new line, separated by " : ", until the "Stop" command is given:
### "Drive : {car} : {distance} : {fuel}":
You need to drive the given distance, and you will need the given fuel to do that. If the car doesn't have enough fuel, print: "Not enough fuel to make that ride"
If the car has the required fuel available in the tank, increase its mileage with the given distance, decrease its fuel with the given fuel, and print: 
"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed."
You like driving new cars only, so if a car's mileage reaches 100 000 km, remove it from the collection(s) and print: "Time to sell the {car}!"
### "Refuel : {car} : {fuel}":
Refill the tank of your car. 
Each tank can hold a maximum of 75 liters of fuel, so if the given amount of fuel is more than you can fit in the tank, take only what is required to fill it up. 
Print a message in the following format: "{car} refueled with {fuel} liters"
### "Revert : {car} : {kilometers}":
Decrease the mileage of the given car with the given kilometers and print the kilometers you have decreased it with in the following format:
"{car} mileage decreased by {amount reverted} kilometers"
If the mileage becomes less than 10 000km after it is decreased, just set it to 10 000km and 
DO NOT print anything.
Upon receiving the "Stop" command, you need to print all cars in your possession in the following format:
"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt."
### Input/Constraints
The mileage and fuel of the cars will be valid, 32-bit integers, and will never be negative.
The fuel and distance amounts in the commands will never be negative.
The car names in the commands will always be valid cars in your possession.
### Output
All the output messages with the appropriate formats are described in the problem description.

# Problem - Guinea Pig
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2031#0.

Merry has a guinea pig named Puppy, that she loves very much. Every month she goes to the nearest pet store and buys him everything he needs – food, hay, and cover.
On the first three lines, you will receive the quantity of food, hay, and cover, which Merry buys for a month (30 days). On the fourth line, you will receive the guinea pig's weight.
Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, then gives it a certain amount of hay equal to 5% of the rest of the food. On every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight.
Calculate whether the quantity of food, hay, and cover, will be enough for a month.
If Merry runs out of food, hay, or cover, stop the program!
### Input
- On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
- On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
- On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
- On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]
### Output
- If the food, the hay, and the cover are enough, print:
"Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
- If one of the things is not enough, print:
"Merry must go to the pet store!"
The output values must be formatted to the second decimal place!

#1. Problem - Shopping List
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2031#1.

It's the end of the week, and it is time for you to go shopping, so you need to create a shopping list first.
### Input
You will receive an initial list with groceries separated by an exclamation mark "!".
After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
- "Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
- "Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.
- "Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. Otherwise, skip this command.
- "Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of the list. Otherwise, skip this command.
### Constraints
There won't be any duplicate items in the initial list
### Output
Print the list with all the groceries, joined by ", ":
"{firstGrocery}, {secondGrocery}, … {nthGrocery}"

# Problem - Heart Delivery
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2031#2.

Valentine's day is coming, and Cupid has minimal time to spread some love across the neighborhood. Help him with his mission!
You will receive a string with even integers, separated by a "@" - this is our neighborhood. After that, a series of Jump commands will follow until you receive "Love!". Every house in the neighborhood needs a certain number of hearts delivered by Cupid so it can celebrate Valentine's day. The integers in the neighborhood indicate those needed hearts.
Cupid starts at the position of the first house (index 0) and must jump by a given length. The jump commands will be in this format: "Jump {length}". 
Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2: 
- If the needed hearts for a certain house become equal to 0, print on the console "Place {house_index} has Valentine's day." 
- If Cupid jumps to a house where the needed hearts are already 0, print on the console "Place {house_index} already had Valentine's day."
- Keep in mind that Cupid can have a larger jump length than the size of the neighborhood, and if he does jump outside of it, he should start from the first house again (index 0)
For example, we are given this neighborhood: 6@6@6. Cupid is at the start and jumps with a length of 2. He will end up at index 2 and decrease the needed hearts by 2: [6, 6, 4]. Next, he jumps again with a length of 2 and goes outside the neighborhood, so he goes back to the first house (index 0) and again decreases the needed hearts there: [4, 6, 4].
### Input
- On the first line, you will receive a string with even integers separated by "@" – the neighborhood and the number of hearts for each house.
- On the next lines, until "Love!" is received, you will be getting jump commands in this format: "Jump {length}".
### Output
In the end, print Cupid's last position and whether his mission was successful or not:
- "Cupid's last position was {last_position_index}."
- If each house has had Valentine's day, print: 
"Mission was successful."
- If not, print the count of all houses that didn't celebrate Valentine's Day:
"Cupid has failed {houseCount} places."
### Constraints
- The neighborhood's size will be in the range [1…20]
- Each house will need an even number of hearts in the range [2 … 10]
- Each jump length will be an integer in the range [1 … 20]

# Problem - Password Reset
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#0.

Yet again, you have forgotten your password. Naturally, it's not the first time this has happened. Actually, you got so tired of it that you decided to help yourself with an intelligent solution.
Write a password reset program that performs a series of commands upon a predefined string. First, you will receive a string, and afterward, until the command "Done" is given, you will be receiving strings with commands split by a single space. The commands will be the following:
- "TakeOdd"
 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
- "Cut {index} {length}"
Gets the substring with the given length starting from the given index from the password and removes its first occurrence, then prints the password on the console.
The given index and the length will always be valid.
- "Substitute {substring} {substitute}"
If the raw password contains the given substring, replaces all of its occurrences with the substitute text given and prints the result.
If it doesn't, prints "Nothing to replace!".
### Input
You will be receiving strings until the "Done" command is given.
### Output
After the "Done" command is received, print:
- "Your password is: {password}"
### Constraints
The indexes from the "Cut {index} {length}" command will always be valid.

# Problem 2 - Fancy Barcodes
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#1.

Your first task is to determine if the given sequence of characters is a valid barcode or not. 
Each line must not contain anything else but a valid barcode. A barcode is valid when:
- It is surrounded by a "@" followed by one or more "#"
- It is at least 6 characters long (without the surrounding "@" or "#")
- It starts with a capital letter
- It contains only letters (lower and upper case) and digits
- It ends with a capital letter
Examples of valid barcodes: @###Che46sE@##, @#FreshFisH@#, @###Brea0D@###, @##Che46sE@##
Examples of invalid barcodes: ##InvaliDiteM##, @InvalidIteM@, @#Invalid_IteM@#
Next, you have to determine the product group of the item from the barcode. The product group is obtained by concatenating all the digits found in the barcode. If there are no digits present in the barcode, the default product group is "00".
Examples:  
- @#FreshFisH@# -> product group: 00
- @###Brea0D@### -> product group: 0
- @##Che4s6E@## -> product group: 46
### Input
On the first line, you will be given an integer n – the count of barcodes that you will be receiving next. 
On the following n lines, you will receive different strings.
### Output
For each barcode that you process, you need to print a message.

If the barcode is invalid:
- "Invalid barcode"

If the barcode is valid:
- "Product group: {product group}"

# Problem - Heroes of Code and Logic VII
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2303#0.

You got your hands on the most recent update on the best MMORPG of all time – Heroes of Code and Logic. You want to play it all day long! So cancel all other arrangements and create your party!
On the first line of the standard input, you will receive an integer n – the number of heroes that you can choose for your party. On the next n lines, the heroes themselves will follow with their hit points and mana points separated by a single space in the following format: 
#### "{hero name} {HP} {MP}"
- HP stands for hit points and MP for mana points
- a hero can have a maximum of 100 HP and 200 MP
After you have successfully picked your heroes, you can start playing the game. You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given. 
There are several actions that the heroes can perform:
#### "CastSpell – {hero name} – {MP needed} – {spell name}"
If the hero has the required MP, he casts the spell, thus reducing his MP. Print this message: 
- "{hero name} has successfully cast {spell name} and now has {mana points left} MP!"
If the hero is unable to cast the spell print:
- "{hero name} does not have enough MP to cast {spell name}!"
#### "TakeDamage – {hero name} – {damage} – {attacker}"
Reduce the hero HP by the given damage amount. If the hero is still alive (his HP is greater than 0) print:
- "{hero name} was hit for {damage} HP by {attacker} and now has {current HP} HP left!"
If the hero has died, remove him from your party and print:
- "{hero name} has been killed by {attacker}!"
#### "Recharge – {hero name} – {amount}"
The hero increases his MP. If it brings the MP of the hero above the maximum value (200), MP is increased to 200. (the MP can't go over the maximum value).
 Print the following message:
- "{hero name} recharged for {amount recovered} MP!"
#### "Heal – {hero name} – {amount}"
The hero increases his HP. If a command is given that would bring the HP of the hero above the maximum value (100), HP is increased to 100 (the HP can't go over the maximum value).
 Print the following message:
 - "{hero name} healed for {amount recovered} HP!"
### Input
- On the first line of the standard input, you will receive an integer n
- On the following n lines, the heroes themselves will follow with their hit points and mana points separated by a space in the following format
- You will be receiving different commands, each on a new line, separated by " – ", until the "End" command is given
### Output
Print all members of your party who are still alive, in the following format (their HP/MP need to be indented 2 spaces):
"{hero name}
- HP: {current HP}
- MP: {current MP}"
### Constraints
- The starting HP/MP of the heroes will be valid, 32-bit integers will never be negative or exceed the respective limits.
- The HP/MP amounts in the commands will never be negative.
- The hero names in the commands will always be valid members of your party. No need to check that explicitly.

# Problem - Bonus Scoring System
Create a program that calculates bonus points for each student enrolled in a course. On the first line, you are going to receive the number of the students. On the second line, you will receive the total number of lectures in the course. The course has an additional bonus, which you will receive on the third line. On the following lines, you will be receiving the count of attendances for each student.
The bonus is calculated with the following formula:
##### {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
Find the student with the maximum bonus and print them, along with his attendances, in the following format:
##### "Max Bonus: {max bonus points}."
##### "The student has attended {student attendances} lectures."
Round the bonus points at the end to the nearest larger number.
### Input / Constrains
- On the first line, you are going to receive the number of the students – an integer in the range [0…50]
- On the second line, you will receive the number of the lectures – an integer number in the range [0...50].
- On the third line, you will receive the additional bonus – an integer number in the range [0….100].
- On the following lines, you will be receiving the attendance of each student.
- There will never be students with equal bonuses.
### Output
Print the maximum bonus points and the attendances of the given student, rounded to the nearest larger number, scored by a student in this course in the format described above.

# Problem - Mu Online
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2028#1.

You have initial health 100 and initial bitcoins 0. You will be given a string representing the dungeon's rooms. Each room is separated with '|' (vertical bar): "room1|room2|room3…"
Each room contains a command and a number, separated by space. The command can be:
##### "potion"
- You are healed with the number in the second part. But your health cannot exceed your initial health (100).
- First print: "You healed for {amount} hp."
- After that, print your current health: "Current health: {health} hp."
##### "chest"
- You've found some bitcoins, the number in the second part.
- Print: "You found {amount} bitcoins."
##### In any other case, you are facing a monster, which you will fight. The second part of the room contains the attack of the monster. You should remove the monster's attack from your health. 
- If you are not dead (health <= 0), you've slain the monster, and you should print: "You slayed {monster}."
- If you've died, print "You died! Killed by {monster}." and your quest is over. Print the best room you've manage to reach: "Best room: {room}"
##### f you managed to go through all the rooms in the dungeon, print on the following three lines: 
- "You've made it!"
- "Bitcoins: {bitcoins}"
- "Health: {health}"
### Input / Constraints
You receive a string representing the dungeon's rooms, separated with '|' (vertical bar): "room1|room2|room3…".
### Output
Print the corresponding messages described above.

# Problem -3. Inventory
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2028#2.

As a young traveler, you gather items and craft new items.
### Input / Constraints
You will receive a journal with some collecting items, separated with a comma and a space (", "). After that, until receiving "Craft!" you will be receiving different commands split by " - ":
- "Collect - {item}" - you should add the given item to your inventory. If the item already exists, you should skip this line.
- "Drop - {item}" - you should remove the item from your inventory if it exists.
- "Combine Items - {old_item}:{new_item}" - you should check if the old item exists. If so, add the new item after the old one. Otherwise, ignore the command.
- "Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
### 
After receiving "Craft!" print the items in your inventory, separated by ", ".

# Problem - Activation Keys
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#0.

You are about to make some good money, but first, you need to think of a way to verify who paid for your product and who didn't. You have decided to let people use the software for a free trial period and then require an activation key to continue using the product. Before you can cash out, the last step is to design a program that creates unique activation keys for each user. So, waste no more time and start typing!
The first line of the input will be your raw activation key. It will consist of letters and numbers only. 
After that, until the "Generate" command is given, you will be receiving strings with instructions for different operations that need to be performed upon the raw activation key.
There are several types of instructions, split by ">>>":
##### "Contains>>>{substring}":
- If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
- Otherwise, prints: "Substring not found!"
##### "Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
- Changes the substring between the given indices (the end index is exclusive) to upper or lower case and then prints the activation key.
- All given indexes will be valid.
##### "Slice>>>{startIndex}>>>{endIndex}":
- Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
- Both indices will be valid.
### Input
The first line of the input will be a string consisting of letters and numbers only. 
After the first line, until the "Generate" command is given, you will be receiving strings.
### Output
After the "Generate" command is received, print:
"Your activation key is: {activation key}"

# Problem - Emoji Detector
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#1.

Your task is to write a program that extracts emojis from a text and find the threshold based on the input.
You have to get your cool threshold. It is obtained by multiplying all the digits found in the input.  The cool threshold could be a huge number, so be mindful.
An emoji is valid when:
- It is surrounded by 2 characters, either "::" or "**"
- It is at least 3 characters long (without the surrounding symbols)
- It starts with a capital letter
- Continues with lowercase letters only
Examples of valid emojis: ::Joy::, **Banana**, ::Wink::
Examples of invalid emojis: ::Joy**, ::fox:es:, **Monk3ys**, :Snak::Es::
You need to count all valid emojis in the text and calculate their coolness. The coolness of the emoji is determined by summing all the ASCII values of all letters in the emoji. 
Examples: ::Joy:: - 306, **Banana** - 577, ::Wink:: - 409
You need to print the result of the cool threshold and, after that to take all emojis out of the text, count them and print only the cool ones on the console.
### Input
On the single input, you will receive a piece of string. 
### Output
- On the first line of the output, print the obtained Cool threshold in the format:
> "Cool threshold: {coolThresholdSum}"
- On the following line, print the count of all emojis found in the text in format:
 "{countOfAllEmojis} emojis found in the text. The cool ones are:
> 
> {cool emoji 1}
> 
> {cool emoji 2}
> 
> …
> {cool emoji N}"
> 
### Constrains
There will always be at least one digit in the text!

# Problem - P!rates
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2302#2.

Anno 1681. The Caribbean. The golden age of piracy. You are a well-known pirate captain by the name of Jack Daniels. Together with your comrades Jim (Beam) and Johnny (Walker), you have been roaming the seas, looking for gold and treasure… and the occasional killing, of course. Go ahead, target some wealthy settlements and show them the pirate's way!
Until the "Sail" command is given, you will be receiving:
- You and your crew have targeted cities, with their population and gold, separated by "||".
- If you receive a city that has already been received, you have to increase the population and gold with the given values.
After the "Sail" command, you will start receiving lines of text representing events until the "End" command is given. 

Events will be in the following format:
##### "Plunder=>{town}=>{people}=>{gold}"
- You have successfully attacked and plundered the town, killing the given number of people and stealing the respective amount of gold. 
- For every town you attack print this message: "{town} plundered! {gold} gold stolen, {people} citizens killed."
If any of those two values (population or gold) reaches zero, the town is disbanded.
- You need to remove it from your collection of targeted cities and print the following message: "{town} has been wiped off the map!"
There will be no case of receiving more people or gold than there is in the city.
##### "Prosper=>{town}=>{gold}"
- There has been dramatic economic growth in the given city, increasing its treasury by the given amount of gold.
- The gold amount can be a negative number, so be careful. If a negative amount of gold is given, print: "Gold added cannot be a negative number!" and ignore the command.
- If the given gold is a valid amount, increase the town's gold reserves by the respective amount and print the following message: 
"{gold added} gold added to the city treasury. {town} now has {total gold} gold."

### Input
- On the first lines, until the "Sail" command, you will be receiving strings representing the cities with their gold and population, separated by "||"
- On the following lines, until the "End" command, you will be receiving strings representing the actions described above, separated by "=>"
### Output
- After receiving the "End" command, if there are any existing settlements on your list of targets, you need to print all of them, in the following format:
"Ahoy, Captain! There are {count} wealthy settlements to go to:
>
> {town1} -> Population: {people} citizens, Gold: {gold} kg
> 
> {town2} -> Population: {people} citizens, Gold: {gold} kg
> 
>    …
>    
> {town…n} -> Population: {people} citizens, Gold: {gold} kg"
> 
- If there are no settlements left to plunder, print:
> "Ahoy, Captain! All targets have been plundered and destroyed!"

### Constraints
- The initial population and gold of the settlements will be valid 32-bit integers, never negative, or exceed the respective limits.
- The town names in the events will always be valid towns that should be on your list.

# Problem - Black Flag 
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/1773#0.

Pirates are invading the sea, and you're tasked to help them plunder
Create a program that checks if target plunder is reached. First, you will receive how many days the pirating lasts. Then you will receive how much the pirates plunder for a day. Last you will receive the expected plunder at the end.
Calculate how much plunder the pirates manage to gather. Each day they gather the plunder. Keep in mind that they attack more ships every third day and add additional plunder to their total gain, which is 50% of the daily plunder. Every fifth day the pirates encounter a warship, and after the battle, they lose 30% of their total plunder.
If the gained plunder is more or equal to the target, print the following:
"Ahoy! {totalPlunder} plunder gained."
If the gained plunder is less than the target. Calculate the percentage left and print the following:
"Collected only {percentage}% of the plunder."
Both numbers should be formatted to the 2nd decimal place.
### Input
On the 1st line, you will receive the days of the plunder – an integer number in the range [0…100000]
On the 2nd line, you will receive the daily plunder – an integer number in the range [0…50]
On the 3rd line, you will receive the expected plunder – a real number in the range [0.0…10000.0]
### Output
In the end, print whether the plunder was successful or not, following the format described above.
 
# Problem - Treasure Hunt
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/1773#1.

The pirates need to carry a treasure chest safely back to the ship, looting along the way.
Create a program that manages the state of the treasure chest along the way. On the first line, you will receive the initial loot of the treasure chest, which is a string of items separated by a "|".
"{loot1}|{loot2}|{loot3} … {lootn}"
The following lines represent commands until "Yohoho!" which ends the treasure hunt:
##### "Loot {item1} {item2}…{itemn}":
- Pick up treasure loot along the way. Insert the items at the beginning of the chest. 
- If an item is already contained, don't insert it.
##### "Drop {index}":
- Remove the loot at the given position and add it at the end of the treasure chest. 
- If the index is invalid, skip the command.
##### "Steal {count}":
- Someone steals the last count loot items. If there are fewer items than the given count, remove as much as there are. 
- Print the stolen items separated by ", ":
"{item1}, {item2}, {item3} … {itemn}"
In the end, output the average treasure gain, which is the sum of all treasure items length divided by the count of all items inside the chest formatted to the second decimal point:
"Average treasure gain: {averageGain} pirate credits."
If the chest is empty, print the following message:
"Failed treasure hunt."
### Input
- On the 1st line, you are going to receive the initial treasure chest (loot separated by "|")
- On the following lines, until "Yohoho!", you will be receiving commands.
### Output
- Print the output in the format described above.
### Constraints
- The loot items will be strings containing any ASCII code.
- The indexes will be integers in the range [-200…200]
- The count will be an integer in the range [1….100]

# Problem - Man-O-War
Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/1773#2.

The pirates encounter a huge Man-O-War at sea. 
Create a program that tracks the battle and either chooses a winner or prints a stalemate. On the first line, you will receive the status of the pirate ship, which is a string representing integer sections separated by ">". On the second line, you will receive the same type of status, but for the warship: 
"{section1}>{section2}>{section3}… {sectionn}"
On the third line, you will receive the maximum health capacity a section of the ship can reach. 
The following lines represent commands until "Retire":
- "Fire {index} {damage}" - the pirate ship attacks the warship with the given damage at that section. Check if the index is valid and if not, skip the command. If the section breaks (health <= 0) the warship sinks, print the following and stop the program: "You won! The enemy ship has sunken."
- "Defend {startIndex} {endIndex} {damage}" - the warship attacks the pirate ship with the given damage at that range (indexes are inclusive). Check if both indexes are valid and if not, skip the command. If the section breaks (health <= 0) the pirate ship sinks, print the following and stop the program:
"You lost! The pirate ship has sunken."
- "Repair {index} {health}" - the crew repairs a section of the pirate ship with the given health. Check if the index is valid and if not, skip the command. The health of the section cannot exceed the maximum health capacity.
- "Status" - prints the count of all sections of the pirate ship that need repair soon, which are all sections that are lower than 20% of the maximum health capacity. Print the following:
"{count} sections need repair."
In the end, if a stalemate occurs, print the status of both ships, which is the sum of their individual sections, in the following format:
"Pirate ship status: {pirateShipSum}
Warship status: {warshipSum}"
### Input
- On the 1st line, you are going to receive the status of the pirate ship (integers separated by '>')
- On the 2nd line, you are going to receive the status of the warship
- On the 3rd line, you will receive the maximum health a section of a ship can reach.
- On the following lines, until "Retire", you will be receiving commands.
### Output
- Print the output in the format described above.
### Constraints
- The section numbers will be integers in the range [1….1000]
- The indexes will be integers [-200….200]
- The damage will be an integer in the range [1….1000]
- The health will be an integer in the range [1….1000]
