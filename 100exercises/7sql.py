import sqlite3

miConexion=sqlite3.connect("PruebaDB")
cursor = miConexion.cursor()

cursor.execute("""
    CREATE TABLE VEHICULOS (
        MATRICULA VARCHAR(10) PRIMARY KEY,
        MODELO VARCHAR(15),
        PRECIO INTEGER,
        COLOR VARCHAR(15)
        )
""")

addData = [
    ("5514-DFS", "MERCEDES", "50000", "BLUE"),
    ("5515-QWE", "BUGATI", "20000", "RED"),
    ("5516-ASD", "LAMBORGINI", "70000", "GREEN"),
    ("5517-ZXC", "FERRARI", "590000", "GRAY")
]

cursor.executemany("INSERT INTO VEHICULOS VALUES (?,?,?,?)", addData)
miConexion.commit()
miConexion.close() 