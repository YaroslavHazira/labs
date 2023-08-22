def count_tiles(count, wieght, lenghts, rou, space):
    a = (lenghts + space) * rou + 1
    print(a)
    b = (wieght + 1) * count + 1
    print(b)
    result = a * b

    print(result)
    return result

def test(expect, testResult):
    if(expect == testResult):
        print("Test pass: ", expect, ":" ,testResult)
    else: 
        print("Test fail: ", expect, testResult )

test(37638 , count_tiles(2, 60, 60, 5, 1))
# test(2150 , count_tiles(2, 50, 1000))