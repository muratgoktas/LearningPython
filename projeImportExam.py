# from  kısmi import için kullanılır
from calculate import Sum
import myClass as myC
import random
print(Sum(10,80))
print(myC.productDal1.Add())
print(myC.productDal2.Delete())
print(myC.productDal1)

productDal3 = myC.productDal("Ram")
print(productDal3.Update())

print(random.randint(0,20))