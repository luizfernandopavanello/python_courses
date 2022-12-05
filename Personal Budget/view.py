import sys
import sqlite3 as lite
from datetime import datetime
import pandas as pd


con = lite.connect('dados.db')

def inserir_categoria(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Categoria (nome) VALUES (?)'
        cur.execute(query, i)


def inserir_receita(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Receitas (categoria, adicionado_em, valor) VALUES (?,?,?)'
        cur.execute(query, i)


def inserir_gastos(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Gastos (categoria, retirado_em, valor) VALUES (?,?,?)'
        cur.execute(query, i)


def deletar_receitas(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Receitas WHERE id=?'
        cur.execute(query, i)


def deletar_gastos(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Receitas WHERE id=?'
        cur.execute(query, i)


def ver_categorias():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Categoria')
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


def ver_Receitas():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Receitas')
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens


def ver_gastos():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM Gastos')
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens
