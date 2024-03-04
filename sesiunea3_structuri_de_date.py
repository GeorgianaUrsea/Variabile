#1 - LISTE

#declarati o lista de elemente care sa contina tipuri de date
'''lista_elemente = ['a', 'e','i','f']

#acesati si printati primul elem din lista
#indexul este intre -len(list) si len(list)-1
indice= -len(lista_elemente)
print(indice)
prim_element= lista_elemente[indice]
print(prim_element)
element_doi = lista_elemente[0]
print(element_doi)

#adauga un element la sfarsitul listei
lista_elemente.append('t')
print(lista_elemente)

#adaugam un element pe prima pozitie
lista_elemente.insert(0,"k")
print(lista_elemente)
#CAND FACEM UN INSERT ELEMENTUL SE ADAUGA LISTEI, NU SE INLOCUIESC ELEMENTELE

#STERGERE ELEMENT DIN LISTA DE LA PRIMA POZITIE DIN LISTA POP PT INDEX
lista_elemente.pop(0)
print(lista_elemente)

#stergem litera 'e' din lista
lista_elemente.remove('e')
print(lista_elemente)

'''#2- SA TRECEM LA SETS-SETURI
'''set_elemente = {"a", 'b', ' o', 3, 300.0}
print(set_elemente)
#nu avem ordine, elementele nu sunt ordonate

#adauga cifra 4
set_elemente.add(4)
print(set_elemente)
set_elemente.add(True)
print(set_elemente)

#obtinem un element din set
elem= set_elemente.pop() #returneaza o valoare si o sterge
print(elem)
print(set_elemente)

set_elemente.pop()
set_elemente.remove(True)
print(set_elemente)'''

'''#3 - TUPLURI
#declara un tuplu

tuplu_element= ('w','f', 4, True)

#print continut si tipul de date a tuplului
print(tuplu_element)
print(type(tuplu_element))
tuplu_element.count(True)
print(tuplu_element.count(True)) # de cate ori apare valoarea in tuplu

print(f"pozitia elem 4 este" {tuplu_element(4)}'''''


#4 - DICTIONARE

dic_elem = {'a':1, 'b': 2, 'c':3}
print(dic_elem)
print(dic_elem.keys()) #retureneaza cheile din dictionar

print(dic_elem.values())

#update cheia c cu valoarea 40
dic_elem.update({'c':40})
print(dic_elem)
dic_elem['c'] = 400
print(dic_elem)

#declarati un dictionar care are o singura cheie a carei valoare este o lista de 3 nr

m= {'a': [1,2,3]}
print(m)

#stergem un element din dictionar
dic_elem.pop('c')
print(dic_elem)
