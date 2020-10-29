#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici

import os

# TODO: Définissez vos fonction ici
def compare_files(fname1, fname2):
    isSame = True
    with open(fname1, 'r') as f1, open(fname2,'r') as f2:

        c1 = f1.read(1)
        c2 = f2.read(1)
        
        while isSame and c1 != '' and c2 != '':
            if c1 != c2:
                isSame = False
                print(f"La différence est au {f1.tell()}e caractere. c1 = {c1}, c2 = {c2}")
                break
            c1 = f1.read(1)
            c2 = f2.read(1)
        
        if isSame:
            print("Les fichiers sont identiques")

def nombres(fname):
    with open(fname, 'r') as f:
        donnees = f.read()
    
    liste_nombres = sorted([int(mot) for mot in donnees.split() if mot.isdigit()])
    print(liste_nombres)

def mot_le_plus_long(fname):
    #print(os.getcwd())
    os.chdir('ch8_ressources')
    #print(os.getcwd())
    #print(os.listdir())
    with open(fname, mode='r', encoding='utf-8') as file:
        mots = file.read().split()
        mots = [m.strip(',.') for m in mots]
        mots.sort(key=lambda x: len(x), reverse=True)
        print(mots)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    compare_files(fname1='exemple.txt', fname2='exemple.txt')
    nombres('exemple.txt')
    mot_le_plus_long('exemple2.txt')
    pass
