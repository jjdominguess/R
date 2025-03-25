import sys
from dataclasses import dataclass

@dataclass
class FarmTech:
    
    length: float = 0.0
    width: float = 0.0
    
    arrayAgriculturalInput = [
        {"Cultura":"Milho", "Fósforo": 0.0, "Potássio": 0.0},
        {"Cultura":"Feijão", "Fósforo": 0.0, "Potássio": 0.0}
        ]
    
    def textMenuOption(self): 
        print("""Selecione as opções que deseja operar: 
        1 - Inserir dados da área que deseja calcular 
        2 - Atualizar dados do cálculo da área 
        3 - Excluir dados da área 
        4 - Sair do programa """)
        
    def menuSelect(self) :
        self.textMenuOption()
        menuSelection = int(input("Escolha uma das opções acima: "))
        print("\n")    
        
        match menuSelection:
            case 1:
                # Inserir dados da área que deseja calcular
                self.length = float(input("Insira o comprimento do local: "))
                self.width = float(input("Insira a largura do local: "))
                # Chamada do método areaCalculator para determinar a área do local
                area = self.areaCalculator(self.length, self.width)
                
                # Chamada do método agriculturalInput para determinar a quantidade de fósforo e potássio necessária para o plantio de milho e feijão
                agriculturalInputPhosphorus, agriculturalInputPotassium = self.agriculturalInputCorn(area)
                agriculturalInputPhosphorusBean, agriculturalInputPotassiumBean = self.agriculturalInputBean(area)
                nBeanPlanted, nCornPlanted, streetBetweenPlants = self.plantCalculator(self.length, self.width)
                
                # Mostra dos resultado da área e quantidade de fósforo e potássio necessária para o plantio de milho e feijão
                print(f"O tamanho do local é: {area:.2f}m²\n")
                
                print(f"A quantidade de fósforo necessária será {agriculturalInputPhosphorus:.2f}g e de potássio será {agriculturalInputPotassium:.2f}g para o feijão")
                print(f"A quantidade de fósforo necessária será {agriculturalInputPhosphorusBean:.2f}g e de potássio será {agriculturalInputPotassiumBean:.2f}g para o milho")
                print(f"A quantidade de feijão plantado será {nBeanPlanted} e de milho será {nCornPlanted}")
                print(f"A quantidade de ruas entre as plantas será {streetBetweenPlants}\n")
                
                # print dos valores do array             
                print(self.arrayAgriculturalInput[0])
                print(self.arrayAgriculturalInput[1])
                print("\n")
                
                exitInput = input("Deseja sair do programa? (S/N)")
                if exitInput == "S" or exitInput == "s":
                    print("Até a próxima!")
                    return  # Use return instead of break to exit the function
                else: 
                    self.menuSelect()
            
            case 2: 
                while True:
                    dataUpdate = int(input("""Qual dado deseja atualizar?
                    1 - Cultura
                    2 - Insumo
                    3 - Voltar ao menu principal
                    """))
                    match dataUpdate:  
                        case 1:
                            while True:
                                print("\n")
                                print("""Gostaria de atualizar qual cultura?: 
                                        1 - Milho
                                        2 - Feijão
                                        """)
                                # TODO - Implementar exclusão de input de string, só aceitar inteiros no crop = int(input())
                                crop = int(input())
                                cropUpdate = input("Insira a nova cultura: ")
                                if crop == 1:
                                    self.arrayAgriculturalInput[0]["Cultura"] = cropUpdate
                                    print(self.arrayAgriculturalInput[0])
                                    break
                                elif crop == 2: 
                                    self.arrayAgriculturalInput[1]["Cultura"] = cropUpdate
                                    print(self.arrayAgriculturalInput[1])
                                    break
                                else:
                                    print("Escolha uma opção válida")

                        case 2:
                            while True:    
                                agriculturalInput = int(input("""Insira o insumo:
                                1 - Fósforo
                                2 - Potássio
                                """))
                                
                                # TODO - Implementar a lógica de atualização de insumos de acordo com a área
                                cropUpdate = float(input(f"Insira a quantidade do insumo por m² "))
                                
                                if agriculturalInput == 1:
                                    self.arrayAgriculturalInput[0]["Fósforo"] = cropUpdate
                                    print(self.arrayAgriculturalInput[0])
                                    break
                                elif agriculturalInput == 2:
                                    self.arrayAgriculturalInput[1]["Potássio"] = cropUpdate
                                    print(self.arrayAgriculturalInput[1])
                                    break
                                else:
                                    print("Escolha uma opção válida")
                        case 3:
                            self.menuSelect()
                        case _:
                            print("Escolha uma opção válida")
                        
            case 3:
                while True:
                    infoDelete = int(input("""Qual dado deseja excluir?
                                            1 - Cultura
                                            2 - Insumo
                                            3 - Voltar ao menu principal
                                            """))
                    
                    match infoDelete:
                        case 1:
                            while True: 
                                print("\n")
                                print("""Gostaria de excluir qual cultura?: 
                                        1 - Milho
                                        2 - Feijão
                                        """)
                                crop = int(input())
                                if crop == 1:
                                    if "Cultura" in self.arrayAgriculturalInput[0]:
                                        del self.arrayAgriculturalInput[0]["Cultura"]
                                        print(self.arrayAgriculturalInput[0])
                                    else:
                                        print("Cultura de Milho já foi excluída.")
                                    
                                    returnMenu = input("Deseja voltar ao menu principal? S/N ")
                                    if returnMenu == "S" or returnMenu == "s":
                                        self.menuSelect()
                                    else:
                                        return
                                
                                elif crop == 2:
                                    if "Cultura" in self.arrayAgriculturalInput[1]:
                                        del self.arrayAgriculturalInput[1]["Cultura"]
                                        print(self.arrayAgriculturalInput[1])
                                    else:
                                        print("Cultura de Feijão já foi excluída.")
                                    
                                    returnMenu = input("Deseja voltar ao menu principal? S/N ")
                                    if returnMenu == "S" or returnMenu == "s":
                                        self.menuSelect()
                                    else:
                                        return
                                else:
                                    print("Escolha uma opção válida")
                            break                            
                        
                        case 2:
                            while True:
                                print("""Gostaria de excluir qual insumo?: 
                                        1 - Fósforo
                                        2 - Potássio
                                        """)
                                insumo = int(input())
                                if insumo == 1:
                                    if "Fósforo" in self.arrayAgriculturalInput[0]:
                                        del self.arrayAgriculturalInput[0]["Fósforo"]
                                        print(self.arrayAgriculturalInput[0])
                                    else:
                                        print("Fósforo já foi excluído.")
                                    returnMenu = input("Deseja voltar ao menu principal? S/N ")
                                    if returnMenu == "S" or returnMenu == "s":
                                        self.menuSelect()
                                    else:
                                        break
                                    
                                elif insumo == 2:
                                    if "Potássio" in self.arrayAgriculturalInput[1]:
                                        del self.arrayAgriculturalInput[1]["Potássio"]
                                        print(self.arrayAgriculturalInput[1])
                                    else:
                                        print("Potássio já foi excluído.")
                                    returnMenu = input("Deseja voltar ao menu principal? S/N ")
                                    if returnMenu == "S" or returnMenu == "s":
                                        self.menuSelect()
                                    else:
                                        break
                                else:
                                    print("Escolha uma opção válida")
                            break
                        case 3:
                            self.menuSelect()
                        case _:
                            print("Escolha uma opção válida")
            
            case 4:
                exitInput = input("Deseja sair do programa? (S/N)")
                if exitInput == "S" or exitInput == "s":
                    print("Até a próxima!")
                    sys.exit()  # Use return instead of break to exit the function
                else:
                    self.menuSelect()
                       
            case _: 
                print("Escolha uma opção válida")
    
    def areaCalculator(self, length: float, width: float):
        area = length * width
        return area

    def agriculturalInputCorn(self, perimeter: float):
        totalPhosphorus = perimeter * 0.09
        totalPotassium = perimeter * 0.05
        
        self.arrayAgriculturalInput[0]["Fósforo"] = totalPhosphorus
        self.arrayAgriculturalInput[0]["Potássio"] = totalPotassium
        
        return totalPhosphorus, totalPotassium
    
    def agriculturalInputBean(self, perimeter: float):
        totalPhosphorus = perimeter * 0.09
        totalPotassium = perimeter * 0.05
        
        self.arrayAgriculturalInput[1]["Fósforo"] = totalPhosphorus
        self.arrayAgriculturalInput[1]["Potássio"] = totalPotassium
        
        return totalPhosphorus, totalPotassium
    
    def plantCalculator(self, length: float, width: float):
        plantAreaLength = 0.0
        plantAreaWidth = 0.0
        
        nBeanPlanted = 0
        nCornPlanted = 0
        
        streetBetweenPlants = 0
        
        while plantAreaWidth < width:
            plantAreaWidth += 0.20
            # print("lado 20cm")
            
            while plantAreaLength < length: 
                plantAreaLength += 0.20
                #print("baixo 20cm")
                nCornPlanted += 1
                plantAreaLength += 0.10
                #print("baixo 10cm")
                nBeanPlanted += 1
            
            streetBetweenPlants += 1    
            plantAreaLength = 0.0    
            plantAreaWidth += 0.80
            # print("lado 80cm")
            # print("\n")
        
        self.arrayAgriculturalInput[0]["Quantidade de milho plantado"] = nCornPlanted
        self.arrayAgriculturalInput[1]["Quantidade de feijão plantado"] = nBeanPlanted
            
        return nBeanPlanted, nCornPlanted, streetBetweenPlants
    
farm = FarmTech() 
farm.menuSelect()