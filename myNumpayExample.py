import numpy as np
import math

print("*************** ortalama """"""""""""")
x= np.array([1,3,6,5])
mean_x =np.mean(x)
print(f"ortalama :{mean_x}")
x_nan =np.array([1,3,5,6, math.nan])
print(f"Math NaN : {math.nan}")
mean_x_nan = np.nanmean(x_nan)
print(f"Mean x nan:  {mean_x_nan}")

print("****************** Varyans**************")

x= np.array([1,3,5,6])
variance_x = np.var(x)
print(f"Varyans: {variance_x}")

x_nan = np.array([1,3,5,6,math.nan])
print(f"NaN lı elemanı olan dizini: {x_nan}")
mean_x_nan = np.nanvar(x_nan ,ddof =1)
print(f"NaN lı elemanı olan dizinin varyansı: {mean_x_nan}")

print("********** Standart Sapma**********")
x= np.array([1,3,5,6])
variance_x = np.std(x)
print(f"Stanart Sapma :{variance_x}")

x_nan=np.array([1,3,5,6,math.nan])
mean_x_nan = np.nanstd(x_nan,ddof=1)
print(f"Standart Sapma nan : {mean_x_nan}")
print("*********** Covariance ****************")
#iki rastgele değişkenin ortak değişkenliğinin bir ölçüsüdür.
x=np.array([1,3,5,6])
y=np.array([-2,-4,-5,-6])
con_xy =np.cov(x,y)
print(f"Convariace : {con_xy}")
print("**************Korelasyon**************")
x=np.array([1,3,5,6])
y=np.array([-2,-4,-5,-6])
corr = np.corrcoef(x,y)
print(f"Kolerasyon : {corr}")
print("**************** Olasılık Dağılım Fonksiyonlaı*************")
print("******|A> Binom Dağılımı ortalama ve varyans ****")
import matplotlib.pyplot  as plt

n= 8
p = 0.16
N = 100
X  = np.random.binomial(n,p,N)

counts, bins, ignored = plt.hist(X, 20, density=True, rwidth = 0.7, color='red')
plt.title("p = 0.16 n =8 ile binomial dağılımı")
plt.xlabel("Başarı sayısı")
plt.ylabel("Olasılık(Probability)")
plt.show()
