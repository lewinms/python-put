#!/usr/bin/env python
# -*- coding utf-8 -*-
import matplotlib.pyplot as plt

def generation(column,cell,krotka):
    krotka[2] = float(cell)

def effort(column,cell,krotka):
    krotka[0] = float(cell)

def run(column,cell,krotka):
    krotka[1].append(float(cell))

def checkCell(column,cell,krotka):
    switcher = {
        "generation": generation,
        "effort": effort,
    }
    function = switcher.get(column,run)
    function(column,cell,krotka)

def readFile(fileName):
    readFile = open(fileName,"r")
    lines = readFile.readlines();
    readFile.close();
    plotArray = [[]]*3
    for i in range(len(plotArray)):
        plotArray[i] = []
    print(plotArray)
    for i in range(len(lines)):
        if i == 0:
            # print("test")
            columns = lines[i]
            columns = columns.split(",")
        else:
            cells = lines[i].split(',')
            krotka = [0,[],0]
            for j in range(len(cells)):
                # print(cells)
                checkCell(columns[j],cells[j],krotka);
            # krotka[1] = sum(krotka[1])/len(krotka[1])
            # if warunki(krotka) == True:
            plotArray[0].append(krotka[0])
            plotArray[1].append(krotka[1])
            plotArray[2].append(krotka[2])
            # else:
                # print("Warunek nie spełniony")
    return plotArray


def readAllFiles(fileList):
    plotList = []
    for i in range(len(fileList)):
        plotList.append(readFile(fileList[i][0]))
        plotList[-1].append(fileList[i])
    return plotList


def drawPlots(plotList):
    axis1 = plt.subplot(121)
    axis1.set_xlabel("Rozegranych gier (x1000)")
    axis1.set_ylabel("Odsetek wygranych gier [%]")
    axis2 = axis1.twiny()
    axis2.set_xlabel("Pokolenie")
    axis3 = plt.subplot(122)
    maxGeneration = []
    for newPlot in plotList:
        xData = [float(x/1000) for x in newPlot[0]]
        yData = [(sum(x)/len(x))*100 for x in newPlot[1]]
        axis1.plot(xData,yData,color = newPlot[3][1],marker=newPlot[3][2],markevery=25,label=newPlot[3][3])
        maxGeneration = max(maxGeneration,newPlot[2])
    axis1.legend(loc=4)
    part = int(len(maxGeneration)/5)
    maxGeneration.append(maxGeneration[-1]+1)
    axis2.set_xticks(maxGeneration[::part])
    axis1.set_xlim(0,500)
    axis2.set_xlim(0,200)

    # axis3.boxplot(newPlot[1][-1],labels=newPlot[3][3],notch=True,bootstrap=10000)
    axis3.boxplot([[x*100 for x in newPlot[1][-1]] for newPlot in plotList],labels=[newPlot[3][3] for newPlot in plotList],notch=True,bootstrap=10000,showmeans=True,color="b")
    axis3.set_ylim(60,100)
    # plt.savefig('wykresy.png')
    plt.show()
    plt.close()

def main():
    fileList = [["rsel.csv","b","o","1-Evol-RS"],["cel-rs.csv","g","v","1-Coev-RS"],["2cel-rs.csv","r","D","2-Coev-RS"],["cel.csv","k","s","1-Coev"],["2cel.csv",'m',"d","2-Coev"]]
    newPlotList = readAllFiles(fileList)
    drawPlots(newPlotList)


if __name__ == '__main__':
    main()
