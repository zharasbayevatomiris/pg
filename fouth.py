def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    # Získání typu figurky a její pozice
    typ = figurka["typ"]
    pozice = figurka["pozice"]

    # Kontrola, zda je cílová pozice na šachovnici
    if not (1 <= cilova_pozice[0] <= 8 and 1 <= cilova_pozice[1] <= 8):
        return False

    # Kontrola, zda je cílová pozice obsazená
    if cilova_pozice in obsazene_pozice:
        return False

    # Rozdělíme pravidla podle typu figurky
    if typ == "pěšec":
        # Pěšec se může pohybovat o jedno pole dopředu
        if cilova_pozice == (pozice[0] + 1, pozice[1]):
            return True
        # Pěšec se může pohybovat o dvě pole dopředu ze startovní pozice
        if pozice[0] == 2 and cilova_pozice == (pozice[0] + 2, pozice[1]):
            return True
        return False

    elif typ == "jezdec":
        # Jezdec se pohybuje ve tvaru "L"
        if (abs(cilova_pozice[0] - pozice[0]), abs(cilova_pozice[1] - pozice[1])) in [(2, 1), (1, 2)]:
            return True
        return False

    elif typ == "věž":
        # Věž se pohybuje horizontálně nebo vertikálně
        if pozice[0] == cilova_pozice[0]:  # Horizontálně
            for y in range(min(pozice[1], cilova_pozice[1]) + 1, max(pozice[1], cilova_pozice[1])):
                if (pozice[0], y) in obsazene_pozice:
                    return False
            return True
        elif pozice[1] == cilova_pozice[1]:  # Vertikálně
            for x in range(min(pozice[0], cilova_pozice[0]) + 1, max(pozice[0], cilova_pozice[0])):
                if (x, pozice[1]) in obsazene_pozice:
                    return False
            return True
        return False

    elif typ == "střelec":
        # Střelec se pohybuje diagonálně
        if abs(cilova_pozice[0] - pozice[0]) == abs(cilova_pozice[1] - pozice[1]):
            step_row = 1 if cilova_pozice[0] > pozice[0] else -1
            step_col = 1 if cilova_pozice[1] > pozice[1] else -1
            x, y = pozice[0] + step_row, pozice[1] + step_col
            while (x, y) != cilova_pozice:
                if (x, y) in obsazene_pozice:
                    return False
                x += step_row
                y += step_col
            return True
        return False

    elif typ == "dáma":
        # Dáma kombinuje pohyby věže a střelce
        if pozice[0] == cilova_pozice[0] or pozice[1] == cilova_pozice[1]:  # Horizontálně nebo vertikálně
            return je_tah_mozny({"typ": "věž", "pozice": pozice}, cilova_pozice, obsazene_pozice)
        elif abs(cilova_pozice[0] - pozice[0]) == abs(cilova_pozice[1] - pozice[1]):  # Diagonálně
            return je_tah_mozny({"typ": "střelec", "pozice": pozice}, cilova_pozice, obsazene_pozice)
        return False

    elif typ == "král":
        # Král se může pohybovat o jedno pole ve všech směrech
        if abs(cilova_pozice[0] - pozice[0]) <= 1 and abs(cilova_pozice[1] - pozice[1]) <= 1:
            return True
        return False

    return False