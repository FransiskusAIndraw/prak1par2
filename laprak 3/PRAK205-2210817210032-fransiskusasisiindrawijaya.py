from math import sqrt
ting,simir = input().split()
ting = float(ting)
simir = float(simir)
alas = sqrt((simir * simir)-(ting * ting))
kel1 = ting+simir+alas
luas = (alas*ting)/2
print("Alas = %.0fcm" %alas)
print("Tinggi = %.0fcm" %ting)
print("Keliling = %.0fcm"%kel1)
print("Luas = %.0fcm^2" %luas)
ting1 = input()
simir1 = input()
ting1 = float(ting1)
simir1 = float(simir1)
alas1 = sqrt((simir1 * simir1)-(ting1 * ting1))
kel11 = ting1+simir1+alas1
luas1 = (alas1*ting1)/2
print("Alas = %.0fcm" %alas1)
print("Tinggi = %.0fcm" %ting1)
print("Keliling = %.0fcm"%kel11)
print("Luas = %.0fcm^2" %luas1)
