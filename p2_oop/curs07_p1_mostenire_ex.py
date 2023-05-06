from curs07_p1_mostenire import *

# instantierea unui obiect din clasa AndroidPhone
onePlus8Pro = AndroidPhone("OnePlus 8 Pro", '6.7"', True)

# afisam tipul obiectului onePlus8Pro
print(f'Tipul obiectului onePlus8Pro: {type(onePlus8Pro)}')

# afisam numele clasei din care face parte onePlus8Pro
print(f'Clasa din care farce parte onePlus8Pro: {type(onePlus8Pro).__name__}')

# accesam proprietatea (atributul / field-ul) <<turned_on>> mostenita din clasa Phone
print(f'Este pornit? {onePlus8Pro.turned_on}')

# accesam metoda <<set_android_version()>> mostenita din clasa AndroidPhone
onePlus8Pro.set_android_version("13")
print(f'Versiunea de Android este {onePlus8Pro.android_version}')

# eroare: cand onePlus8Pro este de tipul AndroidPhone nu poate accesa print_oneplus_properties()
# onePlus8Pro.print_oneplus_properties()

print("")

# instantierea unui obiect din clasa OnePlus8Pro
onePlus8Pro = OnePlus8Pro("OnePlus 8 Pro", '6.7"', False)

# afisam numele clasei din care face parte obiectul onePlus8Pro
print(f'Clasa din care farce parte onePlus8Pro: {type(onePlus8Pro).__name__}')

# accesam proprietatea (atributul / field-ul) <<turned_on>> mostenita din clasa Phone
print(f'Este pornit? {onePlus8Pro.turned_on}')

# accesam metoda <<print_android_version()>> mostenita din clasa AndroidPhone
onePlus8Pro.print_android_version()

# accesam metoda <<set_android_version()>> mostenita din clasa AndroidPhone
onePlus8Pro.set_android_version("13.1")

# printam din nou versiunea, dupa ce a fost setata
onePlus8Pro.print_android_version()
print("")

# instantierea unui obiect din clasa Iphone 13 Pro
iphone13pro = Iphone13Pro("Iphone 13 PRO", '6"', True)

# accesam metoda print_phone_properties() mostenita din clasa Phone
iphone13pro.print_phone_properties()

# accesam metoda print_ios_version() mostenita din clasa IPhone
iphone13pro.print_ios_version()

# accesam metoda set_ios_version() mostenita din clasa IPhone
iphone13pro.set_ios_version("15")

print("")

# accesam metoda print_iphone_13_properties() din clasa IPhone13Pro
iphone13pro.print_iphone_13_properties()