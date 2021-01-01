print("mükemmel sayı bulma programına hoşgeldiniz")
 
list1 = list()
sayi = int(input("mükemmelliğini kontrol edeceğimiz sayıyı giriniz"))
for i in range(1,sayi+1):
    if(sayi % i == 0):
        list1.append(i)
        
a = sum(list1) -int(6)

print(a)      

if(sayi == a):
    print("{} sayısı mükemmel sayidir".format(sayi))
else:
    print("{} sayısı mükemmel sayi değildir".format(sayi))
    
    
    
  
 