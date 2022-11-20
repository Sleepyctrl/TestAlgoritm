import sqlite3

connection = sqlite3.connect('TestAlgoritmPython_Sqlite.db')
cursor = connection.cursor()
Counter =0
Full=""

#Открытие исходного файла
with open("Data.txt","r",encoding="utf-8") as reading_obj:
    Fulltext = reading_obj.readlines()

#Создание бд, если её нет
cursor.execute('''CREATE TABLE IF NOT EXISTS BASE(
            PhoneNumber TEXT , 
            Properties TEXT)''')
connection.commit()

#Выбор строки из всего документа
for SelectedRow in Fulltext:

    SelectedRow =Fulltext[Counter].split(";")
    Counter+=1
    SelectedRow[1]=int(SelectedRow[1])
    SelectedRow[2]=int(SelectedRow[2])

    #Формирование данных для бд, и текстового файла.
    while(SelectedRow[1]<=SelectedRow[2]):
        Full+=(SelectedRow[0] + (f'{SelectedRow[1]:07}') + " " + SelectedRow[4]+ "\n")
        StringInsert=f'{SelectedRow[0]} 'f'{SelectedRow[1]:07}'''
        StringInsert=StringInsert.replace(" ", "")
        Params=(StringInsert,SelectedRow[4])
        cursor.execute("INSERT INTO BASE VALUES (?, ?)", Params)
        connection.commit()
        SelectedRow[1]+=1
        
    with open("test.txt","w",encoding="utf-8") as writing_obj:
        writing_obj.write(Full)
connection.close()