def mix_columns(b):
    # Ergebnisvektor initialisieren
    result = [0, 0, 0, 0]

    # MixColumns-Operation durchführen
    for i in range(4):
        # da die Multiplikations-Matrix nach einem festen Schema gebildet wird, können wir das hier so darstellen
        result[i] = (
            multiply_by_02(b[i]) ^
            multiply_by_03(b[(i + 1) % 4]) ^
            b[(i + 2) % 4] ^
            b[(i + 3) % 4]
        )

    return result

def multiply_by_02(num):
    # Hilfsfunktion für die Multiplikation mit 0x02
    if num < 0x80:
        result = (num << 1)
    else:
        result = (num << 1) ^ 0x1B
    return result % 0x100

def multiply_by_03(num):
    # Hilfsfunktion für die Multiplikation mit 0x03
    return multiply_by_02(num) ^ num

# Beispiel
input_vector = [0x1E, 0x27, 0x5A, 0xB3]
result_vector = mix_columns(input_vector)

print("Eingabe-Vektor:", [hex(num) for num in input_vector])
print("Ergebnis-Vektor:", [hex(num) for num in result_vector])
