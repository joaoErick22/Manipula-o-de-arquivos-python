
#bibliotecas de manipulação de arquivos

import os #comandos basicos (criar, renomear, listar)
import glob #acha arquivos por padroēs(html, pdf, exe)
import shutil #manipular pastas e arvores inteiras
import pathlib #mais moderno e trata caminho windows/linux sozinho

print("hello world")

print(os.getcwd()) #obter caminho atual
print(os.listdir()) #listar dentro da pasta
print(glob.glob("*pdf")) #retornar os arquivos pdf
os.mkdir("pasta_teste") #criar pasta
os.rename("pasta_teste", "teste_pasta") #renomear arquivos
os.makedirs("pasta/pasta", exist_ok=True) #cria pastas dentro de pasta
shutil.rmtree("pasta") #apaga tudo que estiver dentro
shutil.rmtree("teste_pasta")
print("shutil.move()") #mover arquivos ou pastas
print("shutil.copy()") #copia arquivos 
print("shutil.copytree()") #copia pastas inteiras
print("os.path.exists()") #tal pacote ou arquivo existe? 
print("os.path.isfile()") #é um arquivo?
print("os.path.isdir()") #é um diretorio?

#with open como utiliza-lo

#ARQUIVO:  selecione o nome do arquivo junto com sua extensao

#MODO:  "r: apenas ler e retorna quando usado o arquivo.read(qunatidade de linhas)", "w: modo usado para escrever, porém apaga o que ja existe no arquivo, usado com arquivo.write(mensagem)", "a: esse escreve igual o write, porém adiciona por ultimo e nao apaga nada. Usado com arquivo.write(mensagem)", "x: cria um novo arquivo para escrever"

#OBS "a+", "w+", "r+", utilizados quando voce quer utilizar outros modos juntos

#ERRORS: utilizado para tratar erro de icones ou letras, recomendavel usar o "replace"

#ENCODING: jogo de palavras, no brasil usa-se "utf-8"

#BUFERRING: utilizando 1, 0 ou numero determinado de bytes, 0 se usa em logs importantes enquanto o 1 se usa quando se quer ver cada linha apos a quebra de linha "\n"

with open("arquivo", "modo", errors="replace", encoding="utf-8", buffering=1) as f: #primeiro voce escreve o nome do arquivo e extensao, depois o modo de leitura, e em seguida o encoding.e errors
    f.write("hello world \n") # hello world
    f.write("esse é um exemplo de append! \n") #primeira linha: hello world. segunda linha: esse é um exemplo de append!
    f.write("novo texto \n") # quando o parametro do mod é "w", o write apaga tudo do arquivo e escreve do zero
    f.read() # novo texto
    f.write("segunda linha \n") 
    f.tell() # salva a posicao que o cursor parou, no caso apos a segunda linha.
    f.seek(0) # coloca o cursor no inicio, importante utilizar pois por padrao o cursor permanece na ultima linha
    linhas = f.readlines() # salva todas as linhas em uma lista de variaveis em linhas, importante usar seek(0) antes para salvar todas as linhas
    del linhas[1] # apaga o "segunda linha \n"
    f.writelines(linhas) # toda string que estiver em linhas, salva no arquivo .txt
    print(f.read()) # "novo texto"
