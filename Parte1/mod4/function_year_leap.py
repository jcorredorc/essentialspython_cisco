def isYearLeap(year):
#
# coloca tu código aquí
#
    if year > 1582 :
        if year % 4 != 0 :
            print("año comun")
            return False
        elif year % 100 != 0:
            print("bisiesto")
            return True
        elif year % 400 != 0:
            print("comun")
            return False
        else:
            print("bisiestoo") 
            return True        
    else:
        print("No dentro del período del calendario gregoriano")
        return None


testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")