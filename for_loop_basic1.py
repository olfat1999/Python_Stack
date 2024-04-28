# Basic - Print all integers from 0 to 150.
for i in range(1, 150):
    print(i)
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)
# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum_of_odds = sum(range(1, 500001, 2))
print(sum_of_odds)
# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)
# Flexible Counter
lowNum = 4
highNum = 12
mult = 2
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)