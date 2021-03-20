import random


def computer_choise():
    '''Computer randomly choose number from 1 to 100. Function dont need arguments.'''
    number = random.randint(1,101)
    return number


def gues_number():
    '''Function finding number that was randomly chosen by computer. Dont need arguments.
    
    Function return "count" - iterations used for searching.
    
    '''
    
    number = computer_choise()

    count = 0
    highrange = 101
    medium = 50
    lowrange = 0
    
    while medium != number:
        count+=1
        if medium > number:
            highrange = medium
        else:
            lowrange =  medium
        medium = lowrange + (highrange-lowrange)//2    
    return count 


def score_count():
    '''Function finding count's mean.  Function return mean. Dont need arguments.'''
    totalcounts = []
    for x in range(1000):
        x = gues_number()
        totalcounts.append(x)
        
    mean = sum(totalcounts)//1000
    print (f"Среднее число попыток равно: {mean}.")
    return mean



score_count()    
    

