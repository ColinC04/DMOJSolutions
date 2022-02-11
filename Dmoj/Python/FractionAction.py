def greatestCommonDenominator(numerator, denominator):
    if (denominator == 0):
        return numerator
    else:
        return greatestCommonDenominator(denominator, numerator%denominator)


num1 = int(input())
num2 = int(input())

quotient = num1 // num2
remainderNumerator = (num1%num2) 
remainderDenominator = num2

#Find the reduced fraction of the remainder
gcd = greatestCommonDenominator(remainderNumerator, remainderDenominator)
reducedNumerator , reducedDenominator = remainderNumerator / gcd, remainderDenominator / gcd

reducedNumerator, reducedDenominator = int(reducedNumerator), int(reducedDenominator)

if quotient == 0:
    print(str(reducedNumerator) + "/" + str(reducedDenominator))

elif reducedNumerator == 0:
    print(str(quotient))

else:
    print(str(quotient) + " " + str(reducedNumerator) + "/" + str(reducedDenominator))