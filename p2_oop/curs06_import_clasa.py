from curs06_definire_clasa import Masina

# culoare, model, propulsie, consum, numar_locuri, viteza_maxima, faruri
toyota = Masina("Gri", "Auris", "benzina", "7l", 5, 150, "oprite")

toyota.accelereaza_masina(10)
toyota.accelereaza_masina(10)

toyota.accelereaza_masina(10)
toyota.accelereaza_masina(10)

toyota.accelereaza_masina(10)
toyota.accelereaza_masina(10)
toyota.accelereaza_masina(100)

toyota.decelereaza_masina(100)
toyota.claxoneaza_masina()

Masina.claxoneaza_masina()  # am accesat metoda claxoneaza_masina() in mod static