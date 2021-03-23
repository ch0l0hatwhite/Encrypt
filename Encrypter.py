import os
import hashlib
import base64
import time

def  xi():
		os.system("exit")
		os.system("exit")
		os.system("exit")
		
def dec():
	print("\033[33m")
	print("""
 ...,,,**///   .  .*((((((////**,,,.. 
 ..,,**///   .     ......./%###((//***,,
.,,*///        .    .........&%%%##(//**
,*//((      ......,,,..,...,../&&&%%#((/
*/((#   .                    .*@@@&&%%#(
/(##                             ,@@&%%#
(.                        .   .   ..@&%%
(#%  /,,    . ./****//(,....,,*%/@@@@&&%
(#%%*(/*,... ,*,  (# /##%%%#&&&&&@@@@&&%
(#%%&/*.,,//,.,.,,(,##/(cholohatwhite@@&
(#%  **,./**,.,*,,,,*//###%&&%##,,..&&%%
      *,**/*,**.,*   ,/#%%@&%%%...    .#
       ,.*/***...*,,,  .#%@&&%   .    #(
         ..,.   */*//...*.,(*       ((//
                  ./. *(##/        (//**
                  ./,//(,*.         *,,.""")
	print("""
  ========= by cholohatwhite =========
    		
    	1) Cifrar En Base64
	
   	2) Decodificar Base64
    		
   	3) Cifrar en SHA-512 Hexadecimal
    		
    	4) Cifrar en SHA-512 en Bytes
    	
    	5) Cifrar en SHA-1 Hexadecimal
    	
    	6) Cifrar Archivo En MD5 
    	
    	7) Cifrar En Blake2b
    	
    	8) Cifrar En Blake2s
    	
    	9) Cifrar En SHA-224
    	
       10) Cifrar En SHA-384
       
         0) Salir 
""")
	m=input("Elija Una Opcion En Numeros >> ")
	print("")
	if m=="1":
		print("\033[31m")
		print("""                                ,  
,,                        ,/   /|  
||      _                //   / |  
||/|,  < \,  _-_,  _-_  ((_-  __|_ 
|| ||  /-|| ||_.  || \\  || )) ---- 
|| |' (( ||  ~ || ||/   (( ||   |  
\\/     \/\\ ,-_-    \\,/   \//   ,_,         
""")
		text = input( '\033[31mTexto a codificar > ' )
		time.sleep(0.1)
		texto_bytes = base64.b64encode(text.encode())
		texto_base64 =texto_bytes.decode()
		time.sleep(2)
		print("")
		print('\033[32m su texto en base 64 es : '+texto_base64)
		print("")
		time.sleep(3)
		dec()
		
		
	if m=="8":
	 Blac= input("\033[34mIngrese Palabra a Codificar > ") 
	 obs= hashlib.blake2s()
	 obs.update(Blac.encode('utf-8'))
	 print("")
	 print("\033[32mPalabra Codificada  En Blake2s :")
	 print("")
	 print(obs.hexdigest())
	 time.sleep(3)
	 dec()
	 
	if m=="9":
	 Blc= input("\033[34mIngrese Palabra a Codificar > ") 
	 obo= hashlib.sha224()
	 obo.update(Blc.encode('utf-8'))
	 print("")
	 print("\033[32mPalabra Codificada  En SHA-224 :")
	 print("")
	 print(obo.hexdigest())
	 dec()
	 
	if m=="10":
	 Blop= input("\033[34mIngrese Palabra a Codificar > ") 
	 obp= hashlib.sha384()
	 obp.update(Blop.encode('utf-8'))
	 print("")
	 print("\033[32mPalabra Codificada  En SHA-384 :")
	 print("")
	 print(obp.hexdigest())
	 dec()
		
	if m=="2":
		print("\033[35m")
		print("""
                                ,  
,,                        ,/   /|  
||      _                //   / |  
||/|,  < \,  _-_,  _-_  ((_-  __|_ 
|| ||  /-|| ||_.  || \\  || )) ---- 
|| |' (( ||  ~ || ||/   (( ||   |  
\\/     \/\\ ,-_-    \\,/   \//   ,_,         
""")
		texto = input('\033[35mtexto en base 64 >  ')
		texto_encode = base64.b64decode(texto.encode())
		res=(texto_encode.decode())
		print("")
		print("\033[32m Su Texto Es : " +res)
		time.sleep(3)
		print("")
		dec()
		
	if m=="3":
		print("\033[36m")
		print("""
                       ___          ____            
  -_-/  _-_-       -   -_,       ||  `  /|   /\  
 (_ /     /,      (  ~/||        ||_   /||  (  ) 
(_ --_    || __   (  / ||        |/ \   ||    // 
  --_ )  ~||-  -   \/==||  <>-<>    ))  ||   //  
 _/  ))   ||===||  /_ _||          //   ||  /(   
(_-_-    ( \_, |  (  - \\,        /'   ,/-' {___ 
""")
		print("")
		jaks= input("\033[36mIngrese Palabra a Codificar > ")
		print("")
		cifra= hashlib.sha512(jaks.encode())
		print("\033[32m Palabra codificada en SHA-512 Hexadecimal es : ")
		print("")
		print(cifra.hexdigest())
		dec()
		
	if m=="0":
		xi()
		
		
	if m=="4":
		print("\033[34m")
		print("""
                       ___          ____            
  -_-/  _-_-       -   -_,       ||  `  /|   /\  
 (_ /     /,      (  ~/||        ||_   /||  (  ) 
(_ --_    || __   (  / ||        |/ \   ||    // 
  --_ )  ~||-  -   \/==||  <>-<>    ))  ||   //  
 _/  ))   ||===||  /_ _||          //   ||  /(   
(_-_-    ( \_, |  (  - \\,        /'   ,/-' {___ 
""")
		jaks= input("\033[34mIngrese Palabra a Codificar > ")
		print("")
		cifra= hashlib.sha512(jaks.encode())
		print("\033[32m Palabra codificada en SHA-512 Bytes es : ")
		print("")
		print(cifra.digest())
		
	if  m=="5":
	 print("\033[34m")
	 print("""
                    ___               
  -_-/  _-_-       -   -_,        /|  
 (_ /     /,      (  ~/||        /||  
(_ --_    || __   (  / ||         ||  
  --_ )  ~||-  -   \/==||  <>-<>  ||  
 _/  ))   ||===||  /_ _||         ||  
(_-_-    ( \_, |  (  - \\,       ,/-'.
""")
	 shat= input("\033[34mIngrese Palabra a Codificar > ") 
	 h = hashlib.sha1()
	 h.update(shat.encode('utf-8'))
	 print("")
	 print("Palabra Codificada En SHA-1 :")
	 print("")
	 print(h.hexdigest())
	 dec()
	 
	if m=="7":
	 print("\033[34m")
	 print("""                                         
_-_ _,,   ,,       ,,          /\  ,,    
   -/  )  ||   _   ||         (  ) ||    
  ~||_<   ||  < \, ||/\  _-_    // ||/|, 
   || \\   ||  /-|| ||_< || \\   //  || || 
   ,/--|| || (( || || | ||/   /(   || |' 
  _--_-'  \\  \/\\ \\,     \\\,/ {___  \\/   
 (                                       
 
""")
	 Blacket= input("\033[34mIngrese Palabra a Codificar > ") 
	 obj= hashlib.blake2b()
	 obj.update(Blacket.encode('utf-8'))
	 print("")
	 print("\033[32mPalabra Codificada En Blake2b:")
	 print("")
	 print(obj.hexdigest())
	 dec()
	 
		
	if m=="6":
		
		print("""
		     ____  
  /\\,/\\,   -_____    ||  ` 
 /| || ||    ' | -,  ||_   
 || || ||   /| |  |` |/ \  
 ||=|= ||   || |==||    )) 
~|| || ||  ~|| |  |,   //  
 |, \\,\\,  ~-____,     /'   
_-         (               
		""")
		rutaxd=input('Ruta de almacenamiento del archivo a cifrar > ')
		f = open(rutaxd)   
		print("")
		lineas = f.readlines()    
		h = hashlib.new('md5')
		for linea in lineas:
			linea = str.encode(linea)  
			h.update(linea)    
			print("\033[32mEl resultado en bytes del hash es: " )
			print("")
			print(str(h.digest()))
			print("")
			print("\033[32mEl resultado en hexadecimales del hash es: " )
			print("")
			print(str(h.hexdigest())) 
			dec()
			
	if m==""or " ":
			print("\033[31m")
			print("""
.########.########..########...#######..########.
.##.......##.....##.##.....##.##.....##.##.....##
.##.......##.....##.##.....##.##.....##.##.....##
.######...########..########..##.....##.########.
.##.......##...##...##...##...##.....##.##...##..
.##.......##....##..##....##..##.....##.##....##.
.########.##.....##.##.....##..#######..##.....##  
""")
			print("\033[31mERROR ENTRADA NO VALIDA ELIJA UNA OPCION ")
			dec()
dec()