#
#   SEND
# + MORE
# --------
#  MONEY
#
def getnext():
    value = [i for i in range(10)]
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
    
def Check():
    gen = getnext()
    while True:
        # 0~7 for: D E M N O R S Y
        word = gen.next()
        if word: 
            if word[2] > 2: continue
            if (word[0] + word[1]) % 10 != word[7]: continue
            if (word[6]+word[2]+1)/10 != word[2]: continue
            if ((word[6]+word[2])*1000+(word[1]+word[4])*100+(word[3]+word[5])*10+(word[0]+word[1])) == (word[2]*10000+word[4]*1000+word[3]*100+word[1]*10+word[7]):
                print word
        else:
            return
                
if __name__=='__main__':
    Check()