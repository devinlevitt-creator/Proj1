class TestPylance:
    def addTwoNumbers(self, a: int, b: int) -> int:
        return a + b
    
test = TestPylance()
print(test.addTwoNumbers(3, 5))

class Test1Pylance:
    def __init__(self):
        self.test1 = TestPylance()

def multiplyTwoSums(addTwoNumbers1: int, addTwoNumbers2: int) -> int:
    return addTwoNumbers1 * addTwoNumbers2

obj = Test1Pylance()
test1 = multiplyTwoSums(obj.test1.addTwoNumbers(7, 19), obj.test1.addTwoNumbers(13, 12))
print(test1)

def squareTwoProducts(multiplyTwoSums1, multiplyTwoSums2) :
    return multiplyTwoSums1 ** 2 + multiplyTwoSums2 ** 2  
 
obj2 = Test1Pylance()
test2 = squareTwoProducts(multiplyTwoSums(2, 4), multiplyTwoSums(3, 5))
print(test2)



