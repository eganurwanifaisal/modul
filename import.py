import bangunruang

def main():
	#luas permukaan tabung
	r = 14
	t = 10

	luas = bangunruang.menghitungluaspermukaantabung (r,t) 

	print(" LUAS PERMUKAAN TABUNG")
	print("jari-jari\t: ",r )
	print(" tinggi\t: ",t)
	print("luas permukaan tabung\t: ", luas)

	#luas permukaan balok
	p = 5
	l = 12
	t= 15

	luas = bangunruang.menghitungluaspermukaanbalok (p,l,t) 

	print(" LUAS PERMUKAAN BALOK")
	print("panjang\t: ",p )
	print("lebar \t: ",l)
	print("tinggi\t: ", t)
	print(" luas permukaan balok\t: ", luas)

	#luas permukaan kubus
	s = 14

	luas = bangunruang.menghitungluaspermukaankubus (s) 

	print(" LUAS PERMUKAAN KUBUS")
	print("sisi\t: ",s )
	print(" luas permukaan kubus\t: ", luas)

	#luas permukaan bola
	r = 14

	luas = bangunruang.menghitungluaspermukaanbola (r) 

	print(" LUAS PERMUKAAN BOLA")
	print("jari-jari\t: ",r )
	print(" luas permukaan bola\t: ", luas)

if __name__=="__main__":
	main()