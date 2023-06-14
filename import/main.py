$sourceFilePath = "C:\ścieżka\do\twojego\pliku.pdf"
$destinationFilePath = "C:\ścieżka\do\wynikowego\pliku.pdf"

$acrobat = New-Object -ComObject "AcroExch.App"
$avDocs = $acrobat.GetAVDocs()

$sourceDoc = $avDocs.Open($sourceFilePath, "")
$jsObject = $sourceDoc.GetJSObject()

# Ustawienia drukowania
$printerName = "Adobe PDF"
$jsObject.printerName = $printerName
$jsObject.printWithDialogs = $false  # Drukuj bez pokazywania dialogów

# Wydrukuj do pliku PDF
$jsObject.printAll()

# Zapisz wynikowy plik PDF
$sourceDoc.Save(1, $destinationFilePath)

$sourceDoc.Close()
$acrobat.Exit()



#import packs
import csv
import psycopg2
import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pickle
import os 
from threading import Thread
from tqdm import tqdm

#Threading function 
def T_Import():
    blindLabel.config(text='')
    thread2 = Thread(target=import_data)
    thread2.start()

#Import data to database 
def import_data():
    file = textbox1.get()
    table = textbox2.get()
    database_name = textbox3.get()
    host_name= textbox4.get()
    user_name= textbox5.get()
    password_name= textbox6.get()
    port_name = textbox7.get()
    delimeters = snifer(file)
    length = length_cols(file, delimeters)
    len_rows = sum1forline(file) -1
    print('ilosc kolumn: ' + str(length))
    print('ilosc wierszy: '+ str(len_rows))
    dot_table = table.find(".")
    schema_name = table[0:dot_table]
    table_len = len(table)
    table_name = table [(dot_table+1):table_len]

    print(table, dot_table, schema_name, table_name)
    s_value =''
    conn = psycopg2.connect(database=database_name,
                                host=host_name,
                                user=user_name,
                                password=password_name,
                                port=port_name)
    cur = conn.cursor()
    for i in range (0,length):
        if i ==0:
            s_value = '%s'
        else:
            s_value = s_value + ', %s' 
    print('ilość kolumn do zastąpienia: '+ s_value)
    
    #Check of how much rows has table to update 
    postgreSQL_select_Query = "SELECT count(*) FROM information_schema.columns WHERE table_schema = '"+schema_name+"' and table_name = '"+table_name+"'"
    cur.execute(postgreSQL_select_Query)
    mobile_records = cur.fetchall()
    print('ilość kolumn w bazie: '+str(mobile_records[0][0]))

    #Import data if columns in file are smaller or equal to columns in database
    if mobile_records[0][0] >= length:
        with open(file, 'r', encoding='utf-8') as f:
            if delimeters == 'BRAK':
                reader = csv.reader(f)
            else:  
                reader = csv.reader(f,delimiter=delimeters)
            next(reader) # Skip the header row.
            for row in tqdm(reader, desc="Updating row: ...", total = len):
                cur.execute(
                "INSERT INTO "+table+" VALUES ("+s_value+")",
                row
            )
        conn.commit()
        filename= os.path.basename(file)
        blindLabel.config(text='Zaimportowano plik: '+filename)
    else:
        filename= os.path.basename(file)
        print('Zła ilosc kolumn w pliku importowym')
        blindLabel.config(text='Sprawdz ilosc kolumn w pliku: '+filename)

#Cols length for loop
def length_cols(file, delimeters):
    if delimeters == 'BRAK':
        length = 1
    else:
        deli = delimeters 
        data = pd.read_csv(file,delimiter = deli).columns
        length = len(data)
    return(length)

#Delimeter recogniser 
def snifer(file):

    with open(file, 'r', encoding='utf-8') as csvfile:
        try:
            deli = csv.Sniffer().sniff(csvfile.read(1024))
            a = deli.delimiter
        except:
            a ='BRAK'
        return(a)

#Rows length for loop
def sum1forline(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)
    
#GUI
window = Tk()
window.title("Import CSV By Daniel Zielinski")
window.resizable(False, False)

notebook = ttk.Notebook(window)
notebook.grid(pady=1)

frame1 = Frame(notebook, width=550, height=300)
frame2 = Frame(notebook, width=550, height=300)
frame1.pack(expand=1)
frame2.pack(expand=1)
notebook.add(frame1, text="Import CSV")
notebook.add(frame2, text="Server")

var1 = IntVar()
var2 = IntVar()
textbox3 = StringVar()
textbox4 = StringVar()
textbox5 = StringVar()
textbox6 = StringVar()
textbox7 = StringVar()

def get_Folder_Path():
    file_selected = filedialog.askopenfilename()
    textbox1.delete(0, END)
    textbox1.insert(0, file_selected)

def show():
    textbox6.configure(show='')
    check.configure(command=hide, text='Ukryj')

def hide():
    textbox6.configure(show='*')
    check.configure(command=show, text='Pokaż')      

def save():
    config = {
        'Database': textbox3.get(),
        'Server': textbox4.get(),
        'Login': textbox5.get(),
        'Haslo': textbox6.get(),
        'Port': textbox7.get()
    }

    with open("saved_settings.dat", "wb") as pickle_file:
        pickle.dump(config, pickle_file, pickle.HIGHEST_PROTOCOL)     

def load():
    with open("saved_settings.dat", "rb") as pickle_file:
        config = pickle.load(pickle_file)

    textbox3.insert(0,config.get('Database'))
    textbox4.insert(0,config.get('Server'))
    textbox5.insert(0,config.get('Login'))
    textbox6.insert(0,config.get('Haslo'))
    textbox7.insert(0,config.get('Port'))

#Importuj
label1 = Label(frame1, text='Podaj scieżke do folderu:')
label1.grid(row=0,column=0, padx=5, pady=10)
textbox1 = Entry(frame1, width=55)
textbox1.grid(row=0,column=1, padx=5, pady=10)
Folder = Button(frame1, text='▼', command=lambda:get_Folder_Path())
Folder.grid(row=0, column=2)
#c1 = Checkbutton(frame1, text='Tylko Plik',variable=var1, onvalue=1, offvalue=0)
#c1.grid(row=2,columnspan=3)
label2 = Label(frame1, text='Podaj nazwe tabeli:')
label2.grid(row=3,column=0, padx=5, pady=10)
textbox2 = Entry(frame1, width=55)
textbox2.grid(row=3,column=1, padx=5, pady=10)
Import = Button (frame1, text='Importuj', width=10, command=T_Import)
Import.grid(row=4,columnspan=3)
blindLabel = Label(frame1, text="")
blindLabel.grid(row=5, columnspan=3, padx=5, pady=10)

#Server
label1 = Label(frame2, text='Database:')
label1.grid(row=0,column=0, padx=5, pady=10)
textbox3 = Entry(frame2, width=55)
textbox3.grid(row=0,column=1, padx=5, pady=10)
#check_save = Checkbutton(frame2, text='Save',
        #command=save)
#check_save.grid(row=0,column=2, padx=5, pady=10)
save_button = Button(frame2, text='Save', command=save)
save_button.grid(row=0, column=2)


label2 = Label(frame2, text='Server:')
label2.grid(row=1,column=0, padx=5, pady=10)
textbox4 = Entry(frame2, width=55)
textbox4.grid(row=1,column=1, padx=5, pady=10)

label3 = Label(frame2, text='Login:')
label3.grid(row=2,column=0, padx=5, pady=10)
textbox5 = Entry(frame2, width=55)
textbox5.grid(row=2,column=1, padx=5, pady=10)

label4 = Label(frame2, text='Haslo:')
label4.grid(row=3,column=0, padx=5, pady=10)
textbox6 = Entry(frame2, width=55, show='*')
textbox6.grid(row=3,column=1, padx=5, pady=10)
check = Checkbutton(frame2, text='Pokaż',
        command=show)
check.grid(row=3,column=2, padx=5, pady=10)

label5 = Label(frame2, text='Port:')
label5.grid(row=4,column=0, padx=5, pady=10)
textbox7 = Entry(frame2, width=55)
textbox7.grid(row=4,column=1, padx=5, pady=10)

check_file = os.path.isfile("saved_settings.dat")
if check_file == True:
    load()


window.mainloop()