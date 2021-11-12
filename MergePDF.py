import glob, os, subprocess, sys, ctypes
from PyPDF2 import PdfFileMerger
from tkinter import messagebox

MessageBox = ctypes.windll.user32.MessageBoxW
#Arguments = ["", "C:\\Temp\\mergePDF", "C:\\Temp", "PDF_merged", "0", "1"]
Arguments = sys.argv
print("Arguments: " + str(sys.argv))

if Arguments[1] == "?" : 
    messagebox.showinfo('Help', 'Dieses Programm fügt PDFs aus einem Ordner zusammen\n\n'
        '1. Parameter: Quellpfad\n'
        '2. Parameter: Zielpfad\n'
        '3. Parameter: Dateiname\n'
        '4. Parameter: sollen alle Quelldateien gelöscht werden?\n'
        '5. Parameter: soll die Zieldatei automatisch geöffnet werden?\n\n'
        'Bsp: MergePDF.exe "C:\Quellpfad" "C:\Zielpfad" "Dateiname"')
    exit()

source = Arguments[1]
print("Source: " + source)
if os.path.isdir(source) == False :
    messagebox.showwarning('Invalid Source', 'Der Quellpfad existiert nicht\nAngegebener Pfad: ' + source)
    exit()

destination = Arguments[2]
print("Destination: " + destination)
if os.path.isdir(destination) == False :
    messagebox.showwarning('Invalid Destination', 'Der Zielpfad existiert nicht\nAngegebener Pfad: ' + destination)
    exit()

filename = Arguments[3]
print("Filename: " + filename)
if "/" in filename or "\"" in filename or "." in filename :
    messagebox.showwarning('Invalid Filename', 'Der Dateiname wurde nicht definiert oder enthält unerlaubte Zeichen\nAngegebener Name: ' + filename)
    exit()

autoDelete = Arguments[4]
print("autoDelete: " + autoDelete)
if autoDelete == '0' or autoDelete == '1' :
    print('autoDelete Parameter ok')
else:
    messagebox.showwarning('Invalid Parameter', '1 - Automatisch alle Quelldateien löschen\n0 - Quelldateien nicht löschen\nAngegebener Parameter: ' + autoDelete)
    exit()

autoOpen = Arguments[5]
print("autoOpen: " + autoOpen)
if autoOpen == "0" or autoOpen == "1" :
    print('autoOpen Parameter ok')
else:
    messagebox.showwarning('Invalid Parameter', '1 - Automatisch die Zieldatei öffnen\n0 - Zieldateien nicht öffnen\nAngegebener Parameter: ' + autoOpen)
    exit()


print(glob.glob(source + "\*.pdf"))
pdfs = glob.glob(source + "\*.pdf")

for f in os.listdir(source):
    if ".pdf" not in f :
        messagebox.showerror('Non-PDF Files!', 'Im Quellordner liegen nicht ausschließlich PDF-Dateien vor!')
        exit()

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(destination + "\\" + filename + ".pdf")
merger.close()

if autoDelete == "1":
    for f in os.listdir(source):
        os.remove(os.path.join(source, f))

if autoOpen == "1":
    subprocess.Popen(destination + "\\" + filename + ".pdf" ,shell=True)
