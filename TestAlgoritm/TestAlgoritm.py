# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import sqlite3

Counter =0
Full=""

#Открываем для чтения текстовый файл, содержаший нужную нам информацию

#Для тестирования используется лишь вторая строка  
#"900;0062000;0062999;1000;ООО "Т2 Мобайл";Ростовская обл."
#1-ое число код DEF-код
#2-ое с какого числа формируется номер телефона
#3-е количество номеров
#4-ое компания оператор
#5-ое территория обслуживания

with open("Data.txt","r",encoding="utf-8") as reading_obj:
    Fulltext = reading_obj.readlines()

with sqlite3.connect('TestAlgoritmPython_Sqlite.db') as connection:
#Создаём бд, если не была создана
    connection.cursor().execute('''CREATE TABLE IF NOT EXISTS BASE(
                PhoneNumber TEXT , 
                Properties TEXT)''').fetchall()

    #Основной цикл в программе, считываем n-ую строку
    for SelectedRow in Fulltext:

        SelectedRow =Fulltext[Counter].split(";")
        Counter+=1
        SelectedRow[1]=int(SelectedRow[1])
        SelectedRow[2]=int(SelectedRow[2])

        #Из изначальной строки берём нужные нам значения, и формируем номер и название организации, и сразу вносим их в базу.
        while(SelectedRow[1]<=SelectedRow[2]):
            Full+=(SelectedRow[0] + (f'{SelectedRow[1]:07}') + " " + SelectedRow[4]+ "\n")
            StringInsert=f'{SelectedRow[0]} 'f'{SelectedRow[1]:07}'''
            StringInsert=StringInsert.replace(" ", "")
            Params=(StringInsert,SelectedRow[4])
            connection.cursor().execute("INSERT INTO BASE VALUES (?, ?)", Params).fetchall()
            SelectedRow[1]+=1

        #Записываем этот же получившийся файл в текстовый файл.    
        with open("test.txt","w",encoding="utf-8") as writing_obj:
            writing_obj.write(Full)