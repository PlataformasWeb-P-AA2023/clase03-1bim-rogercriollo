import csv
import os

with open('data/rc.csv', newline='') as File:  

    reader = csv.reader(File)
    
    index = open("ejemplos1/index.html", "w")
    for row in reader:

        

        print(row)
        

        file = open("ejemplos1/{name}.html".format(name = row[0].split('|')[0]), "w")
        file.write("<h1>Nombre de la institución</h1>"+ os.linesep)
        file.write("<h1>{data}</h1>".format(data = row[0].split('|')[1]) + os.linesep)
        file.write("<hr>" + os.linesep)
        file.write("datos relevantes " + os.linesep)
        file.write("<hr>" + os.linesep)
        file.write("<strong>Provincia:</strong> {data}".format(data = row[0].split('|')[3]) + os.linesep)
        file.write("<br>" + os.linesep)
        file.write("<strong>Canton: </strong> {data}".format(data = row[0].split('|')[5]) + os.linesep)
        file.write("<br>" + os.linesep)
        file.write("<strong>Parronquia: </strong>{data}".format(data = row[0].split('|')[7]) + os.linesep)
        file.write("<br>" + os.linesep)
        file.write("<hr>" + os.linesep)

        file.write("autor rc" + os.linesep)

        file.write("<br>" + os.linesep)



        index.write("<br>" + os.linesep)
        index.write("<hr>" + os.linesep)
        index.write("<a href='{ref}'>{name}</a>"
        .format(
        ref = "file:///home/salab/Descargas/clase03-1bim-rogercriollo-main/ejercicio/ejemplos1/{name_url}.html".format(name_url = row[0].split('|')[0])
        , name = row[0].split('|')[1]) + os.linesep)

       
       
        file
        file.close() 
