# Program that finds the average of elements in a list

def avgs(a):
    tot = 0
    for elem in a:
        tot = tot + elem           

    avg = tot/ len(a)
    return avg

print(avgs([2,3,4]))