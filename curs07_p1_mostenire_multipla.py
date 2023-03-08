class Persoana:
    nume = None
    prenume = None
    CNP = None

    def __init__(self, nume, prenume, cnp):
        self.nume = nume
        self.prenume = prenume
        self.CNP = cnp

    def mananca(self):
        print(f'{self.prenume} mananca.')


class Student:
    nr_matricol = None
    note = {}

    def __init__(self, nr_matricol, note):
        self.nr_matricol = nr_matricol
        self.note = note

    def incepe_examen(self):
        print(f'Studentul cu nr_matricol {self.nr_matricol} incepe examenul...')


# clasa Student nu extinde clasa Persoana, asadar clasa StudentPersoana va mosteni din ambele clase
class StudentPersoana(Persoana, Student):

    def __init__(self, nume, prenume, cnp, nr_matricol, note):
        super().__init__(nume, prenume, cnp)
        self.nr_matricol = nr_matricol
        self.note = note

    def print_tot_info(self):
        print(f'Info student:\n'
              f'Nume, Prenume: {self.nume} {self.prenume}\n'
              f'CNP: {self.CNP}\n'
              f'Nr. matricol: {self.nr_matricol}\n'
              f'Note: {self.note}\n')

    def petrece(self):
        print(f'Studentul {self.prenume} petrece')