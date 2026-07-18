from backend.scoring import calcul_indice

def classer_chevaux(chevaux):

    classement=[]

    for cheval in chevaux:

        classement.append({

            "numero":cheval.numero,

            "nom":cheval.nom,

            "indiceAZ":calcul_indice(cheval)

        })

    classement.sort(
        key=lambda x:x["indiceAZ"],
        reverse=True
    )

    return classement
