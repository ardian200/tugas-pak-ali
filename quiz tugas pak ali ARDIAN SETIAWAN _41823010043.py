#Hasil operasi aritmatika

i =6
j = 20.5
k = 5.7

aa = i * j
ab = i * k
ac = k + j * i
ad = i / j *k
af = j / k*i -5
ag = j - k /2 * i

print("Hasil dari No.1",aa)
print("Hasil dari No.2",ab)
print("Hasil dari No.3",ac)
print("Hasil dari No.4",ad)
print("Hasil dari No.5",af)
print("Hasil dari No.6",ag)


if j > i:
  print("No 1 True")
else :
  print("No 1 False")

if j > k:
  print("No 2 True")
else :
  print("No 2 False")

if i * k < j:
  print("No 3 True")
else :
  print("No 3 False")

if int(k) == 5:
  print("No 4 True")
else :
  print("No 4 False")

if int(j) * 5 ==100:
  print("No 5 True")
else :
  print("No 5 False")

if int(k) * 4 == int (j):
      print("No 6 True")
else:
      print("No 6 False")