# 1 - Biggie Size

def biggieSize(list):
    for i in range(0, len(list), 1):
        if(list[i] > 0):
            list[i] = "big"
    return list


print(biggieSize([-1, 3, 5, -5]))
# [-1, 'big', 'big', -5]


# 2 - Count Positives

def countPos(list):
    count = 0
    for i in range(0, len(list), 1):
        if(list[i] > 0):
            count += 1
    list[len(list) - 1] = count
    return list


print(countPos([-1, 1, 1, 1]))
print(countPos([1, 6, -4, -2, -7, -2]))
# [-1, 1, 1, 3]
# [1, 6, -4, -2, -7, 2]


# 3 - Sum Total

def sumTotal(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum = sum + list[i]
    return sum


print(sumTotal([1, 2, 3, 4]))
print(sumTotal([6, 3, -2]))
# 10
# 7


# 4 - Average

def average(list):
    sum = 0
    for i in range(0, len(list), 1):
        sum = sum + list[i]
    avg = sum / len(list)
    return avg


print(average([1, 2, 3, 4]))
# 2.5


# 5 - Length

def length(list):
    count = 0
    for i in range(0, len(list), 1):
        count += 1
    return count


print(length([37, 2, 1, -9]))
print(length([]))
# 4
# 0


# 6 - Minimum WORK ON THIS ONE MORE

def minimum(list):
    if(len(list) < 1):
        return(False)
    min = list[0]
    for i in range(0, len(list), 1):
        if (list[i] < min):
            min = list[i]
    return min


print(minimum([37, 2, 1, -9]))
print(minimum([]))
# -9
# False


# 7 - Maximum

def maximum(list):
    if(len(list) < 1):
        return(False)
    max = list[0]
    for i in range(0, len(list), 1):
        if (list[i] > max):
            max = list[i]
    return max


print(maximum([37, 2, 1, -9]))
print(maximum([]))
# 37
# False


# 8 - Ultimate Analysis

def ultAnalysis(list):
    sum = 0
    min = list[0]
    max = list[0]
    length = len(list)
    for i in range(0, len(list), 1):
        sum = sum + list[i]
        if(list[i] < min):
            min = list[i]
        if(list[i] > max):
            max = list[i]
    avg = sum / length

    dict = {
        'sumTotal': sum,
        'average': avg,
        'minimum': min,
        'maximum': max,
        'length': length
    }
    return dict


print(ultAnalysis([37, 2, 1, -9]))
# {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4}


# 9 - Reverse List WORK MORE ON THIS

def revList(list):
    for i in range(0, len(list)//2, 1):
        temp = list[i]
        list[i] = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = temp
    return list


print(revList([37, 2, 1, -9]))
# [-9, 1, 2, 37]