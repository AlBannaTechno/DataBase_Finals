"""
False


"""
import os
import sys
import time
# import pyodbcc
import pyodbc

# LOCATION = "E:/ProjectsUnderWork/TheLastBrain/FullGuiQt/BookT/acsessDatabase/database1.mdb"
LOCATION="database4.mdb"
cnxn = pyodbc.connect(r"Driver={{Microsoft Paradox Driver (*.db )}};Fil=Paradox 5.X;DefaultDir={0};Dbq={0}; CollatingSequence=ASCII;")
cursor = cnxn.cursor()
cursor.execute("select last, first from test")
row = cursor.fetchone()
