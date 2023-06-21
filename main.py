import tkinter
from tkinter import *
from tkinter import ttk

# ---------- cores ----------- #
cor1 = "#FF0000"  # Vermelho
cor2 = "#00FF00"  # Verde
cor3 = "#0000FF"  # Azul
cor4 = "#FFFF00"  # Amarelo
cor5 = "#FF00FF"  # Magenta
cor6 = "#00FFFF"  # Ciano
cor7 = "#FFA500"  # Laranja
cor8 = "#800080"  # Roxo
cor9 = "#008000"  # Verde Escuro
cor10 = "#000080"  # Azul Escuro
cor11 = "#F5F5F5"  # Branco escuro
cor12 = "#000000"  # preto
cor13 = "#808080"  # cinza


window = Tk()
window.title("")
window.geometry('290x400')
window.configure(bg=cor13)

# frame cima
frame_cima = Label(window, width=58, height=8, bg=cor10, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Label(window, width=60, height=140, bg=cor12, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

# Jogador X
playerX = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 50 bold'), bg=cor10,
                fg=cor2)
playerX.place(x=15, y=25)

playerX = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'),
                bg=cor10, fg=cor11)
playerX.place(x=20, y=93)

# estilizando o frame cima -------------

# pontuação jogador X
pontosX = Label(frame_cima, text='0', height=1, width=1, relief='flat', anchor='center', font=('Ivy 30 bold'),
                bg=cor10, fg=cor11)
pontosX.place(x=65, y=40)

# separador
separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=cor10,
                  fg=cor1)
separador.place(x=118, y=40)

# Jogador Y
playerY = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 50 bold'), bg=cor10,
                fg=cor7)
playerY.place(x=210, y=20)

playerY = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'),
                bg=cor10, fg=cor11)
playerY.place(x=210, y=86)

# pontuação jogador X
pontosY = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=cor10,
                fg=cor11)
pontosY.place(x=165, y=40)


# crinado a logica-----------------------------

# nome jogadores
jogador_1 = "X"
jogador_2 = "O"

# pontuação
score_1 = "X"
score_2 = "O"

# tabela 
tabela = [['1', '2', '3'], 
           ['4', '5', '6'], 
           ['7', '8', '9']]

# funcao


jogando = 'X'
jogar = ''
contador = 0

def iniciar_jogo():
    # controlando o jogo
    def controlar_jogo(i):
        global jogando
        global contador
        global jogar
        global color

        # Comparando os valores recebidos
        if i == '1':
            button = b_0
            row, column = 0, 0
        elif i == '2':
            button = b_1
            row, column = 0, 1
        elif i == '3':
            button = b_2
            row, column = 0, 2
        elif i == '4':
            button = b_3
            row, column = 1, 0
        elif i == '5':
            button = b_4
            row, column = 1, 1
        elif i == '6':
            button = b_5
            row, column = 1, 2
        elif i == '7':
            button = b_6
            row, column = 2, 0
        elif i == '8':
            button = b_7
            row, column = 2, 1
        elif i == '9':
            button = b_8
            row, column = 2, 2
        else:
            return

        if button['text'] == '':  # Verificando se a posição está vazia
            if jogando == 'X':
                cor1 = cor1
            elif jogando == 'O':
                cor7 = cor7

        # Alterando o texto do botão e atualizando a tabela
        button['fg'] = cor1
        button['text'] = jogando
        tabela[row][column] = jogando

        # Verificando quem está jogando
        if jogando == 'X':
            jogando = 'O'
            jogar = 'Jogador 1'
        else:
            jogando = 'X'
            jogar = 'Jogador 2'

        # Incrementando o contador
        contador += 1

        # Verificando se há algum vencedor
        if contador >= 5:
            # Linhas
            if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                vencedor(jogando)

            # Colunas
            if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                vencedor(jogando)

            # Diagonais
            if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                vencedor(jogando)

            # Empate
            if contador >= 9:
                vencedor("Empate")
                    # linhas
                if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                    vencedor(jogando)
                elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                    vencedor(jogando)
                elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                    vencedor(jogando)

                # colunas
                if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                    vencedor(jogando)
                elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                    vencedor(jogando)
                elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                    vencedor(jogando)

                    # diagonais
                if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                    vencedor(jogando)
                elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                    vencedor(jogando)
                        
                #  empate
                if contador >= 9:
                    vencedor("Empate")
                    
        if i==str(2):
            if b_1['text'] == '': # verificando se a posição esta vazia
                if jogando == 'X':
                    cor2 = cor1
                if jogando == 'O':
                    cor2 = cor2
                
                # cor dotexto do botão que marca a posicção da tabela 
                # com o valor do jogador atual
                b_1['fg'] = color
                b_1['text'] = jogando
                tabela[[0][0]] = jogando

                # verificando quem esta jogando 
                if jogando == "X":
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementando o contator
                contador += 1

                # verificando se há algum vencedor

                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        vencedor(jogando)

                    # diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        vencedor(jogando)
                    
                    #  empate
                    if contador >= 9:
                        vencedor("Empate")
        
        if i==str(3):
            if b_2['text'] == '': # verificando se a posição esta vazia
                if jogando == 'X':
                    color = cor1
                if jogando == 'O':
                    color = cor2
                
                # cor dotexto do botão que marca a posicção da tabela 
                # com o valor do jogador atual
                b_2['fg'] = color
                b_2['text'] = jogando
                tabela[[0][0]] = jogando

                # verificando quem esta jogando 
                if jogando == "X":
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementando o contator
                contador += 1

                # verificando se há algum vencedor

                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        vencedor(jogando)

                    # diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        vencedor(jogando)
                    
                    #  empate
                    if contador >= 9:
                        vencedor("Empate")
        
        if i==str(4):
            if b_3['text'] == '': # verificando se a posição esta vazia
                if jogando == 'X':
                    color = cor1
                if jogando == 'O':
                    color = cor2
                
                # cor dotexto do botão que marca a posicção da tabela 
                # com o valor do jogador atual
                b_3['fg'] = color
                b_3['text'] = jogando
                tabela[[0][0]] = jogando

                # verificando quem esta jogando 
                if jogando == "X":
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementando o contator
                contador += 1

                # verificando se há algum vencedor

                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        vencedor(jogando)

                    # diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        vencedor(jogando)
                    
                    #  empate
                    if contador >= 9:
                        vencedor("Empate")
        
        if i==str(5):
            if b_4['text'] == '': # verificando se a posição esta vazia
                if jogando == 'X':
                    color = cor1
                if jogando == 'O':
                    color = cor2
                
                # cor dotexto do botão que marca a posicção da tabela 
                # com o valor do jogador atual
                b_4['fg'] = color
                b_4['text'] = jogando
                tabela[[0][0]] = jogando

                # verificando quem esta jogando 
                if jogando == "X":
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementando o contator
                contador += 1

                # verificando se há algum vencedor

                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        vencedor(jogando)

                    # diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        vencedor(jogando)
                    
                    #  empate
                    if contador >= 9:
                        vencedor("Empate")
        
        if i==str(6):
            if b_5['text'] == '': # verificando se a posição esta vazia
                if jogando == 'X':
                    color = cor1
                if jogando == 'O':
                    color = cor2
                
                # cor dotexto do botão que marca a posicção da tabela 
                # com o valor do jogador atual
                b_5['fg'] = color
                b_5['text'] = jogando
                tabela[[0][0]] = jogando

                # verificando quem esta jogando 
                if jogando == "X":
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementando o contator
                contador += 1

                # verificando se há algum vencedor

                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        vencedor(jogando)

                    # diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        vencedor(jogando)
                    
                    #  empate
                    if contador >= 9:
                        vencedor("Empate")
        
        if i==str(7):
            if b_6['text'] == '': # verificando se a posição esta vazia
                if jogando == 'X':
                    color = cor1
                if jogando == 'O':
                    color = cor2
                
                # cor dotexto do botão que marca a posicção da tabela 
                # com o valor do jogador atual
                b_6['fg'] = color
                b_6['text'] = jogando
                tabela[[0][0]] = jogando

                # verificando quem esta jogando 
                if jogando == "X":
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementando o contator
                contador += 1

                # verificando se há algum vencedor

                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        vencedor(jogando)

                    # diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        vencedor(jogando)
                    
                    #  empate
                    if contador >= 9:
                        vencedor("Empate")
        
        if i==str(8):
            if b_8['text'] == '': # verificando se a posição esta vazia
                if jogando == 'X':
                    color = cor1
                if jogando == 'O':
                    color = cor2
                
                # cor dotexto do botão que marca a posicção da tabela 
                # com o valor do jogador atual
                b_7['fg'] = color
                b_7['text'] = jogando
                tabela[[0][0]] = jogando

                # verificando quem esta jogando 
                if jogando == "X":
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementando o contator
                contador += 1

                # verificando se há algum vencedor

                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        vencedor(jogando)

                    # diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        vencedor(jogando)
                    
                    #  empate
                    if contador >= 9:
                        vencedor("Empate")
        
        if i==str(9):
            if b_8['text'] == '': # verificando se a posição esta vazia
                if jogando == 'X':
                    color = cor1
                if jogando == 'O':
                    color = cor2
                
                # cor dotexto do botão que marca a posicção da tabela 
                # com o valor do jogador atual
                b_8['fg'] = color
                b_8['text'] = jogando
                tabela[[0][0]] = jogando

                # verificando quem esta jogando 
                if jogando == "X":
                    jogando = '0'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'

                # incrementando o contator
                contador += 1

                # verificando se há algum vencedor

                if contador >=5:
                    # linhas
                    if tabela[0][0] == tabela[0][1] == tabela[0][2] != "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2] != "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2] != "":
                        vencedor(jogando)

                    # colunas
                    if tabela[0][0] == tabela[1][0] == tabela[2][0] != "":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2] != "":
                        vencedor(jogando)

                    # diagonais
                    if tabela[0][0] == tabela[1][1] == tabela[2][2] != "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0] != "":
                        vencedor(jogando)
                    
                    #  empate
                    if contador >= 9:
                        vencedor("Empate")


    # decidir o vencedor
    def vencedor():
        pass

    # terminar o jogo
    def terminar():
        pass

        

    #  linhas verticais
    vertical_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'),
                    bg=cor11, fg=cor2)
    vertical_.place(x=100, y=25)
    vertical_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'),
                    bg=cor11, fg=cor2)
    vertical_.place(x=180, y=25)

    # linhas horizontal
    vertical_ = Label(frame_baixo, text=' ', width=190, relief='flat', padx=2, anchor='center', font=('Ivy 1 bold'),
                    bg=cor11, fg=cor2)
    vertical_.place(x=45, y=70)
    vertical_ = Label(frame_baixo, text=' ', width=190, relief='flat', padx=2, anchor='center', font=('Ivy 1 bold'),
                    bg=cor11, fg=cor2)
    vertical_.place(x=45, y=140)

    # botões

    # botões horizontais
    # linha 0
    b_0 = Button(frame_baixo, text=' ', width=4, command=lambda:controlar_jogo('1'), font=('Ivy 15 bold'), overrelief=RIDGE, relief='flat', bg=cor12, fg=cor2)
    b_0.place(x=42, y=27)

    # linha 1
    b_1 = Button(frame_baixo, text=' ', width=5, command=lambda:controlar_jogo('2'),font=('Ivy 15 bold'), overrelief=RIDGE, relief='flat', bg=cor12, fg=cor2)
    b_1.place(x=109, y=27)

    # linha 2
    b_2 = Button(frame_baixo, text=' ', width=4,command=lambda:controlar_jogo('3') ,font=('Ivy 15 bold'), overrelief=RIDGE, relief='flat', bg=cor12, fg=cor2)
    b_2.place(x=188, y=27)

    # linha 3
    b_3 = Button(frame_baixo, text=' ',command=lambda:controlar_jogo('4') ,width=3, height=1,font=('Ivy 21 bold'), overrelief=RIDGE, relief='flat', bg=cor12, fg=cor2)
    b_3.place(x=39, y=80)

    # linha 4
    b_4 = Button(frame_baixo, text=' ',command=lambda:controlar_jogo('5') , width=5, height=2,font=('Ivy 14 bold'), overrelief=RIDGE, relief='flat', bg=cor12, fg=cor2)
    b_4.place(x=109, y=79)

    # linha 5
    b_5 = Button(frame_baixo, text=' ', width=5,command=lambda:controlar_jogo('6'), height=2,font=('Ivy 14 bold'), overrelief=RIDGE, relief='flat', bg=cor12, fg=cor2)
    b_5.place(x=188, y=79)

    # linha 6
    b_6 = Button(frame_baixo, text=' ', width=3,command=lambda:controlar_jogo('7'), height=1,font=('Ivy 21 bold'), overrelief=RIDGE, relief='flat', bg=cor12, fg=cor2)
    b_6.place(x=39, y=150)

    # linha 7
    b_7 = Button(frame_baixo, text=' ', width=5,command=lambda:controlar_jogo('8'), height=2,font=('Ivy 14 bold'), overrelief=RIDGE, relief='flat', bg=cor12, fg=cor2)
    b_7.place(x=109, y=148)

    # linha 8
    b_8 = Button(frame_baixo, text=' ', width=5,command=lambda:controlar_jogo('9'), height=2,font=('Ivy 10 bold'), overrelief=RIDGE, relief='flat', bg=cor12, fg=cor2)
    b_8.place(x=188, y=148)

# BOTÃO JOGAR
b_jogar = Button(frame_baixo, text='Jogar ',width=7,font=('Ivy 14 bold'),command=iniciar_jogo ,overrelief=RIDGE, relief='flat', bg=cor11, fg=cor12)
b_jogar.place(x=95, y=220)


window.mainloop()
