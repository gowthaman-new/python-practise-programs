# THIS PROGRAM IS ROBUST. YOU CAN CHANGE THE slabRange & slabCalculation VALUES. YOU CAN ALSO ADD MORE RANGES IF YOU NEED 
slabRange = [100, 200, 300, 300]
slabCalculation = [1, 2, 3, 5]

# Calculates the value of index [0] for slabRange & slabCalculation
def initAmountCalculation():
    return (slabRange[0] * slabCalculation[0])

# Calculates the value of all indices for slabRange & slabCalculation except the first and the last index
def midAmountCalculation():
    sum = 0
    for i in range(1, len(slabRange) - 1):
        sum = sum + ((slabRange[i] - slabRange[i-1]) * slabCalculation[i])
    return sum

# Calculates only the last index [slabRange & slabCalculation] value
def endAmountCalculation():
    return ((units - slabRange[len(slabRange)-1]) * slabCalculation[len(slabRange)-1])

# Calculates all the index [slabRange & slabCalculation] values except first & last index. This calculation is based upon the index value
def recurringDifferenceCalculation(index):
    result = 0
    for i in range(1, index):
        result = result + ((slabRange[i] - slabRange[i-1]) * slabCalculation[i])
    return result

# Calculates the last index [slabRange & slabCalculation] value & its based upon the index value
def calcAmountWithInRange(index):
    return (units - slabRange[index-1]) * slabCalculation[index]

# Main Method which calculates the EB Bill
def ebBillCalculation(units):
    if len(slabCalculation) != len(slabRange):
        return "length of slabRange & slabCalculation is not matching. So exiting..."

    if (units <= slabRange[0]):
        return units * slabCalculation[0]

    if (len(slabRange) >= 2):
        if (units <= slabRange[1]):
            return (initAmountCalculation() + calcAmountWithInRange(1))

    if (units > slabRange[len(slabRange)-1]):
        return (initAmountCalculation() + midAmountCalculation() + endAmountCalculation())

    for i in range(2, len(slabRange)):
        if (units <= slabRange[i]):
            return (initAmountCalculation() + recurringDifferenceCalculation(i) + calcAmountWithInRange(i))

units = 250;
print(ebBillCalculation(units));
