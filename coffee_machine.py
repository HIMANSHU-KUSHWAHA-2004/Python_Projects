from PRACTICE.coffee_machine_logo import logo

ressources = {
    "milk" : 1500,
    "water" : 2000,
    "coffee" : 300,
}
Menu = {
        "latte" :{
            "ingridents" :{
                "milk" : 200,
                "water" : 250,
                "coffee" : 25
            },
            "cost" : 350
        }
    
,
        "espresso" :{
            "ingridents" :{
                "milk" : 150,
                "water" : 200,
                "coffee" : 30
            },
            "cost" : 300
        }
    
,
        "cappuccino" :{
            "ingridents" :{
                "milk" : 300,
                "water" : 200,
                "coffee" : 40
            },
            "cost" : 450
        }
    
}
profit = 0

def check_resources(order_resources):
    for key in order_resources:
        if ressources[key] < order_resources[key]:
            print(f"SORRY THERE IS NOT ENOUGH {key}")
            return False
        return True
    
def money_insert(money_for_coffee):
    while True :   
        print("COFFEE MACHINE ACCEPT MONEY IN FORM OF Rs (10/50/100)")
        m_100 = int(input("INSERT Rs100 NOTES : "))
        m_50 = int(input("INSERT Rs50 NOTES : "))
        m_10 = int(input("INSERT Rs10 NOTES : "))
        if  m_100*100 + m_50*50 + m_10*10 < money_for_coffee:
            print("SORRY YOU HAVE NOT INSERTED ENOUGH MONEY PLEASE REINSERT THE MONEY \n")
        else :
            print("THNAKS FOR THE PAYMENT")
            return  m_100*100 + m_50*50 + m_10*10
        
def coffee_making(coffee_name,coffe_ingrident):
    for key in coffe_ingrident:
        ressources[key] -= coffe_ingrident[key]
    print(f"HERE IS YOUR {coffee_name.upper()} ☕ ENJOY IT")

def report(name,rate):
    cof = name.upper()
    file = open("orders.txt" ,"a")
    file.writelines(f"TYPE OF COFFEE : {cof}\tRATE OF COFFE : {rate}\n")
    file.close()

def main():
    print(logo())
    global profit
    working = True
    while working:
        choice = input("WHAT WOULD YOU LIKE TO TAKE (LATTE/ESPRESSO/CAPPUCCINO) : ").strip().lower()
        if  choice == "off":
            working = False
        elif choice == "report" or choice == "r":
                print(f"WATER - {ressources['water']}ml")
                print(f"MILK - {ressources['milk']}ml")
                print(f"COFFEE - {ressources['coffee']}gram")
                print(f"PROFIT - Rs {profit}")
        else:            
            coffee_type = Menu[choice]
            if check_resources(coffee_type["ingridents"]):
                payment = money_insert(coffee_type["cost"])
                if payment > coffee_type["cost"]:
                    change = payment - coffee_type["cost"]
                    profit += coffee_type["cost"]
                    print(f"YOUR CHANGE IS Rs {change} YOUR COFFEE IS ON THE WAY PLEASE WAIT")
            coffee_making(choice,coffee_type["ingridents"])
            report(choice,coffee_type["cost"])
        print("THANKS FOR USING \n")
        
if __name__ == "__main__":
    main()     