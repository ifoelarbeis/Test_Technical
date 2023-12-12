def primenumber(MyNum):
  n = 0
  i = 2
  for i in range(2,MyNum//2+1):
    if MyNum % i == 0:
      n = n + 1
      break
  if n == 0:
    print(MyNum)

x = int(input('masukkan angka:'))
print("Bilangan Prima kurang dari", x, "=")
for i in range(2, x+1):
  primenumber(i)