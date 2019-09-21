def convertDecNum(num):

    num2 = num
    startPower = 0
    binSum = ""

    while 2 ** startPower < int(num):
        startPower+=1
        

    while startPower > -1:
        if int(num) - 2**startPower >= 0:
            num = str(int(num) - 2**startPower)
            startPower -=1
            binSum = binSum + "1"
        else:
            binSum = binSum + "0"
            startPower-=1

    while len(binSum) > 0 and binSum[0] != "1":
        binSum = binSum[1::1]

    binSumCopy = binSum

    while (len(binSumCopy))%4 != 0:
        binSumCopy = '0' + binSumCopy

    index = 0
    hexSum = ""
    hexPart1 = ""
    hexPart2 = ""

    while index < len(binSumCopy):
        hexPart1 = binSumCopy[index:index+4]
        if hexPart1 == "0000":
            hexPart2 = "0"

        elif hexPart1 == "0001":
            hexPart2 = "1"

        elif hexPart1 == "0010":
            hexPart2 = "2"

        elif hexPart1 == "0011":
            hexPart2 = "3"

        elif hexPart1 == "0100":
            hexPart2 = "4"

        elif hexPart1 == "0101":
            hexPart2 = "5"

        elif hexPart1 == "0110":
            hexPart2 = "6"

        elif hexPart1 == "0111":
            hexPart2 = "7"

        elif hexPart1 == "1000":
            hexPart2 = "8"

        elif hexPart1 == "1001":
            hexPart2 = "9"

        elif hexPart1 == "1010":
            hexPart2 = "A"

        elif hexPart1 == "1011":
            hexPart2 = "B"

        elif hexPart1 == "1100":
            hexPart2 = "C"

        elif hexPart1 == "1101":
            hexPart2 = "D"

        elif hexPart1 == "1110":
            hexPart2 = "E"

        elif hexPart1 == "1111":
            hexPart2 = "F"


        hexSum = hexSum + hexPart2
        index+=4

    print(num2 + " (decimal) is " + binSum + " in Binary.")
    print(num2 + " (decimal) is " + hexSum + " in Hexadecimal.")
    

def convertHexNum(num):
    index = 0
    binSum = ""
    decSum = 0

    while index != len(num):
        if num[index] == "0":
            binSum = binSum + "0000"
        elif num[index] == "1":
            binSum = binSum + "0001"
        elif num[index] == "2":
            binSum = binSum + "0010"
        elif num[index] == "3":
            binSum = binSum + "0011"
        elif num[index] == "4":
            binSum = binSum + "0100"
        elif num[index] == "5":
            binSum = binSum + "0101"
        elif num[index] == "6":
            binSum = binSum + "0110"
        elif num[index] == "7":
            binSum = binSum + "0111"
        elif num[index] == "8":
            binSum = binSum + "1000"
        elif num[index] == "9":
            binSum = binSum + "1001"
        elif num[index] == "A":
            binSum = binSum + "1010"
        elif num[index] == "B":
            binSum = binSum + "1011"
        elif num[index] == "C":
            binSum = binSum + "1100"
        elif num[index] == "D":
            binSum = binSum + "1101"
        elif num[index] == "E":
            binSum = binSum + "1110"
        elif num[index] == "F":
            binSum = binSum + "1111"

        index+=1


    print(binSum)
    while len(binSum) > 0 and binSum[0] != "1":
        binSum = binSum[1::1]

    if len(binSum) == 0:
        binSum = "0"

        
    index = 0
    index2 = len(binSum)-1

    while index < len(binSum):
        decSum += (int(binSum[index]) * (2**index2))
        index2+= -1
        index+= 1


    print(num + " (hex) is " + binSum + " in binary.")
    print(num + " (hex) is " + str(decSum) + " in decimal")
        
        

def convertBinNum(num):

    decSum = 0
    hexSum = ""
    
    index = 0
    index2 = len(num)-1

    while index < len(num):
        decSum += (int(num[index]) * (2**index2))
        index2+= -1
        index+= 1

    while (len(num))%4 != 0:
        num = '0' + num

    index = 0
    hexPart1 = ""
    hexPart2 = ""

    while index < len(num):
        hexPart1 = num[index:index+4]
        if hexPart1 == "0000":
            hexPart2 = "0"

        elif hexPart1 == "0001":
            hexPart2 = "1"

        elif hexPart1 == "0010":
            hexPart2 = "2"

        elif hexPart1 == "0011":
            hexPart2 = "3"

        elif hexPart1 == "0100":
            hexPart2 = "4"

        elif hexPart1 == "0101":
            hexPart2 = "5"

        elif hexPart1 == "0110":
            hexPart2 = "6"

        elif hexPart1 == "0111":
            hexPart2 = "7"

        elif hexPart1 == "1000":
            hexPart2 = "8"

        elif hexPart1 == "1001":
            hexPart2 = "9"

        elif hexPart1 == "1010":
            hexPart2 = "A"

        elif hexPart1 == "1011":
            hexPart2 = "B"

        elif hexPart1 == "1100":
            hexPart2 = "C"

        elif hexPart1 == "1101":
            hexPart2 = "D"

        elif hexPart1 == "1110":
            hexPart2 = "E"

        elif hexPart1 == "1111":
            hexPart2 = "F"


        hexSum = hexSum + hexPart2
        index+=4

    while len(num) > 0 and num[0] != "1":
        num = num[1::1]


    print(num + " (binary) is " + str(decSum) + " in decimal.")
    print(num + " (binary) is " + hexSum + " in Hexadecimal.")





repeat = True

while repeat:
    userinput = input("Please input your number:   ")

    validType = False

    while not validType:
        print("Is the number you entered a...")
        print("\t1.) Binary Number\n\t2.) Hexadecimal Number\n\t3.) Deciaml Number")
        userType = input("Selection ('1', '2', or '3'):   ")


        if userType == "1":
            convertBinNum(userinput)

        elif userType == "2":
            convertHexNum(userinput)

        elif userType == "3":
            convertDecNum(userinput)

        validType = True

        if userType != "1" and userType != "2" and userType != "3":
            print("ERROR... PLEASE SELECT VALID TYPE OF NUMBER ENTERED")
            validType = False

    repeat = bool(input("Would you like to convert another number?('True'/*Enter*):   "))
    print("\n"*5)
