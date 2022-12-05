import sqlite3 as lite


# criando uma conexão com um novo banco de dados
con = lite.connect('dados.db')

# criando tabela categoria
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE categora(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT)')


# Criando tabela receitas
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Receitas(id INTEGER PRIMARY  KEY AUTOINCREMENT, categora TEXT, adicionado_em DATE, valor DECIMAL)')


# Criando tabela de gastos
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE Gastos(id INTEGER PRIMARY KEY AUTOINCREMENT, categoria TEXT, retirado_em DATE, valor DECIMAL)')