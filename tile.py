def count_tiles(colum, row, wieght, lenghts, space):
    a = (lenghts + space) * row + space
    print(a)
    b = (wieght + space) * colum + space
    print(b)
    result = a * b

    print(result)
    return result

def test(expect, testResult):
    if(expect == testResult):
        print("Test pass: ", expect, ":" ,testResult)
    else: 
        print("Test fail: ", expect, testResult )


test(37638 , count_tiles(2, 5, 60, 60, 1))
