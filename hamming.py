import numpy as np

## Defines variables for block length, redundancy, and message length.

redundancy = 4

blocklength = pow(2,redundancy) - 1
messagelength = blocklength - redundancy 

print("Hamming(" + str(blocklength) + "," + str(messagelength) + ")")

messageString = "10101010101"

messageVec = [0] * len(messageString)

indices=0

# Build string vector

for n in messageString:
    messageVec[indices] = int(messageString[indices:indices+1])
    #print(messageVec[indices])
    indices+=1
indices=0

## Following code encodes our message within hamming code.

positionVec = [0] * redundancy # Creates empty parity vector

for n in positionVec:
    positionVec[indices] = pow(2,indices)
    #print(str(positionVec[indices])+"\n")
    indices+=1
indices=0    

encodedVec = [0] * blocklength

parityTicker = 0
messageTicker = 0

for n in encodedVec:
    if indices+1 == pow(2,parityTicker):
        encodedVec[indices] = 9 #redundancy #positionVec[parityTicker]
        parityTicker+=1
        indices+=1
    else:
        encodedVec[indices] = messageVec[messageTicker]
        messageTicker+=1
        indices+=1

indices=0

### Replace 9's with parity bit

encodeCounter = 0

while(indices < redundancy):
    digitAccumulator = 0
    encodeCounter = pow(2,indices) - 1
    digitParityPosition = positionVec[indices] - 1
    parityAmount = positionVec[indices]
    OnOff = 1
############################
    repetitionCheck = 0    
    while(encodeCounter < len(encodedVec)):
        if OnOff == 1:
            if (repetitionCheck < parityAmount):
                digitAccumulator += encodedVec[encodeCounter]
                repetitionCheck += 1
                encodeCounter+=1
            else:
                OnOff = 0
                repetitionCheck = 0
            
        else: #OnOff == 0
            if (repetitionCheck < parityAmount):
                repetitionCheck += 1
                encodeCounter += 1
            else:
                OnOff = 1
                repetitionCheck = 0

#############################
    encodedVec[digitParityPosition] = (digitAccumulator-9)%2
    indices+=1
indices=0


###
for n in encodedVec:
    print(str(encodedVec[indices])+ " ", end = '')
    indices+=1
indices=0

print()

