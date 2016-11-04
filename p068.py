# -*- coding: utf-8 -*
    
def getnext():
    value = [i for i in range(1,11)]
    yield value
    N = len(value)
    while True:
        i = N - 1
        while value[i - 1] >= value[i]:
            i -= 1
            if i == 0: 
                yield None
                return              # Now array of value is the max

        j = N
        while value[j - 1] <= value[i - 1]:
            j -= 1

        swap(value, i - 1, j - 1)
        print value
        i += 1
        j = N
        while i < j:
            swap(value, i - 1, j - 1)
            i += 1
            j -= 1

        yield value

def swap(value, i, j):
    temp     = value[i]
    value[i] = value[j]
    value[j] = temp

def fivegonring(array):
    if  array[1] == 10 or
        array[2] == 10 or
        array[4] == 10 or
        array[8] == 10:
        return False
    
    if  array[0] > array[3] or
        array[0] > array[5] or
        array[0] > array[7] or
        array[0] > array[9]:
        return False
    
    if array[0] + array[1] + array[2] != array[3] + array[2] + array[4]:
        return False
    if array[0] + array[1] + array[2] != array[5] + array[4] + array[6]:
        return False
    if array[0] + array[1] + array[2] != array[7] + array[6] + array[8]:
        return False
    if array[0] + array[1] + array[2] != array[9] + array[8] + array[1]:
        return False
        
    return True
        
if __name__ == '__main__':
    gen = getnext()
    while True:
        array = gen.next()
        while not array: break
        