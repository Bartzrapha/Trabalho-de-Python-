def lin():
 print('-' *90)
lin()
print('  TRABALHO DE TECNICO EM PROGRAMAÇÃO  ')
lin()

def lin():
 print('-' *90)
lin()
print('   CAFETERIA PYTHON')
lin()

def menu():
    print(''' 
           MENU:
           
           [C] - Cadastrar novo voto
           [R] - Ver Resultado
           [S] - Sair


           ''')
    return str(input('Escolha uma opção: ')) 
cadastrarVoto = "c"
verResultado = "r"
sair = "s"

def porcentagem(n, t):
    return (n/t) * 100
menu()
if (cadastrarVoto):
    while (cadastrarVoto):
        n = int(input("Digite o número de um jogador para cadstrar um voto ( 0 = Voltar ao menu): "))
        if (n !=0):
            votos = 23 * [0.0]
            total = 0

            while (n != 0):
                if(n < 0 or n > 23):
                    print("Informe um valor entre 1 e 23 ou 0 para sair!")
                else:
                    votos[n - 1] +=1
                    total += 1
                    n = int(input("Digite o número de um jogador para cadastrar um novo voto (0 = Voltar ao menu):  "))
        if (n == 0):
         opcao_escolhida = menu()
if (verResultado):
    print("Resultado da Votação: ")

    print("Foram computados %de votos." % (total))
    print("Jogador / Votos / Porcentagem")
    i = 0
    melhor = 0 
    melhorPorcentagem = porcentagem(votos[0], total)

    while i < 23:
        porcentagemAtual = porcentagem(votos[i], total)
        print("%d / %d / %.1f" % (i + 1, votos[i], porcentagemAtual))
        if (porcentagemAtual > melhorPorcentagem):
            melhor = i
            melhorPorcentagem = porcentagemAtual
        i += 1
    print("O melhor jogador foi o número %d, com %d votos, correspondendo a 1f% porcento do total de votos" % (melhor +1, votos [melhor], melhorPorcentagem))                                      
    if(sair): 
     print('Programa Finalizado' )
