valInvest = float(input('Digite o valor investido: R$'))
visuOrig = valInvest * 30
totvisuNova = totcomp = totclique = 0
for c in range(3):
    if c == 0:
        clique = visuOrig * 12 / 100  # calculando o valor de cliques na 1a iteração (a partir de visuOrig)
        totclique += clique  # armazenando o valor de clique da 1 iteração em totclique
    comp = clique * 3 / 20
    visu = comp * 40
    clique = visu * 12 / 100

    totvisuNova += visu  #total de visualizações novas
    totcomp += comp  # total de compartilhamentos
    totclique += clique  # total de cliques
    visualizacoes = totvisuNova + visuOrig

print('O investimento de R${:.2f} resultou em aproximadamente {:.0f} visualizações'.format(valInvest, visualizacoes))


