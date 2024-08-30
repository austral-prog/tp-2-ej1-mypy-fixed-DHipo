# Replace the "ANSWER HERE" for your answer
def is_leap_year() -> bool:
    number:int = int(input("ingrese un año \n\t->"))
    if number <= 1582: 
        print(f"El año {number} no es bisiesto")
        return False
    
    if (number%4 == 0 and number%100) or number%400 == 0:
        print(f"El año {number} es bisiesto")
        return True
    
    print(f"El año {number} no es bisiesto")
    return False