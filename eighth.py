def bin_to_dec(binarni_cislo):
    # Pokud je binární číslo typu int, převedeme ho na řetězec
    if isinstance(binarni_cislo, int):
        binarni_cislo = str(binarni_cislo)
    # Funkce int() s parametrem 2 přetvoří binární řetězec na desítkový
    return int(binarni_cislo, 2)

def test_bin_to_dec():
    # Testy pro funkci bin_to_dec()
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    assert bin_to_dec("10011101") == 157  # Opravené číslo na správný výsledek pro 10011101
    print("Všechny testy proběhly úspěšně!")

# Volání testu
test_bin_to_dec()
