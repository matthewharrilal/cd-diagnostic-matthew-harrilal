
# Problem 6 Fizzbuzz Psueudocode

# to start this problem off essentially what has to happen is that a function has to be created that takes in the arguments start and end.
# Then what occurs is to print every number inclusively from start to end what has to happen is that a for loop has to be created to iterate over the items in the start and end argument labels, however there are conditions that have to be satisified such as if a number is evenly divisible by 3, print the word “fizz” instead of the number.  If a number is evenly divisible by 5, print “buzz” instead of the number.  If a number is evenly divisible by both 3 and 5, print “fizzbuzz” instead of the number.
#Therefore we have to implement a conditional flow, to start of this conditional flow a if statement would start off declaring if a number is evenly divisible by 3, print the word “fizz” instead of the number. If that condition is not satisfied hit the elif statement and what that basically will state that if the f a number is evenly divisible by 5, print “buzz” instead of the number. If that condition ends up not being satisfied what we want to happen is that we want  If a number is evenly #divisible by both 3 and 5, print “fizzbuzz” instead of the number. To essentially check if these numbers are evenly divisible what we would have  to do is atually when these numbers are divided by the the corresponding values if the remainder is zero or not, for example if the number is 15 and the number is being divided is odd and gives a remainder of zero we obviously know the number is odd due to basic mathematical principles

def fizzbuzz(start, end):
    for number in start and end:
        if number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("buzz")
        elif number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        else:
            print(number)

    fizzbuzz(4, 9)
