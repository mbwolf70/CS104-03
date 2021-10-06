average = 0
total = 0
howManyEntered = 0
howMany = int(input('How many test scores would you like to average?'))
while howManyEntered < howMany:
    testScore = int(input('Enter test score:'))
    total += testScore
    howManyEntered += 1
Average = total/howMany
print ('The average for the test scores you entered is:')
print (average)
    
