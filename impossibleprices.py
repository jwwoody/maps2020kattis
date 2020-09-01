numInputs = int(input())
for i in range(numInputs):
    a, b, t = input().split(' ')
    a = round(100*float(a))
    b = round(100*float(b))
    t = 1+round(float(t), 2)/100

    count = 0
    curval = a

    while curval < b+1:
        pre_tax_price = round(curval / t)
        plusOne = pre_tax_price+1
        nextVal = round((plusOne)*t)
        if nextVal > b:
            count+= b-curval
            break
        else:
            count+= nextVal-curval-1
        curval = nextVal
    print(count)

