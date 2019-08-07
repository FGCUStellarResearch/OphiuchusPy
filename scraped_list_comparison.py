#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Python script for figuring out what targets can be compared easily between
already-available eleanor output and TASOC output 
TODO: while more gracefully recovering from issues
Static Parameters:
    
    
Created 27 Mar 2019
.. codeauthor:: Lindsey Carboneau
"""

import re
from bs4 import BeautifulSoup
import sqlite3
import numpy as np 
import os

def picky_eat_soup(insoup, inregex):
    with open(insoup) as soupfile:
        soup = BeautifulSoup(soupfile, "lxml")
    #find_string = soup.findAll(text=re.compile(inregex));
    find_string = re.findall(inregex, open(insoup).read())
    return find_string

eleanor_files = [
    '../data/view-source_https___archipelago.uchicago.edu_tess_postcards_tpfs_s0001_4-1_.html',
    '../data/view-source_https___archipelago.uchicago.edu_tess_postcards_tpfs_s0001_4-2_.html',
    '../data/view-source_https___archipelago.uchicago.edu_tess_postcards_tpfs_s0001_4-3_.html',
    '../data/view-source_https___archipelago.uchicago.edu_tess_postcards_tpfs_s0001_4-4_.html'
]
eleanor_regex = 'tic(\d*)_s01'

#eleanor_tic_list = [picky_eat_soup(files, eleanor_regex) for files in eleanor_files]
eleanor_tic_list = []
for files in eleanor_files:
    eleanor_tic_list = eleanor_tic_list + picky_eat_soup(files, eleanor_regex)
eleanor_tic_list = list(map(int, eleanor_tic_list))

conn = sqlite3.connect('../../Stellar/TESS_data/todo.sqlite')

query = "SELECT starid FROM todolist WHERE camera IS 4"
cursor = conn.execute(query)
tasoc_tic_list = [int(record[0]) for record in cursor.fetchall()]

run_list = list(set(tasoc_tic_list) & set(eleanor_tic_list))
print(len(eleanor_tic_list))
print(len(tasoc_tic_list))

for run in run_list:
    os.system("py -W ignore C:/Users/Lindsey/Documents/clean/corrections/run_tesscorr.py ../../Stellar/TESS_data --starid "+ str(run) +" -p -q --source ffi")
    pass