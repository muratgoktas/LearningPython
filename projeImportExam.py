# from  kısmi import için kullanılır
import selenium.webdriver
from calculate import Sum
import myClass as myC
import random
import selenium


print(Sum(10,80))
print(myC.productDal1.Add())
print(myC.productDal2.Delete())
print(myC.productDal1)

productDal3 = myC.productDal("Ram")
print(productDal3.Update())

print(random.randint(0,20))
chromDriver =selenium.webdriver.Chrome()