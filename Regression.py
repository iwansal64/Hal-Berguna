import math
import turtle
from mathfunctionconverter import FunctionConverter

indexTracker = 0

dataArray = []
indexArray = []

sumAllArray = 0
sumAllIndex = 0

minimumAvgError = 3

fillX = input('fill x (auto, custom, leap): ')
difference = 0
if fillX == 'leap':
    difference = int(input('difference : '))
    first = int(input('first number : '))
indexHighestRange, indexLowestRange, highestValue, lowestValue = [0], [0], 0, 0
while True:
    if fillX == "auto":
        index = indexTracker + 1
    elif fillX == "leap":
        index = indexTracker * difference + first
    elif fillX == "custom":
        try:
            index = int(input('masukkan x : '))
            if indexTracker != 0:
                if index <= indexArray[-1]:
                    print(f'harus lebih dari {index}')
                    continue
        except:
            last = input('afkh yakin? (y/n) ')
            if last == 'y':
                break
            elif last == '':
                exit(0)
            else:
                continue

    try:
        data = float(input('masukan data ke-'+str(index)+" : "))
    except:
        last = input('afkh yakin? (y/n) ')
        if last == 'y':
            break
        elif last == '':
            exit(0)
        else:
            continue

    if indexTracker == 0:
        highestValue = data
        lowestValue = data

    dataArray.append(data)
    indexArray.append(index)

    sumAllArray += data
    sumAllIndex += index

    if data > highestValue:
        highestValue = data
        indexHighestRange = [indexTracker]
    elif data < lowestValue:
        lowestValue = data
        indexLowestRange = [indexTracker]
    elif data == highestValue:
        indexHighestRange.append(indexTracker)
    elif data == lowestValue:
        indexLowestRange.append(indexTracker)


    indexTracker += 1


n = len(dataArray)
avgY = sumAllArray / n

SigmaX = 0
SigmaXSquare = 0
for index, i in enumerate(indexArray):
    SigmaXSquare += (i * i)
    SigmaX += i

avgX = SigmaX / n

Xy = []
SigmaY = 0
SigmaXY = 0
for index, i in enumerate(dataArray):
    res = i * indexArray[index]
    SigmaY += i
    SigmaXY += res
    Xy.append(res)


m = ((SigmaXY * n) - (SigmaX * SigmaY)) / (SigmaXSquare * n - (SigmaX * SigmaX))
c = avgY - m * avgX

dataResult = f"{m}x + {c}"
func = FunctionConverter(dataResult)
dataHelper = func.getSimplifiedEquation()
print('Fungsi Regresi : ', dataHelper)
dataResult = []
for index, i in enumerate(indexArray):
    dataResult.append(eval(dataHelper.replace('x', str(i))))

errorArray = []
SigmaError = 0
AvgError = 0
for index, i in enumerate(dataArray):
    j = dataResult[index]
    errorArray.append(round(j - i, 2))
    SigmaError += abs(round(j - i, 2))

AvgError = round(SigmaError / n, 2)
predictSuccessPercent = 100 - (AvgError / minimumAvgError * 100)
predictSuccessPercent = predictSuccessPercent if predictSuccessPercent <= 100 and predictSuccessPercent >= 0 else (100 if predictSuccessPercent > 100 else 0)

print(f"Avg Error = {AvgError}\nSum Error = {SigmaError}\nSuccessful rate = {predictSuccessPercent}%")

highestValueResult, indexHighestResult = 0, [0]
lowestValueResult, indexLowestResult = 0, [0]


lineFit = input("X Line Mode (fit, Follow) : ")

turtle.penup()
width = turtle.window_width()
height = turtle.window_height()


xLineGraph = -(width // 2) + 150
yLineGraph = -(height // 2) + 100
xLength = 600
yLength = 400

turtle.color('white')
turtle.bgcolor('black')

xyLineGraph = (xLineGraph, yLineGraph)



turtle.setx(xLineGraph)
turtle.sety(yLineGraph)
turtle.pendown()
turtle.setheading(90)
turtle.forward(yLength)
turtle.penup()

turtle.setx(xLineGraph)
turtle.sety(yLineGraph)
turtle.pendown()
turtle.setheading(0)
turtle.forward(xLength)
turtle.penup()

gapY = []
gapX = []

stepsY = round(yLength / highestValue, 2)
stepsX = round(xLength / indexArray[-1], 2)

#Setup
turtle.setheading(90)
turtle.goto(xyLineGraph)
turtle.shape('square')
turtle.shapesize(1, 0.1)
turtle.speed(10)


for i in range(math.ceil(highestValue)):
    turtle.forward(stepsY)
    gapY.append(turtle.pos())
    turtle.stamp()
    turtle.left(90)
    turtle.forward(10)
    turtle.write(i + 1)
    turtle.backward(10)
    turtle.right(90)

turtle.setheading(0)
turtle.goto(xyLineGraph)
turtle.shape('square')
for i in range(1, round(highestValue * xLength / yLength) if lineFit == 'follow' else (indexArray[-1] + 1)):
    if lineFit == 'follow':
        turtle.forward(stepsY)
    else:
        turtle.forward(stepsX)
    

    gapX.append(turtle.pos())
    turtle.stamp()
    if i in indexArray:
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(10)
        turtle.write(i)
        turtle.backward(10)
        turtle.left(90)
        turtle.backward(10)

turtle.goto(xyLineGraph)
turtle.speed(5)
turtle.shape('circle')
turtle.shapesize(0.5, 0.5)

for i in range(0, n):
    if i == 0:
        turtle.penup()
    elif i == 1:
        turtle.pendown()

    turtle.color('white')
    turtle.goto(((stepsY if lineFit == "follow" else stepsX) * indexArray[i] + xLineGraph, (dataArray[i] * stepsY) + yLineGraph))

    if i in indexHighestRange:
        turtle.color('green')
    elif i in indexLowestRange:
        turtle.color('red')
    else:
        turtle.color('blue')

        
    turtle.stamp()

turtle.penup()
turtle.goto(xyLineGraph)
turtle.shapesize(0.2, 0.2)
for i in range(0, n):
    if i == 0:
        turtle.penup()
    elif i == 1:
        turtle.pendown()

    turtle.color('green')
    turtle.goto(((stepsY if lineFit == "follow" else stepsX) * indexArray[i] + xLineGraph, (dataResult[i] * stepsY) + yLineGraph))

    if i in indexHighestResult:
        turtle.color('green')
    elif i in indexLowestResult:
        turtle.color('red')
    else:
        turtle.color('blue')

        
    turtle.stamp()

while True:
    try:
        data = int(input('masukkan nilai x untuk prediksi : '))
    except:
        data = ''
        
    if data == '':
        exit(0)
    else:
        res = eval(dataHelper.replace('x', str(data)))
        print('result :', res)
        if data in indexArray:
            print('error / difference : '+str(errorArray[indexArray.index(data)]))



