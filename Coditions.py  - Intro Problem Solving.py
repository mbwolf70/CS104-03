temp = 0
while temp != 999:
    temp = int(input('Enter a temp:'))
    print(type(temp))

    if temp == 999:
        print ('program ended')
    elif  temp > 90:
        print ('Wear Shorts')
    elif temp > 70:
        print ('Short sleeves are fine')
    elif temp > 50:
        print ('Wear a jacket')
    elif temp > 32:
        print ('Wear a heavy coat')
    else:
        print ('Stay Inside')
        
