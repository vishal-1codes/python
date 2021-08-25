#PART1
#If you’d like to print a variable that is an integer, you can “pad” it with zeros using %02d. 
# The 0 means “pad with zeros”, the 2 means to pad to 2 characters wide, 
# the d means the number is a signed integer (can be positive or negative).

string_1 = "Camelot"
string_2 = "place"

print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

#PART2
#Remember, we used the % operator to replace the %s placeholders with the variables in parentheses.
name = "Alex"
quest = "Teaching Python"
color = "Blue"

print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))