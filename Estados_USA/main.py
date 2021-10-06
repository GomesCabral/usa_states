import turtle
import pandas


screen = turtle.Screen()
screen.title('Estados de USA')

#MUDAR O FUNDO
screen.addshape('blank_states_img.gif')
turtle.shape('blank_states_img.gif')
estados_certos = []


dados = pandas.read_csv('50_states.csv')
cidades = dados.state.to_list()

while len(estados_certos) < 50:
    resposta = screen.textinput(title=f'{len(estados_certos)}/50', prompt='Qual é o proximo Estado?').title()
    posicao = dados[dados.state == resposta]

    if resposta == 'Exit':
        estados_falhados = []
        for estado in cidades:
            if estado not in estados_certos:
                estados_falhados.append(estado)
        #CRIAR FICHEIRO CSV
        novos_dados = pandas.DataFrame(estados_falhados)
        novos_dados.to_csv('estados_a_aprender')

        break
    #SÓ É POSSIVEL USAR 'IN' SE CONVERTER AS CIDADES EM LISTA
    if resposta in cidades:
        estados_certos.append(resposta)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(posicao.x), int(posicao.y))
        t.write(resposta)