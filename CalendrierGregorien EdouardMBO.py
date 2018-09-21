#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      mbo-e
#
# Created:     21/09/2018
# Copyright:   (c) mbo-e 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#-*- coding: utf-8 -*-#


import os



                                                                                #on initialise les 3 varibales que nous allons utiliser
annee = 0
journee = 0
mois = ("")



def dateA(annee):                                                               #Creation de la fonction dateA (pour date Annee) qui nous serivra a recuperer l'annee rentree par l'utilisateur
    while annee < 1582 or annee > 2199:                                         #On cree une condition tant que la date est inferieur a 1582 ou superieur a 2199
        try:
            annee = int(input("Entrez l'annee : "))                                #On demandera a  l'utilisateur de rentrer une annee
        except ValueError:
            print("Vous n'avez pas rentrer une date valide. Veuillez reessayer")#Si les elements rentres sont des chiffres a virgule ou des chaines de caracteres,
                                                                                #on reviendra au debut de la condition
    return annee



a = dateA(annee)                                                                #afin de reutiliser la valeur retournee par DateA dans une autre fonction,on l'affecte a une nouvelle variable appelee a



def deuxD(a):                                                                   #Cette fonction deuxD va recuperer les deux derniers chiffres de l'annee rentree
    b = a%100                                                                   #utilisation de modulo 100 pour recuperer les deux derniers chiffres
    return b



c = deuxD(a)                                                                    #afin de retiliser la valeur retournee par deuxD dans une autre fonction, on l'affecte a une nouvelle variable appelee c



def unQ(c):                                                                     #Cette fonction unQ va recuperer le quart du chiffre obtenu dans la fonction deuxD
    d = c//4                                                                    #grace a la division avec // (ce signe nous permet de recuperer le resultat sans le(s) chiffre(s) apres la virgule)
    return d


e = unQ(c)                                                                      #afin de reutiliser la valeur retournee par unQ dans une autre fonction, on l'affecte a une nouvelle variable appelee e

def dateJ(journee):                                                             #Cette fonction DateJ va recuperer le jour du mois
    s = 0                                                                       #Variable boleenne initialisee a 0
    while s == 0:                                                               #Condition dans le cas ou tant que le jour est superieur a 31 ou inferieur a 1 et tant que les elements rentres
        try:                                                                    #sont des chiffres a virgules ou des chaines de caracteres, la variable booleenne restera a 0
            journee = int(input("Entrez la journee du mois (entre 1 et 31) : "))   #donc on reste dans la boucle
            s =1
            if journee < 1 or journee > 31:
                print ("La journee entree est inferieur a 1 ou est superieur a 31 ")
                s =0
        except ValueError:
            print ("Vous n'avez pas rentre une journee valide. Veuillez reessayer")
            s = 0
    return journee



f = dateJ(journee)                                                              #afin de reutiliser la valeur retournee par dateJ dans une autre fonction, on l'affecte a une nouvelle variable appelee f



def dateM(mois):                                                                #Fonction qui va nous permettre de recuperer le mois et de l'associer a un chiffre

    d = 0                                                                       #Variable boleenne d
    moisAnnee = {}                                                              #Creation d'un dictionnaire vide

    moisAnnee["janvier"]=0
    moisAnnee["fevrier"]=3
    moisAnnee["mars"]=3
    moisAnnee["avril"]=6                                                        #Dans ce dictionnaire nous faisons correspondre chaque mois a une valeur
    moisAnnee["mai"]=1
    moisAnnee["juin"]=4
    moisAnnee["juillet"]=6
    moisAnnee["aout"]=2
    moisAnnee["septembre"]=5
    moisAnnee["octobre"]=0
    moisAnnee["novembre"]=3
    moisAnnee["decembre"]=5


    while d == 0:
        mois = str.lower(input("Entrez un mois : "))                               #Debut de la condition
        for g in moisAnnee.keys():                                              #Pour tous les mois dans le dictionnaire
            if mois == g:                                                       #si le mois rentre correspond a un mois dans le dictionnaire
                d = 1                                                           #On sors de la boucle
        if mois not in moisAnnee.keys():                                        #si le mois rentre n'est pas dans le dictionnaire
            print ("le mot rentre ne fait pas parti des mois du calendrier")
            d = 0                                                               #on reste dans la boucle

    for i,j in moisAnnee.items():                                               #Pour les mois et les chiffres correpondants dans le dictionnaire
        if mois == i :                                                          #si le mois rentre correspond a un mois dans le dictionnaire
           return j                                                             #on retourne la valeur correspondante



k = dateM(mois)                                                                 #afin de reutiliser la valeur retournee par dateM dans une autre fonction, on l'affecte a une nouvelle variable appelee k



def bissextile(a):                                                              #Cette fonction va nous permettre de savoir si une annee est bissextile ou non
    s = 0                                                                       #Variable boleenne s
    if a%400 == 0:
        s = 1                                                                   #Une annee est bissextile si elle est divisible par 4 et non par 100 ou si l'annee est divisible par 400
    elif a%100 == 0:
        s = 0
    elif a%4 ==0:
        s = 1
    else:
        s = 0

    if s == 1 and mois == "janvier" or mois == "fevrier":                       #Si l'année est bissextile et si le mois est janvier ou férvier on soustrait 1
        return -1                                                               #sinon on ne fait rien
    else:
        return 0



n = bissextile(a)                                                               #afin de reutiliser la valeur retournee par bissextile dans une autre fonction, on l'affecte a une nouvelle variable appelee n



def siecleD (a,c):                                                              #Cette fonction va nous permettre de recuperer la valeur associee a l'annee moins les deux derniers chiffres de cette meme annee

    siecle = a - c                                                              #Calcul pour trouver l'annee moins les deux derniers chiffres de cette meme annee
    siecleD = {}                                                                #Creation d'un dictionnaire vide

    siecleD[1600]=6
    siecleD[1700]=4
    siecleD[1800]=2                                                             #On a rentrer dans le dictionnaire des elements avec des valeurs leurs correspondant
    siecleD[1900]=0
    siecleD[2000]=6
    siecleD[2100]=4

    for i,j in siecleD.items():                                                 #Dans les elements et les valeurs du dictionnaire
        if siecle == i:                                                         #si l'annee trouve est egale a celle du dictionnaire
            return(j)                                                           #On retourne la valeur correspndante


p = siecleD(a,c)                                                                #afin de reutiliser la valeur retournee par siecleD dans une autre fonction, on l'affecte a une nouvelle variable appelee p




def TrouveJour(c,e,f,k,n,p):                                                    #Cette fonction va nous permettre de trouver le jour correspondant a la date donnée

    somme = (c + e + f + k + n + p)%7                                           #Nous additionnons toutes les variables dont les valeurs correspondent a des fonctions precedemment definies et nous les divisons par
                                                                                #modulo 7 afin de garder que le reste

    dicoJour = {}                                                               #Creation d'un dictionnaire vide
    dicoJour[0]= "Dimanche"
    dicoJour[1]= "Lundi"
    dicoJour[2]= "Mardi"
    dicoJour[3]= "Mercredi"                                                     #on rentre dnas le dictionnaire les valeurs ainsi que les elements les concernants
    dicoJour[4]= "Jeudi"
    dicoJour[5]= "Vendredi"
    dicoJour[6]= "Samedi"

    for u,v in dicoJour.items():                                                #pour tous les valeurs et les elements dnas le dictionnaire
        if somme == u:                                                          #si la somme est egale a la valeur du dictionnaire
            print("C'etait un",v)                                               #Afficher l'element correspondant

TrouveJour(c,e,f,k,n,p)

os.system("pause")