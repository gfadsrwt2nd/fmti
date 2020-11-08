#!/usr/bin/python
######################
# simple code by fmti
# happy anniversary fmti , jayalah selalu , kita luar biasa 
# terima kasih untuk semua anggota fmti yang ikut berpartisipasi ,love you guys & semoga makin erat tali kekeluargaan kedepan nya:)
# terima kasih untuk pembina fmti,kaprodi TI,dan semua dosen di universitas maha karya Asia

## STRUKTUR PENGURUS FORUM MAHASISWA TEKNIK INFORMATIKA (FMTI) 2019-2020

#	Penanggung Jawab	: Pujianto, S.Kom, M.Cs
#	Pembina				: Rusidi M.Kom
#	Ketua Umum 	  		: Hendy susantho 
#	Wakil Ketua Umum	: Deni
#	Sekretaris Umum    :
#	1.Sri Fatmawati
#	2.Melisa Adebi

#	Bendahara Umum  :
#	1. Ikhsan Fajri
#   2.Tri Rahayu

#	Penelitian : Yusril Octa Utama
#	1.Sela Mindasari 
#	2.M.Afif Furqon
#	3. Agus Saputra
#	4. Selamet

#	Kedisiplinan : Jefriansyah
#	1.Andono 
#	2.Aziz umar 
#	3.Trisna Mulyadi

#	Keagamaan : Fajri Al Trisna Negara
#	1.Mita Lestari
#	2.Muhammad Rifa’i 
#	3.Dhui Adithia Firdaus
#	4. Wiradi

# Kominfo : Sony Andrianto
#	1.M. Rusdi Oktapalisa
#	2.M. Rafli Gentapratama 
#	3.Zeni 
#	4.Rindi Septia

# E-Sports : Refi Mardiyan Syaputra
#	1.Efri Marsandi 
#	2.Ardi  Okta Ganda
#	3.Ardo Syahbani
#	4.Koko Kusuma 
#	5.M.Rezqy 
#	6.Intan Sari

# Humas : M.Thorik Al Aziz
#	1.Choirul Anam 
#	2.Bayu Pratama Audi 
#	3.Wulan Sapitri
#	4. Apriani Hartati

# Olahraga: Ardi Prianto
#	1.Deni Putriyani 
#	2. Afrizal Eliyanto
#	3.Oktoresa Tambunan 
#	4. M. Alviano	

# Evaluasi : M. Rizky Surya Pratama
#	1.Rima Arilia Ika Utami
#	2.Martha Indri Syahila
#	3.Feby Puspita Sari 
#	4.Ristiana 
#	5.Luluk Fitriani
#	6.Windiyati
#	7. Ahmad Zulfikri
#	8. Dela Usmiadi

# Pengawas: 1.Adi Mahendra 
#  2.Dela Mona Wijaya 
#  3.Rike Nur safitri 
#  4.Heryanti 
#  3.Andri Setiawan

######################

import time
import os
import sys
from anggota.bendum import ikhsan
from anggota.bendum import rahayu
from anggota.esport import ardo
from anggota.esport import ardi
from anggota.esport import efri
from anggota.esport import intan
from anggota.esport import koko
from anggota.esport import mrezqy
from anggota.esport import refi
from anggota.evaluasi import ahmadZulfikri
from anggota.evaluasi import dela
from anggota.evaluasi import feby
from anggota.evaluasi import luluk
from anggota.evaluasi import martha
from anggota.evaluasi import rima
from anggota.evaluasi import ristiana
from anggota.evaluasi import rizkySurya
from anggota.evaluasi import windi
from anggota.humas import anam
from anggota.humas import apriani
from anggota.humas import thorik
from anggota.humas import ulan
from anggota.keagamaan import dhui
from anggota.keagamaan import fajri
from anggota.keagamaan import mita
from anggota.keagamaan import rifai
from anggota.keagamaan import wiradi
from anggota.kedisiplinan import andono
from anggota.kedisiplinan import aziz
from anggota.kedisiplinan import jefri
from anggota.kedisiplinan import trisna
from anggota.ketum import hendy
from anggota.kominfo import genta
from anggota.kominfo import rindi
from anggota.kominfo import rusdi
from anggota.kominfo import sony
from anggota.kominfo import zeni
from anggota.olahraga import afrizal
from anggota.olahraga import denput
from anggota.olahraga import priantoArdi
from anggota.olahraga import resa
from anggota.olahraga import vino
from anggota.penelitian import afif
from anggota.penelitian import agus
from anggota.penelitian import ninda
from anggota.penelitian import selamet
from anggota.penelitian import yusril
from anggota.pengawas import adi
from anggota.pengawas import andri
from anggota.pengawas import delamona
from anggota.pengawas import heryanti
from anggota.pengawas import rike
from anggota.sektum import fatma
from anggota.sektum import melisa
from anggota.waketum import deni


# color for this program
w = "\033[97m" #putih
y = "\033[93m" #kuning
b   = "\033[34m" #biru
g  = "\033[92m" #ijo
fg = "\033[32m" #ijoterang
r = "\033[91m" #merah

def pilih():
	print("    [*] back to main menu ? [y/N]")
	pilih = input("     root@fmtiUnmaha:~# " + y)
	if pilih == "y" or pilih == "Y":
		time.sleep(0.5)
		main()
	else:
		time.sleep(0.8)
		print("     [!] system exit")
		sys.exit()
		
def hendy():
	time.sleep(0.8)
	os.system('clear')
	print(b + "    __  __               __         _____                        __  __        ")
	print("   / / / /__  ____  ____/ /_  __   / ___/__  ___________ _____  / /_/ /_  ____ ")
	print("  / /_/ / _ \/ __ \/ __  / / / /   \__ \/ / / / ___/ __ '/ __ \/ __/ __ \/ __ \ ")
	print(" / __  /  __/ / / / /_/ / /_/ /   ___/ / /_/ (__  ) /_/ / / / / /_/ / / / /_/ / ")
	print("/_/ /_/\___/_/ /_/\__,_/\__, /   /____/\__,_/____/\__,_/_/ /_/\__/_/ /_/\____/")
	print("                       /____/ \n")
	print(w + "   [+] Nama  : Hendy Susantho")
	print("   [-] Npm   : 1813015")
	print("   [-] Divisi: Ketua Umum")
	print("   [-] Hoby  : Olahraga\n")
	pilih()
	
def fatma():
	time.sleep(0.8)
	os.system('clear')
	print(b + "   _____      _    ______      __                                 __  _    ")
	print("  / ___/_____(_)  / ____/___ _/ /_____ ___  ____ __      ______ _/ /_(_)   ")
	print("  \__ \/ ___/ /  / /_  / __ `/ __/ __ `__ \/ __ `/ | /| / / __ `/ __/ /    ")
	print(" ___/ / /  / /  / __/ / /_/ / /_/ / / / / / /_/ /| |/ |/ / /_/ / /_/ /     ")
	print("/____/_/  /_/  /_/    \__,_/\__/_/ /_/ /_/\__,_/ |__/|__/\__,_/\__/_/     \n") 
	print(w + "   [+] Nama  : Sri Fatmawati")
	print("   [-] Npm   : 1813030")
	print("   [-] Divisi: Sekertaris Umum")
	print("   [-] Hoby  : Masak\n")
	pilih()
	
def deni():
	time.sleep(0.8)
	os.system('clear')
	print(b + "     ____             _ ")
	print("    / __ \___  ____  (_) ")
	print("   / / / / _ \/ __ \/ / ")
	print("  / /_/ /  __/ / / / /  ")
	print(" /_____/\___/_/ /_/_/   \n")             
	print(w + "   [+] Nama  : Deni")
	print("   [-] Npm   : 1913008")
	print("   [-] Divisi: Wakil Ketua Umum")
	print("   [-] Hoby  : Olahraga\n")
	pilih()
	
def genta():
	time.sleep(0.8)
	os.system('clear')
	print(b + "    __  ___      __                                        __   ____        _______  ")
	print("   /  |/  /_  __/ /_  ____ _____ ___  ____ ___  ____ _____/ /  / __ \____ _/ __/ (_) ")
	print("  / /|_/ / / / / __ \/ __ `/ __ `__ \/ __ `__ \/ __ `/ __  /  / /_/ / __ `/ /_/ / / ")
	print(" / /  / / /_/ / / / / /_/ / / / / / / / / / / / /_/ / /_/ /  / _, _/ /_/ / __/ / / ")
	print("/_/  /_/\__,_/_/ /_/\__,_/_/ /_/ /_/_/ /_/ /_/\__,_/\__,_/  /_/ |_|\__,_/_/ /_/_/  ")    
	print("   ______           __                         __   ")         
	print("  / ____/__  ____  / /_____ _____  _________ _/ /_____ _____ ___  ____ _ ")     
	print(" / / __/ _ \/ __ \/ __/ __ `/ __ \/ ___/ __ `/ __/ __ `/ __ `__ \/ __ `/ ")       
	print("/ /_/ /  __/ / / / /_/ /_/ / /_/ / /  / /_/ / /_/ /_/ / / / / / / /_/ / ") 
	print("\____/\___/_/ /_/\__/\__,_/ .___/_/   \__,_/\__/\__,_/_/ /_/ /_/\__,_/  \n")      
	print("                         /_/\n")
	print(w + "   [+] Nama  : Muhammad Rafli Gentapratama")
	print("   [-] Npm   : 1913019")
	print("   [-] Divisi: Kominfo")
	print("   [-] Hoby  : Membaca Komik\n")
	pilih()	

def melisa():
	time.sleep(0.8)
	os.system('clear')
	print(b + "     __  ___     ___               ___       __     __    _    ")
	print("    /  |/  /__  / (_)________ _   /   | ____/ /__  / /_  (_)   ")
	print("   / /|_/ / _ \/ / / ___/ __ `/  / /| |/ __  / _ \/ __ \/ /    ")
	print("  / /  / /  __/ / (__  ) /_/ /  / ___ / /_/ /  __/ /_/ / /     ")
	print(" /_/  /_/\___/_/_/____/\__,_/  /_/  |_\__,_/\___/_.___/_/    \n")  
	print(w + "   [+] Nama  : Melisa Adebi")
	print("   [-] Npm   : 1913016")
	print("   [-] Divisi: Sekertaris Umum")
	print("   [-] Hoby  : Belajar\n")
	pilih()

def zeni():
	time.sleep(0.8)
	os.system('clear')
	print(b + " _____              _  ") 
	print("/__  /  ___  ____  (_) ") 
	print("  / /  / _ \/ __ \/ / ") 
	print(" / /__/  __/ / / / /  ")
	print("/____/\___/_/ /_/_/   \n")  
	print(w + "   [+] Nama  : Zeni")
	print("   [-] Npm   : 1913035")
	print("   [-] Divisi: Kominfo")
	print("   [-] Hoby  : Belajar\n")
	pilih()

def rahayu():
	time.sleep(0.8)
	os.system('clear')
	print(b + "  ______     _    ____        __                     ")
	print(" /_  __/____(_)  / __ \____ _/ /_  ____ ___  ____  __ ")
	print("  / / / ___/ /  / /_/ / __ `/ __ \/ __ `/ / / / / / / ")
	print(" / / / /  / /  / _, _/ /_/ / / / / /_/ / /_/ / /_/ / ")
	print("/_/ /_/  /_/  /_/ |_|\__,_/_/ /_/\__,_/\__, /\__,_/  ")
	print("                                      /____/ \n")
	print(w + "   [+] Nama  : Tri Rahayu")
	print("   [-] Npm   : 1913063")
	print("   [-] Divisi: Bendahara")
	print("   [-] Hoby  : \n")
	pilih()
	
def ninda():
	time.sleep(0.8)
	os.system('clear')
	print(b + "   _____      __         __  ____           __                      _    ")
	print("  / ___/___  / /___ _   /  |/  (_)___  ____/ /___ __________ ______(_)   ")
	print("  \__ \/ _ \/ / __ `/  / /|_/ / / __ \/ __  / __ `/ ___/ __ `/ ___/ /    ")
	print(" ___/ /  __/ / /_/ /  / /  / / / / / / /_/ / /_/ (__  ) /_/ / /  / /     ")
	print("/____/\___/_/\__,_/  /_/  /_/_/_/ /_/\__,_/\__,_/____/\__,_/_/  /_/      \n")
	print(w + "   [+] Nama  : Sela Mindasari ")
	print("   [-] Npm   : 1913031")
	print("   [-] Divisi: Penelitian")
	print("   [-] Hoby  : Musik\n")
	pilih()

def afif():
	time.sleep(0.8)
	os.system('clear')
	print(b + "    __  ___  ___    _____ ____   ______                            ")
	print("   /  |/  / /   |  / __(_) __/  / ____/_  ___________ _____  ____  ")
	print("  / /|_/ / / /| | / /_/ / /_   / /_  / / / / ___/ __ `/ __ \/ __ \ ")
	print(" / /  / / / ___ |/ __/ / __/  / __/ / /_/ / /  / /_/ / /_/ / / / / ")
	print("/_/  /_(_)_/  |_/_/ /_/_/    /_/    \__,_/_/   \__, /\____/_/ /_/  ")
	print("                                                 /_/              \n")
	print(w + "   [+] Nama  : M.Afif Furqon ")
	print("   [-] Npm   : 1913018")
	print("   [-] Divisi: Penelitian")
	print("   [-] Hoby  : Ngoding\n")
	pilih()

def andono():
	time.sleep(0.8)
	os.system('clear')
	print(b + "    ___              __                 ")
	print("   /   |  ____  ____/ /___  ____  ____  ")
	print("  / /| | / __ \/ __  / __ \/ __ \/ __ \ ")
	print(" / ___ |/ / / / /_/ / /_/ / / / / /_/ / ")
	print("/_/  |_/_/ /_/\__,_/\____/_/ /_/\____/  \n")
	print(w + "   [+] Nama  : Andono")
	print("   [-] Npm   : 1913003")
	print("   [-] Divisi: Kedisiplinan")
	print("   [-] Hoby  : Membaca Buku\n")
	pilih()

def trisna():
	time.sleep(0.8)
	os.system('clear')
	print(b + "  ______     _                     __  ___      __                ___  ")
	print(" /_  __/____(_)________  ____ _   /  |/  /_  __/ /_  ______ _____/ (_) ")
	print("  / / / ___/ / ___/ __ \/ __ `/  / /|_/ / / / / / / / / __ `/ __  / /  ")
	print(" / / / /  / (__  ) / / / /_/ /  / /  / / /_/ / / /_/ / /_/ / /_/ / /   ")
	print("/_/ /_/  /_/____/_/ /_/\__,_/  /_/  /_/\__,_/_/\__, /\__,_/\__,_/_/    ")
	print("                                              /____/                   \n")
	print(w + "   [+] Nama  : Trisna Mulyadi")
	print("   [-] Npm   : 1913033")
	print("   [-] Divisi: Kedisiplinan")
	print("   [-] Hoby  : Desain\n")
	pilih()
	
def rusdi():
	time.sleep(0.8)
	os.system('clear')
	print(b + "    __  ___     ____                 ___  ")
	print("   /  |/  /    / __ \__  ___________/ (_)")
	print("  / /|_/ /    / /_/ / / / / ___/ __  / / ")
	print(" / /  / /    / _, _/ /_/ (__  ) /_/ / /  ")
	print("/_/  /_(_)  /_/ |_|\__,_/____/\__,_/_/   ")
	print("                                        \n")   
	print(w + "   [+] Nama  : M.Rusdi")
	print("   [-] Npm   : 1913049")
	print("   [-] Divisi: Kominfo ")
	print("   [-] Hoby  : Ngoding\n")
	pilih()

def rindi():
	time.sleep(0.8)
	os.system('clear')
	print(b + "    ____  _           ___    _____            __  _       ")
	print("   / __ \(_)___  ____/ (_)  / ___/___  ____  / /_(_)___ _ ")
	print("  / /_/ / / __ \/ __  / /   \__ \/ _ \/ __ \/ __/ / __ `/ ")
	print(" / _, _/ / / / / /_/ / /   ___/ /  __/ /_/ / /_/ / /_/ /  ")
	print("/_/ |_/_/_/ /_/\__,_/_/   /____/\___/ .___/\__/_/\__,_/   ")
	print("                                   /_/                   \n")
	print(w + "   [+] Nama  : Rindi Septia")
	print("   [-] Npm   : 1913098")
	print("   [-] Divisi: Kominfo")
	print("   [-] Hoby  : Melakukan hal yang bermanfaat\n")
	pilih()

def efri():
	time.sleep(0.8)
	os.system('clear')
	print(b + "    __________     _    __  ___                                ___  ")
	print("   / ____/ __/____(_)  /  |/  /___ _______________ _____  ____/ (_) ")
	print("  / __/ / /_/ ___/ /  / /|_/ / __ `/ ___/ ___/ __ `/ __ \/ __  / /  ")
	print(" / /___/ __/ /  / /  / /  / / /_/ / /  (__  ) /_/ / / / / /_/ / /   ")
	print("/_____/_/ /_/  /_/  /_/  /_/\__,_/_/  /____/\__,_/_/ /_/\__,_/_/    \n")
	print(w + "   [+] Nama  : Efri Marsandi")
	print("   [-] Npm   : 1913011")
	print("   [-] Divisi: Olahraga")
	print("   [-] Hoby  : Bulutangkis\n")
	pilih()
	
def ulan():
	time.sleep(0.8)
	os.system('clear')
	print(b + " _       __      __               _____             _ __       _  ")
	print("| |     / /_  __/ /___ _____     / ___/____ _____  (_) /______(_) ")
	print("| | /| / / / / / / __ `/ __ \    \__ \/ __ `/ __ \/ / __/ ___/ /  ")
	print("| |/ |/ / /_/ / / /_/ / / / /   ___/ / /_/ / /_/ / / /_/ /  / /   ")
	print("|__/|__/\__,_/_/\__,_/_/ /_/   /____/\__,_/ .___/_/\__/_/  /_/    ")
	print("                                         /_/                    \n ")
	print(w + "   [+] Nama  : Ulan Sapitri")
	print("   [-] Npm   : 1913100")
	print("   [-] Divisi: Humas")
	print("   [-] Hoby  : Membaca Buku\n")
	pilih()
	
def apriani():
	time.sleep(0.8)
	os.system('clear')
	print(b + "    ___               _             _    __  __           __        __  _  ")
	print("   /   |  ____  _____(_)___ _____  (_)  / / / /___ ______/ /_____ _/ /_(_) ")
	print("  / /| | / __ \/ ___/ / __ `/ __ \/ /  / /_/ / __ `/ ___/ __/ __ `/ __/ /  ")
	print(" / ___ |/ /_/ / /  / / /_/ / / / / /  / __  / /_/ / /  / /_/ /_/ / /_/ /   ")
	print("/_/  |_/ .___/_/  /_/\__,_/_/ /_/_/  /_/ /_/\__,_/_/   \__/\__,_/\__/_/    ")
	print("      /_/                                                                 \n")
	print(w + "   [+] Nama  : Apriani Hartati")
	print("   [-] Npm   : 1933005")
	print("   [-] Divisi: Humas ")
	print("   [-] Hoby  : Masak\n")
	pilih()

def resa():
	time.sleep(0.8)
	os.system('clear')
	print(b + "   ____  __   __                                ______                __                               ")
	print("  / __ \/ /__/ /_____  ________  _________ _   /_  __/___ _____ ___  / /_  __  ______  ____ _____      ")
	print(" / / / / //_/ __/ __ \/ ___/ _ \/ ___/ __ `/    / / / __ `/ __ `__ \/ __ \/ / / / __ \/ __ `/ __ \     ")
	print("/ /_/ / ,< / /_/ /_/ / /  /  __(__  ) /_/ /    / / / /_/ / / / / / / /_/ / /_/ / / / / /_/ / / / /     ")
	print("\____/_/|_|\__/\____/_/   \___/____/\__,_/    /_/  \__,_/_/ /_/ /_/_.___/\__,_/_/ /_/\__,_/_/ /_/      \n")
	print(w + "   [+] Nama  : Oktoresa Tambunan")
	print("   [-] Npm   : 1913023")
	print("   [-] Divisi: Olahraga ")
	print("   [-] Hoby  : Masak\n")
	pilih()

def vino():
	time.sleep(0.8)
	os.system('clear')
	print(b + "    __  ___     ___    __      _                 ")
	print("   /  |/  /    /   |  / /   __(_)___ _____  ____  ")
	print("  / /|_/ /    / /| | / / | / / / __ `/ __ \/ __ \ ")
	print(" / /  / /    / ___ |/ /| |/ / / /_/ / / / / /_/ / ")
	print("/_/  /_(_)  /_/  |_/_/ |___/_/\__,_/_/ /_/\____/  \n")
	print(w + "   [+] Nama  : M.Alviano")
	print("   [-] Npm   : 1913017")
	print("   [-] Divisi: Olahraga")
	print("   [-] Hoby  : Gaming\n")
	pilih()

def martha():
	time.sleep(0.8)
	os.system('clear')
	print(b + "    __  ___           __  __             ____          __     _    _____             __    _ __      ")
	print("   /  |/  /___ ______/ /_/ /_  ____ _   /  _/___  ____/ /____(_)  / ___/__  ______ _/ /_  (_) /___ _ ")
	print("  / /|_/ / __ `/ ___/ __/ __ \/ __ `/   / // __ \/ __  / ___/ /   \__ \/ / / / __ `/ __ \/ / / __ `/ ")
	print(" / /  / / /_/ / /  / /_/ / / / /_/ /  _/ // / / / /_/ / /  / /   ___/ / /_/ / /_/ / / / / / / /_/ /  ")
	print("/_/  /_/\__,_/_/   \__/_/ /_/\__,_/  /___/_/ /_/\__,_/_/  /_/   /____/\__, /\__,_/_/ /_/_/_/\__,_/   ")
	print("                                                                     /____/                          \n")
	print(w + "   [+] Nama  : Martha Indri Syahlia")
	print("   [-] Npm   : 1913015")
	print("   [-] Divisi: Evaluasi")
	print("   [-] Hoby  : Musik\n")
	pilih()

def windi():
	time.sleep(0.8)
	os.system('clear')
	print(b + " _       ___           ___             __  _  ")
	print("| |     / (_)___  ____/ (_)_  ______ _/ /_(_) ")
	print("| | /| / / / __ \/ __  / / / / / __ `/ __/ /  ")
	print("| |/ |/ / / / / / /_/ / / /_/ / /_/ / /_/ /   ")
	print("|__/|__/_/_/ /_/\__,_/_/\__, /\__,_/\__/_/    ")
	print("                       /____/                 \n")
	print(w + "   [+] Nama  : Windiyati ")
	print("   [-] Npm   : 1913034")
	print("   [-] Divisi: Evaluasi ")
	print("   [-] Hoby  : Masak\n")
	pilih()
	
def banner():
	print(b + "\n	    ____          __  _ __  __  " + y + "anniversary" + b + "         __          ")
	print("	   / __/___ ___  / /_(_) / / /___  ____ ___  ____ _/ /_  ____ _ ")
	print("	  / /_/ __ `__ \/ __/ / / / / __ \/ __ `__ \/ __ `/ __ \/ __ `/ ")
	print("	 / __/ / / / / / /_/ / /_/ / / / / / / / / / /_/ / / / / /_/ /  2019-2020")
	print("	/_/ /_/ /_/ /_/\__/_/\____/_/ /_/_/ /_/ /_/\__,_/_/ /_/\__,_/   \n")
	print(w + "          thanks to Allah SWT & all my friends at unmaha university\n")
	time.sleep(0.7)
	
def main():
	time.sleep(0.5)
	os.system('clear')
	banner()
	print(w + " [" + fg + "01" + w + "] cari anggota berdasarkan nama")
	print(w + " [" + fg + "02" + w + "] cari anggota berdasarkan divisi")
	print(w + " [" + fg + "00" + w + "] exit ")
	fmti = input(w + "  [" + r + ">" + w + "] root@fmtiUnmaha:~# " + y)
	if fmti == "1" or fmti == "01":
		try:
			name = input(w + "  [>] masukan nama: " + y)
			if name == "hendy" or name == "Hendy":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				hendy()
			elif name == "fatma" or name == "Fatma":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				fatma()
			elif name == "deni" or name == "Deni":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				deni()
			elif name == "melisa" or name == "Melisa":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				melisa()
			elif name == "vino" or name == "alviano":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				vino()
			elif name == "genta" or name == "Genta":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				genta()
			elif name == "rahayu" or name == "Rahayu":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				rahayu()
			elif name == "yusril" or name == "Yusril":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				yusril()
			elif name == "ninda" or name == "Ninda":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				ninda()
			elif name == "afif" or name == "Afif":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				afif()
			elif name == "agus" or name == "Agus":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				agus()
			elif name == "selamet" or name == "Selamet":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				selamet()
			elif name == "andono" or name == "Andono":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				andono()
			elif name == "aziz" or name == "Aziz":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				aziz()
			elif name == "trisna" or name == "Trisna":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				trisna()
			elif name == "ikhsan" or name == "Ikhsan":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				fajri()
			elif name == "mita" or name == "Mita":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				mita()
			elif name == "rifai" or name == "Rifai":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				rifai()
			elif name == "dhui" or name == "Dhui":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				dhui()
			elif name == "wiradi" or name == "Wiradi":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				wiradi()
			elif name == "sony" or name == "Sony":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				sony()
			elif name == "rusdi" or name == "Rusdi":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				rusdi()
			elif name == "rindi" or name == "Rindi":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				rindi()
			elif name == "refi" or name == "Refi":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				refi()
			elif name == "efri" or name == "Efri":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				efri()
			elif name == "ardi" or name == "Ardi":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				ardi()
			elif name == "ardo" or name == "Ardo":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				ardo()
			elif name == "rezqy" or name == "rezqy":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				mrezqy()
			elif name == "intan" or name == "Intan":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				intan()
			elif name == "thorik" or name == "Thorik":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				thorik()
			elif name == "anam" or name == "Anam":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				anam()
			elif name == "ulan" or name == "Ulan":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				ulan()
			elif name == "apriani" or name == "Apriani":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				apriani()
			elif name == "ardi prianto" or name == "Ardi Prianto":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				priantoArdi()
			elif name == "deni putri" or name == "Deni Putri":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				denput()
			elif name == "afrizal" or name == "Afrizal":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				afrizal()
			elif name == "oktoresa" or name == "Oktoresa":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				resa()
			elif name == "alviano" or name == "Alviano":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				vino()
			elif name == "jefri" or name == "Jefri":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				jefri()
			elif name == "rizky surya" or name == "Rizky Surya":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				rizkySurya()
			elif name == "rima" or name == "Rima":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				rima()
			elif name == "martha" or name == "Martha":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				martha()
			elif name == "feby" or name == "Feby":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				feby()
			elif name == "ristiana" or name == "Ristiana":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				ristiana()
			elif name == "luluk" or name == "Luluk":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				luluk()
			elif name == "windi" or name == "Windi":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				windi()
			elif name == "ahmad zulfikri" or name == "Ahmad Zulfikri":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				ahmadZulfikri()
			elif name == "dela" or name == "Dela":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				dela()
			elif name == "adi" or name == "Adi":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				adi()
			elif name == "dela mona" or name == "Dela Mona":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				delamona()
			elif name == "rike" or name == "Rike":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				rike()
			elif name == "heryanti" or name == "Heryanti":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				heryanti()
			elif name == "andri" or name == "Andri":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				andri()
			elif name == "zeni" or name == "Zeni":
				time.sleep(0.8)
				print(w + "   [*] found")
				time.sleep(0.5)
				zeni()
			else:
				time.sleep(0.8)
				print(w + "   [" + r + "!" + w + "] Sorry..name not found or user not yet join fmti :(\n")
				time.sleep(0.5)
				balik = input("   [*] want try again search by npm ? [y/N] ")
				if balik == "y" or balik == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
		except:
			pass
			
	elif fmti == "2" or fmti == "02":
		time.sleep(0.8)
		os.system('clear')
		banner()
		print(w + " [" + fg + "01" + w + "] Ketua Umum            [" + fg + "08" + w + "] Kedisiplinan")
		print(w + " [" + fg + "02" + w + "] Wakil Ketua Umum      [" + fg + "09" + w + "] Kominfo")
		print(w + " [" + fg + "03" + w + "] Sekertaris Umum       [" + fg + "10" + w + "] Olahraga")
		print(w + " [" + fg + "04" + w + "] Bendahara Umum        [" + fg + "11" + w + "] Penelitian")
		print(w + " [" + fg + "05" + w + "] Humas                 [" + fg + "12" + w + "] Pengawas")
		print(w + " [" + fg + "06" + w + "] Evaluasi              [" + fg + "13" + w + "] E-sport")
		print(w + " [" + fg + "07" + w + "] Keagamaan             [" + r + "00" + w + "] kembali.\n")
		divisi = input("  [>] root@fmtiUnmaha:~# " + y)
		try:
			if divisi == "1" or divisi == "01":
				os.system('clear')
				banner()
				print(" No | Nama                        | Deskripsi")
				print(" ---+-----------------------------+-----------------------")
				print(" 1. | Hendy Susantho              | Ketua Umum 2019-2020 ")
				print("    |                             |                     \n ")
				ketum = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if ketum == "y" or ketum == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
					
			elif divisi == "2" or divisi == "02":
				os.system('clear')
				banner()
				print(" No | Nama                    | Deskripsi")
				print(" ---+-------------------------+----------------------------")
				print(" 1. | Deni                    | Wakil Ketua Umum 2019-2020 ")
				print("    |                         |                            \n ")
				waketum = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if waketum == "y" or waketum == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
					
			elif divisi == "3" or divisi == "03":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | Sri Fatmawati            | Sekertaris Umum (1) 2019-2020 ")
				print(" 2. | Melisa Adebi             | Sekertaris Umum (2) 2019-2020  ")
				print("    |                          |                               \n")
				sektum = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if sektum == "y" or sektum == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
					
			elif divisi == "4" or divisi == "04":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | Ikhsan Fajri             | Bendahara Umum (1) 2019-2020 ")
				print(" 2. | Tri Rahayu               | Bendahara Umum (2) 2019-2020  ")
				print("    |                          |                               \n")
				sektum = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if sektum == "y" or sektum == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
			elif divisi == "5" or divisi == "05":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | M.Thorik Al Aziz         | Penanggung Jawab ")
				print(" 2. | Choirul Anam             | Anggota  ")
				print(" 3. | Apriani Hartati          | Anggota  ")
				print(" 4. | Ulan Sapitri             | Anggota \n")
				humas = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if humas == "y" or humas == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
			
			elif divisi == "6" or divisi == "06":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | M.Rizky Surya Pratama    | Penanggung Jawab ")
				print(" 2. | Ahmad Zulfikri           | Anggota ")
				print(" 3. | Dela Usmiadi             | Anggota ")
				print(" 4. | Feby Puspita Sari        | Anggota ")
				print(" 5. | Rima Arilia Ika Utami    | Anggota ")
				print(" 6. | Martha Indri Syahlia     | Anggota ")
				print(" 7. | Luluk Fitriani           | Anggota ")
				print(" 8. | Ristiana                 | Anggota \n")
				evaluasi = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if evaluasi == "y" or evaluasi == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
			elif divisi == "7" or divisi == "07":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | Fajri Al Trisna Negara   | Penanggung Jawab ")
				print(" 2. | Mita Lestari             | Anggota ")
				print(" 3. | Muhammad Rifa'i          | Anggota ")
				print(" 4. | Dhyo Adithia Firdaus     | Anggota ")
				print(" 5. | Wiradi Nur Khaliq        | Anggota \n")
				keagamaan = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if keagamaan == "y" or keagamaan == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
			
			elif divisi == "8" or divisi == "08":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | Jefriansyah              | Penanggung Jawab ")
				print(" 2. | Andono                   | Anggota ")
				print(" 3. | Aziz Umar                | Anggota ")
				print(" 4. | Trisna Mulyadi           | Anggota \n")
				kedisiplinan = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if kedisiplinan == "y" or kedisiplinan == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
			
			elif divisi == "9" or divisi == "09":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | Sony Andrianto           | Penanggung Jawab ")
				print(" 2. | M.Rusdi Oktapalisa       | Anggota ")
				print(" 3. | M.Rafli Gentapratama     | Anggota ")
				print(" 4. | Zeni                     | Anggota ")
				print(" 5. | Rindi Septia             | Anggota \n")
				kominfo = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if kominfo == "y" or kominfo == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
			
			elif divisi == "10":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | Ardi Prianto             | Penanggung Jawab ")
				print(" 2. | Afrizal Eliyanto         | Anggota ")
				print(" 3. | Deni Putriyani           | Anggota ")
				print(" 4. | Oktoresa Tambunan        | Anggota ")
				print(" 5. | M.Alviano                | Anggota \n")
				olahraga = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if olahraga == "y" or olahraga == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
					
			elif divisi == "11":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | Yusril Octa Utama        | Penanggung Jawab ")
				print(" 2. | M.Afif Furqon            | Anggota ")
				print(" 3. | Agus Saputra             | Anggota ")
				print(" 4. | Selamet                  | Anggota ")
				print(" 5. | Sela Mindasari           | Anggota \n")
				penelitian = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if penelitian == "y" or penelitian == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
			
			elif divisi == "12":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | Adi Mahendra             | Penanggung Jawab ")
				print(" 2. | Dela Mona Wijaya         | Anggota ")
				print(" 3. | Rike Nur Safitri         | Anggota ")
				print(" 4. | Heryanti                 | Anggota ")
				print(" 5. | Andri Setiawan           | Anggota \n")
				pengawas = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if pengawas == "y" or pengawas == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
					
			elif divisi == "13":
				os.system('clear')
				banner()
				print(" No | Nama                     | Deskripsi")
				print(" ---+--------------------------+-------------------------------")
				print(" 1. | Refi Mardiyan Syaputra   | Penanggung Jawab ")
				print(" 2. | Efri Marsandi            | Anggota ")
				print(" 3. | M.Rezqy                  | Anggota ")
				print(" 4. | Ardi Okta Ganda          | Anggota ")
				print(" 5. | Ardo Syahbani            | Anggota ")
				print(" 6. | Koko Kusuma              | Anggota ")
				print(" 7. | Intan Sari               | Anggota\n")
				esport = input(w + "  [*] kembali ke menu ? [y/N] " + y)
				if esport == "y" or esport == "Y":
					main()
				else:
					time.sleep(0.8)
					sys.exit()
			elif divisi == "0" or divisi == "00":
				time.sleep(1)
				print(w + "   [" + r + "!" + w + "] system exit")
				time.sleep(0.8)
				sys.exit()
					
			else:
				time.sleep(0.8)
				print ("  [!] invalid command")
				main()
			
			
		except:
			pass
			
	elif fmti == "0" or fmti == "00":
		time.sleep(0.8)
		print("    [*] you are logged out")
		sys.exit()
	else:
		time.sleep(0.8)
		print("   [!] wrong command")
		sys.exit()
		

main()
