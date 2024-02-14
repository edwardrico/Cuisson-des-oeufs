import time
import beepy


def countdown(timer):
    for i in range(timer, 0, -1):
        print(".", end="", flush=True)
        if i % 1 == 0:
            print(f"\nTemps restant : {i // 60:02d}:{i % 60:02d}.", end="")
            time.sleep(1)
    print("\nCuisson terminée")
    beepy.beep(sound="ping")  # Jouer un son une fois la cuisson terminée


def main():
    print("Choisissez une option:")
    print("1. Oeufs à la coque (3 minutes)")
    print("2. Oeufs mollets (6 minutes)")
    print("3. Oeufs durs (9 minutes)")

    option = int(input("Entrez le numéro de l'option choisie: "))

    if option == 1:
        timer = 3 * 60
    elif option == 2:
        timer = 6 * 60
    elif option == 3:
        timer = 9 * 60
    else:
        print("Option invalide.")
        return

    countdown(timer)


if __name__ == "__main__":
    main()
