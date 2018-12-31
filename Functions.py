

naira = input("How much in Naira are you converting ")

def dollarconversion(x):
    rate = input("Whats the rate of conversion today: ")
    value = int(x)/int(rate)
    return value

dollarvalue = dollarconversion(naira)
print("The dollar equivalent is " + str(dollarvalue))