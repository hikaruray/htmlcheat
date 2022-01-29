import mysql.connector

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

my_cursor.execute("CREATE TABLE htmltags (id INT, tagname VARCHAR(125), description VARCHAR(125), examples VARCHAR(512))")


