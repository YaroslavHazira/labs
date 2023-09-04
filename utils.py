def test(expectResult, testResult):
    if(expectResult == testResult):
        print("Test pass: ", expectResult, ":" ,testResult)
    else: 
        print("Test fail: ", expectResult, testResult )