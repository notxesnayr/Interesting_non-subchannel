def Fibonacci_Sequence(x):
    def ret(y):
        return y
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == -1:
        return -1
    if x == -2 :
        return -1
    elif x < -2:
        return ((-1)**(x+1))*Fibonacci_Sequence(-x)
        
    else:
        return Fibonacci_Sequence(x-1) + Fibonacci_Sequence(x-2)
for x in range(-20,20):#moving from ~-1.618 to ~1.618
    if x > 0:
        print(Fibonacci_Sequence(x+1)/Fibonacci_Sequence(x))
    elif x < -1:
        print(Fibonacci_Sequence(x)/Fibonacci_Sequence(x+1))
    

