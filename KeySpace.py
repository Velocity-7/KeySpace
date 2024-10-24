import customtkinter as ck
import sqlite3

window = ck.CTk()
window.geometry('870x508')
window.iconbitmap('Vault/Logo.ico')
window.title('KeySpace')

Line_1 = ck.CTkLabel(window, text='Welcome to KeySpace', text_color='lightblue', font=('Arial', 18))
Line_1.grid(column=2)
Line_2 = ck.CTkLabel(window, text='', font=('Arial', 15))
Line_2.grid(column=2, row=7) 
Fake_Line_1 = ck.CTkLabel(window, text='')
Fake_Line_1.grid(row=2)
Fake_Line_2 = ck.CTkLabel(window, text='')
Fake_Line_2.grid(row=4)
Fake_Line_3 = ck.CTkLabel(window, text='')
Fake_Line_3.grid(row=6)
Fake_Line_4 = ck.CTkLabel(window, text='')
Fake_Line_4.grid(row=7)
Fake_Line_5 = ck.CTkLabel(window, text='')
Fake_Line_5.grid(row=8)
Fake_Line_6 = ck.CTkLabel(window, text='')
Fake_Line_6.grid(row=9)
Fake_Line_7 = ck.CTkLabel(window, text='')
Fake_Line_7.grid(row=10)
Fake_Line_8 = ck.CTkLabel(window, text='')
Fake_Line_8.grid(row=11)
Fake_Line_9 = ck.CTkLabel(window, text='')
Fake_Line_9.grid(row=12)
Fake_Line_10 = ck.CTkLabel(window, text='')
Fake_Line_10.grid(row=12)
Fake_Line_11 = ck.CTkLabel(window, text='')
Fake_Line_11.grid(row=13)
Fake_Line_12 = ck.CTkLabel(window, text='')
Fake_Line_12.grid(row=14)

App_Entry = ck.CTkEntry(window, placeholder_text='Enter Application Name')
App_Entry.grid(column=1, row=1)
Pass_Entry = ck.CTkEntry(window, placeholder_text='Enter Your Password', show='*')
Pass_Entry.grid(column=2, row=1)
Delete_Entry = ck.CTkEntry(window, placeholder_text='Enter ID to Delete')
Delete_Entry.grid(column=1, row=5)

def About():
 window_about = ck.CTk()
 window_about.geometry('310x120')
 window_about.iconbitmap('Vault/Logo.ico')
 window_about.title('About KeySpace')

 Fake_Line_1 = ck.CTkLabel(window_about, text='  ')
 Fake_Line_1.grid(column=0, row=1)
 Fake_Line_2 = ck.CTkLabel(window_about, text='  ')
 Fake_Line_2.grid(column=0, row=2)
 Fake_Line_3 = ck.CTkLabel(window_about, text=' ')
 Fake_Line_3.grid(column=1, row=0)
 Fake_Line_4 = ck.CTkLabel(window_about, text='  ')
 Fake_Line_4.grid(column=2, row=1)
 Fake_Line_5 = ck.CTkLabel(window_about, text='  ')
 Fake_Line_5.grid(column=2, row=2)
 Line_1 = ck.CTkLabel(window_about, text='Version V1.9', font=('Arial', 21))
 Line_1.grid(column=1, row=1)
 Line_2 = ck.CTkLabel(window_about, text='Github - Velocity-7', font=('Arial', 18))
 Line_2.grid(column=1, row=2)

 Button_Import = ck.CTkButton(window_about, text='Import (Disabled)', fg_color='grey', state='disabled', command=Import)
 Button_Import.grid(column=3, row=1)
 Button_Export = ck.CTkButton(window_about, text='Export (Disabled)', fg_color='grey', hover_color='red', state='disabled', command=Export)
 Button_Export.grid(column=3, row=2, pady=3)

 window_about.mainloop()

def Clear():
 Line_2.configure(text='')    

def Delete():
 database_connector = sqlite3.connect('Vault\Passwords.db')
 database_cursor = database_connector.cursor()

 database_cursor.execute('DELETE from passwords WHERE oid= ' + Delete_Entry.get())

 database_connector.commit()
 database_connector.close() 

def Export():
 None 

def Import():
 None     

def Save():
 database_connector = sqlite3.connect('Vault\Passwords.db')
 database_cursor = database_connector.cursor()
 database_cursor.execute('INSERT INTO passwords VALUES (:App_Entry, :Pass_Entry)',
 {
    'App_Entry': App_Entry.get(),
    'Pass_Entry': Pass_Entry.get()
 }
 )
 database_connector.commit()
 database_connector.close()
 App_Entry.delete(0, 'end')
 Pass_Entry.delete(0, 'end')

def Show():
 database_connector = sqlite3.connect('Vault\Passwords.db')
 database_cursor = database_connector.cursor()
 database_cursor.execute('SELECT *, oid FROM passwords')
 records = database_cursor.fetchall()
 
 print_records = ''

 for record in records:
    print_records += 'Username: ' + str(record[0]) + ' | ' + 'Password: ' + str(record[1]) + ' | ' + 'ID :' + ' ' + str(record[2]) + '\n'

 Line_2.configure(text=print_records)

 database_connector.commit()
 database_connector.close()  

Button_Save = ck.CTkButton(window, text='Save', hover_color='green', command=Save)
Button_Save.grid(column=4, row=1)
Button_Show = ck.CTkButton(window, text='Show', command=Show)
Button_Show.grid(column=1, row=3)
Button_Clear = ck.CTkButton(window, text='Clear', command=Clear)
Button_Clear.grid(column=2, row=3) 
Button_Delete = ck.CTkButton(window, text='Delete', fg_color='grey', hover_color='red', command=Delete)
Button_Delete.grid(column=2, row=5)
Button_Quit = ck.CTkButton(window, text='Quit', fg_color='red', hover_color='grey', command=window.quit)
Button_Quit.grid(row=16) 
Button_About = ck.CTkButton(window, text='About', hover_color='grey', command=About)
Button_About.grid(row=17, pady=3)

database_connector = sqlite3.connect('Vault\Passwords.db')
database_cursor = database_connector.cursor()

database_connector.commit()
database_connector.close()

window.mainloop()