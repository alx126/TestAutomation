from curs07_p1_mostenire_multipla import StudentPersoana

note = {'Programare': 8,
        'Proiectare Software': 9,
        "Baze de date": 10}

studentPoli = StudentPersoana("Popescu", "Cristi", 1254565326598, 275326, note)

# apelam metoda mananca() din clasa Persoana
studentPoli.mananca()
print("")

# apelam metoda incepe_examen() din clasa Student
studentPoli.incepe_examen()
print("")

# apelam metodele incepe_examen() & petrece() din clasa StudentPersoana
studentPoli.print_tot_info()
studentPoli.petrece()