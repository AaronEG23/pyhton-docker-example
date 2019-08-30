import constant
import dataManager

from urllib.request import urlopen
from bs4 import BeautifulSoup
 
def proccessHTML(pConnector):
    html                = pConnector.read()
    soup                = BeautifulSoup(html, features="html.parser")
    links               = soup.find_all(True, {'class':['celda17']}) 
    getYearsComplete    = False
    years               = []
    countPerYear        = 0
    day                 = 0
    actualMonth         = -1
    for tag in links:
        value = tag.p.string
        if (getYearsComplete or verifyIfCompleteGetYears(value)):
            getYearsComplete = True
            if (countPerYear < len(years)):
                year = years[countPerYear]
                if (value != None):
                    value = value.replace(",",".")
                    dataManager.insert(year, month, day, value)
                countPerYear = countPerYear + 1
            else:
                countPerYear = 0
                month = getMonthValue(value)
                if (month == actualMonth):
                    day = day + 1
                else:
                    day = 1
                    actualMonth = month
            
        else:
            if (not getYearsComplete):
                years.append(int(value))
                countPerYear = len(years)


def verifyIfCompleteGetYears(pValue):
    if (pValue != None and constant.JANUARY in pValue):
        return True
    else:
        return False

def getMonthValue(pValue):
    out  = constant.ERROR_MONTHVALUE
    for index, month in enumerate(constant.MONTHS):
        if (pValue != None and month in pValue):
            out = index+1
    return out

 
def process():
    try:
        dataManager.prepareDatabase()
        connector = urlopen(constant.URL,timeout=25)
        proccessHTML(connector)
        return True
    except:
        print("Error: timeout")
        return False
