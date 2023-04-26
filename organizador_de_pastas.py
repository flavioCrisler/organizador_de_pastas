import os

# muda a pasta de trabalho para o caminho especificado
os.chdir(r'c:\Users\fcris\Downloads')

# retorna somente o que for um arquivo no diretório atual
lista_arquivos = [arquivo.lower() for arquivo in os.listdir() if os.path.isfile(arquivo)]

# separa cada arquivo pela extensão e tranforma em um conjunto para eliminar as extensões repetidas
lista_extensao = set([extensao.split(".")[-1] for extensao in lista_arquivos])

# confiro se já não existe a pasta e caso não exista crio uma para cada extensão encontrada.
for extensao in lista_extensao:
    if os.path.exists(extensao):
        pass
    else:
        os.mkdir(extensao)

for arquivo in lista_arquivos:
    pasta_destino = arquivo.split('.')[-1]
    de = os.path.join(os.getcwd(), arquivo)
    para = os.path.join(os.getcwd(), pasta_destino, arquivo)
    if os.path.exists(de):
        os.replace(de, para)