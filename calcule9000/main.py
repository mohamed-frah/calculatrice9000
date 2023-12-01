def calculatrice():
    while True:
        try:
            nombre1 = float(input("Entrez le premier nombre : "))
            nombre2 = float(input("Entrez le deuxième nombre : "))
            operation = input("Entrez l'opération (+, -, *, /) : ")

            if operation not in ['+', '-', '*', '/']:
                raise ValueError("Opération non valide. Veuillez entrer +, -, *, ou /.")

            if operation == '+':
                resultat = nombre1 + nombre2
            elif operation == '-':
                resultat = nombre1 - nombre2
            elif operation == '*':
                resultat = nombre1 * nombre2
            elif operation == '/':
                if nombre2 == 0:
                    raise ZeroDivisionError("Division par zéro impossible.")
                resultat = nombre1 / nombre2

            print(f"Le résultat de {nombre1} {operation} {nombre2} est : {resultat}")
            break

        except ValueError as ve:
            print(f"Erreur : {ve}")
        except ZeroDivisionError as ze:
            print(f"Erreur : {ze}")

calculatrice()
