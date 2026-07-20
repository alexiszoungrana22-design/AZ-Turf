def generer_ticket(classement):

    numeros = [c.numero for c in classement]

    return {
        "quinte": numeros[:5],
        "tierce": numeros[:3],
        "couple_gagnant": numeros[:2],
        "couple_place": [numeros[0], numeros[2]] if len(numeros) >= 3 else [],
        "bases": numeros[:2],
        "chances": numeros[2:5],
        "outsiders": numeros[5:7],
        "confiance": 90
    }
