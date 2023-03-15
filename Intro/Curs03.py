### Curs sesiunea 03

# declararea lista
lista_goala = list()

lista_goala = []

# declarare si init liste omogene(populate)

lista_stud_prez = ['Andreea', 'Alex', 'Rene']

prop = 'Astazi invatam despre liste'
lista_cu_split = prop.split()
print(lista_cu_split)

# accesare primul elem
print(lista_stud_prez[0])

# accesare ultimul element
print(lista_stud_prez[len(lista_stud_prez)-1])

# adaugare elem in lista cu append; se pune pe ultimul loc
lista_stud_prez.append("Gabriela")
print(lista_stud_prez)

# adaugare cu insert
lista_stud_prez.insert(3, 'Cosmin')
print(lista_stud_prez)

# aflare pozitie cu fc index
poz_elem_rene = lista_stud_prez.index('Rene')
print(poz_elem_rene)

# stergere element - fc remove
lista_stud_prez.remove('Gabriela')
print(lista_stud_prez)

# sterge elem pe baza de index - fc pop()
lista_stud_prez.pop(3)
print(lista_stud_prez)

# fc count
print(f'Elem alex apare de {lista_stud_prez.count("Alex")} ori')

# afisare inversata - reverse

# adaugare - extend

# fc sort() - sortare lista in ordine alfabetica

# creare lista neomogena
lista_neomogena = ['Andreea', 26, True, 'Felix', 30, False, "Rares", 20, True]

print(f'Persoanele din lista sunt: {lista_neomogena[::3]}')


### Seturi

#var1 -???
set_gol = set(())
print(set_gol)

#var2
set_gol = {}
print(set_gol)






