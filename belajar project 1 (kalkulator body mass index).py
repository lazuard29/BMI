"Program Perhitungan BMI"

print ("PERHITUNGAN BMI (BODY MASS INDEX)")
print ("---------------------------------")

berat_badan = input("Masukan berat badan anda (kg): ") #bentuknya str
berat_badan = float(berat_badan) #diubah
tinggi_badan = input("masukan tinggi badan anda (m): ")
tinggi_badan = float(tinggi_badan)

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal['bawah'] = 18.5*(tinggi_badan**2)
berat_badan_ideal['atas'] = 25*(tinggi_badan**2)


print("Nilai BMI anda adalah: %1.2f kg/m^2"%(bmi))
# bisa juga print (f"nilai bmi anda adalah {bmi:.2f} kg/m^2) .2f adalah angka belakang koma yang dibawa
# bisa juga print ("nilai bmi anda adalah {0} kg/m^2".format(bmi)) 0 berarti bmi index ke-0

print("Nilai BMI normal adalah 18.5 - 25 kg/m^2")
print("Berat badan ideal anda adalah dalam rentang %1.2f kg sampai dengan %1.2f kg"%(berat_badan_ideal["bawah"], berat_badan_ideal["atas"]))

print ("Hatur Thanks!")