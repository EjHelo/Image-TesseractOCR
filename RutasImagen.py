
import os, sys
import re

from PIL import Image

from pytesseract import image_to_string

listaImagenes = ['7001-ALA-HER.png','7002-CUR-BEL.png','7003-CAR.png']

for x in range (0,len(listaImagenes)):
    img =Image.open(listaImagenes[x])
    text = image_to_string(img, lang='spa')

    f= open( (listaImagenes[x])[:-4]+".txt",'w')
    f.write(text)
    f.close()


cadenaRuta=""
listaArchivos = ['7001-ALA-HER.txt','7002-CUR-BEL.txt','7003-CAR.txt']
pattern = "([0-9]|0[0-9]|1[0-9]|2[0-3])(:| )([0-5][0-9])"

for x in range (0,len(listaArchivos)):

    contador=0
    for i, line in enumerate(open(listaArchivos[x])):
        if (len(line)>5):
            ######
            ######COMIENZO DE ASIGNACIONES DE NOMBRES RUTAS
            if( line.startswith ("ALA") ):
                print("ALAJUELA-HEREDIA-SAN JOSE")
            if( line.startswith ("SAN JOSE- HEREDIA") ):
                print("SAN JOSE-HEREDIA-ALAJUELA")
            if( line.startswith ("¡ … CO € r BELEN") ):
                print("BELEN-CURRIDABAT")
            if( line.startswith ("CUR") ):
                print("CURRIDABAT-BELEN")
            if( line.startswith ("SANJOSECARTAGO") ):
                print("SAN JOSE-CARTAGO")
            if( line.startswith ("CARTAGO") ):
                print("CARTAGO-SAN JOSE")
            ######FINALIZACION DE ASIGNACIONES DE NOMBRES RUTAS
            ######
            for match in re.finditer(pattern,line):
                cadenaRuta = cadenaRuta + match.group() + " -> "
                contador+=1
            if (cadenaRuta != "" ):
                if (x==2 and contador<7):
                    cadenaRuta +=""
                else:
                    cadenaRuta = "Recorrido: " + cadenaRuta
                    print (cadenaRuta)
                    cadenaRuta=""
                    contador=0
