def fin_digit(num,digit) :
	number_str = str(num)
	digit_count = len(number_str)

	if digit > digit_count or digit <= 0 :
		return "Posisi diluar Number Input", digit_count

	digit_posisi = number_str[digit-1]

	return digit_posisi, digit_count


number = int(input('Masukkan Angka : '))
posisi = int(input('Masukkan posisi digit : '))

digit, count = fin_digit(number, posisi)
print (f"Digit pada posisi {posisi} adalah {digit}")
print (f"Jumlah digit angka : {count}")