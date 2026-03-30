import os
import shutil

print("\033[31m")
print('''
██╗███████╗ █████╗ ██╗ █████╗ ███████╗
██║╚══███╔╝██╔══██╗██║██╔══██╗██╔════╝
██║  ███╔╝ ███████║██║███████║███████╗
██║ ███╔╝  ██╔══██║██║██╔══██║╚════██║
██║███████╗██║  ██║██║██║  ██║███████║
╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝
       Clean Your Dir's Izaias©
''')
print("\033[31m")

nome_arquivo = os.path.basename(__file__)
pasta = "/SUA/PASTA/AQUI"
prefixo = ""

while prefixo == "":
    prefixo = str(input("Prefixo: "))

arquivos = []
contador = 0
pastas_excluidas = 0
arquivos_excluidos = 0 

incluir_pastas = input("Incluir Pastas? (S/n): ")

if incluir_pastas.upper() == "S":
    incluir_pastas = True

else:
    incluir_pastas = False

for arquivo in os.listdir(pasta):
    caminho_completo = os.path.join(pasta, arquivo)

    if incluir_pastas:
        if arquivo.startswith(prefixo):
            if arquivo == nome_arquivo:
                print(f"{nome_arquivo} Não Pode Ser Excluido!")

            else:
                contador += 1
                arquivos.append(arquivo)
                if os.path.isdir(arquivo):
                    print(f"{contador}. {arquivo} \033[33m(pasta)\033[31m")
                else:
                    print(f"{contador}. {arquivo}")
            

    else:
        if arquivo.startswith(prefixo):
            if os.path.isfile(caminho_completo):
                if arquivo == nome_arquivo:
                    print(f"{nome_arquivo} Não Pode Ser Excluido!")

                else:
                    contador += 1
                    arquivos.append(arquivo)
                    print(f"{contador}. {arquivo}")

if len(arquivos) == 0:
    if incluir_pastas:
        print("0 Arquivos/Pastas Encontradas!")

    else:
        print("0 Arquivos Encontrados!")

else:
    confirm_delete = input(f"Remover {contador} Itens? (S/n): ")
    
    if confirm_delete.upper() == "S":
        for item in arquivos:
            caminho = os.path.join(pasta, item)

            if os.path.isfile(caminho):
                os.remove(caminho)
                arquivos_excluidos += 1

            elif os.path.isdir(caminho):
                shutil.rmtree(caminho)
                pastas_excluidas += 1

        if arquivos_excluidos >= 1 and pastas_excluidas >= 1:
            print(f"{arquivos_excluidos} Arquivos e {pastas_excluidas} Pastas Excluidas Com Sucesso!")
        
        elif arquivos_excluidos >= 1:
            print(f"{arquivos_excluidos} Arquivos Excluidos Com Sucesso!")
        
        else: 
            if pastas_excluidas > 1:
                print(f"{pastas_excluidas} Pastas Excluidas Com Sucesso!")
            else:
                print(f"1 Pasta Excluida Com Sucesso!")

    else:
        print("Abortando...")