import mysql.connector
from html_cheat import flist1, flist2, example

# ------------------------------------------
# SEND HTML TAGNAMES TO MYSQL for PHP USE
# ------------------------------------------

mydb= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="html",
    
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE TABLE htmltags (id INT PRIMARY KEY AUTO_INCREMENT, tagname TINYTEXT, description TINYTEXT, examples MEDIUMTEXT)")

count=0
sql = ('''
    INSERT INTO htmltags 
        (tagname, description, examples)
    VALUES 
        (%s, %s, %s)
    ''')



for i in range(0,130):
    data = (flist1[count],flist2[count],example[count])
    my_cursor.execute(sql,data)
    count+=1


mydb.commit()
# INSERT INTO tbl_name (col_name1, col_name2, ...) VALUES (value1, value2, ...)
# sql=("INSERT INTO favourite (number, info) VALUES ({},{})".format(numbers,animals))

# sql = ('''
#     INSERT INTO student 
#         (first_name, last_name, birthday, gender)
#     VALUES 
#         (%s, %s, %s, %s)
#     ''')

#     data = [
#         ('Shota', 'Sato', '2001-03-12', 'M'),
#         ('Hiroki', 'Takagi', '2000-04-05', 'M'),
#         ('Yuka', 'Kimura', '2001-03-27', 'F')
#     ]