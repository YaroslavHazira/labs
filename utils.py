def test(expectResult, testResult):
    if(expectResult == testResult):
        print("Test pass!!!\n expectResult: ", expectResult, " testResult: " , testResult)
    else: 
        print("Test fail!!!\n: expectResult", expectResult, " testResult: ", testResult )