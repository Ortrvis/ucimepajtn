def main():    
    tridy = [
        {"Oznaceni": "IT1A", "Pocet zaku": 16},  
        {"Oznaceni": "IT1B", "Pocet zaku": 17},
        {"Oznaceni": "IT2A", "Pocet zaku": 20}, 
        {"Oznaceni": "IT2B", "Pocet zaku": 19},
        {"Oznaceni": "IT3A", "Pocet zaku": 15},
        {"Oznaceni": "IT3B", "Pocet zaku": 14}, 
    ]   
    for trida in tridy:
        print("...............................")
        print(f'Oznaceni: {trida["Oznaceni"]}')
        print(f'Pocet zaku: {trida["Pocet zaku"]}')
        print("...............................")
if(__name__ == "__main__"):
    main()





