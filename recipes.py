recipes = [
    {"name: ": "applepie", "flour: ": 300, "baking powder: ": 1, "fruit: ": 2},
    {"name: ": "banana bread", "flour: ": 320, "baking powder: ": 1, "fruit: ": 3},
    {"name: ": "specoulus", "flour: ": 300, "baking powder: ": None, "fruit: ": None}
]


insuff = []
ingredients = ["fruit", "baking powder", "flour"]





def main():
    while True:
        name = input("Recipe: ")
        for recipe in recipes:
            if name == (recipe["name: "]):
                print(f"{recipe["name: "]}")
                print(f"Enter your ingredients for {recipe["name: "]}")
                # Flour
                while True:
                    try:
                        fl = int(input("Available flour: "))
                        break
                    except ValueError:
                        print("Flour quantity must be an integer.")

                # Baking Powder
                while True:
                    try:
                        bp = int(input("Available baking powder: "))
                        break
                    except ValueError:
                        print("Baking powder quantity must be an integer.")

                # Fruit
                while True:
                    try:
                        fr = int(input("Available fruit pieces: "))
                        break
                    except ValueError:
                        print("Fruit quantity must be an integer.")
                qnts(fr, bp, fl, recipe)
                
                insuff.clear()
        if name == "exit":
            break
            


def qnts(fru, bak, flo, r):
    #suff = ""
    if fru >= (r["fruit: "]) and bak >= (r["baking powder: "]) and flo >= (r["flour: "]):
        print(F"You have enough ingredients for {r["name: "]}")
       
    else:
        if fru < (r["fruit: "]):
            insffruit = "fruit"
            insuff.append(insffruit)
        

        if bak < (r["baking powder: "]):
            insfbp = "baking powder"
            insuff.append(insfbp)
        
        

        if flo < (r["flour: "]):
            insflo = "flour"
            insuff.append(insflo)
        
        count = len(insuff)
        
            

        print(f"You still need {count} ingredients: {', '.join(insuff)}.")  
        for missing in insuff:
            if missing == "flour":
                mflo = r["flour: "] - flo
                print(f"You need {mflo}g of flour")
            if missing == "baking powder":
                mbak = r["baking powder: "] - bak
                print(f"You need {mbak}g of baking powder")
            if missing == "fruit":
                mfru = r["fruit: "] - fru 
                print(f"You need {mfru} pieces of fruit") 
    
            

    return fru, bak, flo, r 



   
main()