import random #lai random.randint strāda
velreiz=("j")
while velreiz == "j":


    pareizā_atbilde = random.randint(1,100)  # skaitlis, kas jāuzmin(random katru reizi)

    for megjinajums in range(1, 5):
        guess = int(input(f"Mēģinājums {megjinajums}/4. Ievadi minējumu: "))

        if guess > pareizā_atbilde:
            print("Minejums>atbilde")
        elif guess < pareizā_atbilde:
            print("Minejums<atbilde")
        elif guess == pareizā_atbilde:
            print("Pareiza atbilde!")
            break
        
    else:
        # šis izpildās tikai tad, ja cikls beidzas un skaitlis netiek uzminēts
        print(f"Spēle beigusies! Pareizā atbilde bija {pareizā_atbilde}.")
        
velreiz = input("Vai velies spelet velreiz? (ievadi tikai: j, vai, n):")

