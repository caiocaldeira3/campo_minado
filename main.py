from campo import *

lins = cols = 151

while lins > 20 or cols > 25 or lins <= 0 or cols <= 0:
    print('Tamanho recomendado 10 linhas e 10 colunas')
    try:
        lins = int(input('Determine o número de linhas do seu campo minado: '))
        cols = int(input('Determine o número de colunas do seu campo minado: '))
    except:
        print('Digite novamente')

n_bombs = lins*cols
flags = 0

while n_bombs >= lins*cols:
    print('Quantidade de minas sugerida: {}'.format((lins*cols)//8))
    try:
        n_bombs = int(input('Determine o número de bombas ativas no seu campo minado: '))
    except:
        print('Digite novamente!')
minefield = init_minefield(lins, cols, n_bombs)

while True:
    print('{:^56}'.format('Flags: %d --- Mines: %d'%(flags, n_bombs)))
    print_minefield(minefield, lins, cols)
    try:
        x = int(input('Linha da posição a ser clicada: '))
        y = int(input('Coluna da posição a ser clicada: '))
        jogada = input('{:^56}\n'.format('Jogar - 1 || Flag - 2'))
        if jogada == '1':
            if minefield[x][y].on_click(minefield) == -1:
                print_minefield_showed(minefield, lins, cols)
                print('{:^56}\n{:^56}'.format('BUUUM!','Você perdeu'))
                break
        elif jogada == '2':
            minefield[x][y].flag()
            if minefield[x][y].flagged == 1:
                flags += 1
            else:
                flags -= 1
        elif jogada == 'exit':
            break
    except:
        pass

    if check_bombs(minefield, lins, cols):
        print_minefield_showed(minefield, lins, cols)
        print('\n\n\n\n{:^56}'.format('YOU WIN'))
        break

    if check_flags(minefield, lins, cols):
        print_minefield_showed(minefield, lins, cols)
        print('\n\n\n\n{:^56}'.format('YOU WIN'))
        break

input()
