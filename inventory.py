from colorama import Fore
run = True
bag = []

while run:
    print(Fore.RED + "visa innehållet [V]")
    print(Fore.GREEN + "search🔍 [F]")
    print(Fore.YELLOW + "inventory🎁 [s]")
    print(Fore.BLUE + "Avsluta programmet☠️ [Q]")
    choice = input(Fore.CYAN + "vad vill du göra?")
    print(Fore.RESET)
  
    if choice.lower() == "v":
        print(bag)
   
    elif choice.lower() == "s":
        bag.append(input("inventory"))
   
    elif choice.lower() == "q":
        run = False
    elif choice.lower() == "f":
        query = input("vad letar du efter?")
    
    
        if query in bag:
            print(Fore.MAGENTA + f"hittade {query} i inventory🎁")
        else:
            print(f"{query}, finns inte")
    
    else:
            print("felaktigt kommando, försök igen😢")
        
    print(Fore.RESET)


   