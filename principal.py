# -*- coding: utf-8 -*-
from Tkinter import *
from objetos import *
from random import choice, randint, random
from repertorio import Vetor
from math import *

root = Tk()
root.wm_title('Sinuca')
tela1 = Canvas(root, width=320, height=240)
tela1.pack()


imagem= PhotoImage(file='sinuca0012.gif')
colocarimagem=tela1.create_image(162,120, image=imagem)
titulo=tela1.create_text(165,20, text= "SINUCA viu um jogo como este!", font='Elephant',
                       fill='red')

taco1=[]
contador=0
jogada=True
memoria=True
memsituacao= True
def apertar():
    global taco1, contador, jogada, memoria, memsituacao
    taco1=[]
    contador=0
    jogada=True
    memoria=True
    memsituacao= True
    cores=["blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","blue","red","black"]
    cores2=["brown","green","darkorange","purple","red","blue","gold","black","brown","green","darkorange","purple","red","blue","gold"]
    preptacada=False
    posmouse=Vetor(0,0)
    raiobola=15
    corlado = "green"
    
    def cor(n):
        return cores[n]
    
    def situacao():
        soma=0
        for i in objetos:
            for j in i:
                soma+=abs(j.vel)
        if soma==0:
            return True
        else:
            return False

    def apagar(evento):
        global taco1
        if len(taco1)>0:
            tela.delete(taco1[0])
            taco1.remove(taco1[0])
        

    def tacada(evento):
        click=Vetor(evento.x,evento.y)
        if situacao()==True:
            click=Vetor(evento.x,evento.y)
            direcao=click-objetosbranco[0].pos
            p1=objetosbranco[0].pos+(direcao/abs(direcao))*(objetosbranco[0].raio+5)
            p2=objetosbranco[0].pos+(direcao/abs(direcao))*(objetosbranco[0].raio+300)
            normal=Vetor(direcao.y,-direcao.x)
            v1=p1+(normal/abs(normal))*2
            v2=p1-(normal/abs(normal))*2
            v3=p2+(normal/abs(normal))*7
            v4=p2-(normal/abs(normal))*7
            t=tela.create_polygon(
                v1.x,v1.y,
                v2.x,v2.y,
                v4.x,v4.y,
                v3.x,v3.y,
                fill='brown',outline='brown')
            
            global taco1
            taco1.append(t)
            if len(taco1)>1:
                tela.delete(taco1[0])
                taco1=[taco1[1]]
            
            

    def vez ():
        global jogada
        global memoriadocontadordejogadas1
        global contadordejogadas
        global memsituacao
        if memsituacao==False and situacao()==True:
            if  jogada==True and parametro[0]!=len(objetosazul):
                parametro[0]=len(objetosazul)
                parametro[1]=len(objetosvermelho)
                if len(objetosbranco)==0:
                    BB = Bolabranca(tela, 15, Vetor(950,350),Vetor(0,0),"white")
                    objetosbranco.append(BB)
                    tela.delete(objetosvermelho[0].fig)
                    objetosvermelho.remove(objetosvermelho[0])
                    parametro[1]-=1
            elif jogada==True and parametro[0]==len(objetosazul):
                jogada= False
                parametro[1]=len(objetosvermelho)
                if len(objetosbranco)==0:
                    BB = Bolabranca(tela, 15, Vetor(950,350),Vetor(0,0),"white")
                    objetosbranco.append(BB)
                    tela.delete(objetosvermelho[0].fig)
                    objetosvermelho.remove(objetosvermelho[0])
                    parametro[1]-=1
            elif jogada==False and parametro[1]!=len(objetosvermelho):
                parametro[1]=len(objetosvermelho)
                parametro[0]=len(objetosazul)
                if len(objetosbranco)==0:
                    BB = Bolabranca(tela, 15, Vetor(950,350),Vetor(0,0),"white")
                    objetosbranco.append(BB)
                    tela.delete(objetosazul[0].fig)
                    objetosazul.remove(objetosazul[0])
                    parametro[0]-=1
            elif jogada==False and parametro[1]==len(objetosvermelho):
                jogada= True
                parametro[0]=len(objetosazul)
                if len(objetosbranco)==0:
                    BB = Bolabranca(tela, 15, Vetor(950,350),Vetor(0,0),"white")
                    objetosbranco.append(BB)
                    tela.delete(objetosazul[0].fig)
                    objetosazul.remove(objetosazul[0])
                    parametro[0]-=1
        memsituacao=situacao()

          
    def animar():
        LAPSO = 1.0 / 500
        for i in objetos:
            for ob in i:
                ob.atualizar(LAPSO)
        colidindo()
        batendo()
        sumindo()
        vez()
        cordolado()
        termino()
        janela.after(int(500 * LAPSO), animar)

    def termino():
        global contador
        global tela1
        global imagem1
        global imagem2
        if len(objetosazul)==0 or (jogada==True and len(objetospreto)==0) and contador==0 and situacao()==True:
            imagem1= PhotoImage(file='azul.gif')
            colocarimagem=tela1.create_image(162,120, image=imagem1)
            contador+=1
        if len(objetosvermelho)==0 or (jogada==False and len(objetospreto)==0) and contador==0 and situacao()==True:
            imagem1= PhotoImage(file='vermelho.gif')
            colocarimagem=tela1.create_image(162,120, image=imagem1)
            contador+=1
            
        

    def colidindo():
        LAPSO = 1.0 / 250
        for j in objetos:
            for ob in j:
                j.remove(ob)
                for i in objetosazul+ objetosvermelho+ objetosbranco+ objetospreto :
                    if abs(i.pos-ob.pos)<=i.raio+ob.raio:
                        choque=i.pos-ob.pos
                        plano=Vetor(choque.y,-choque.x)
                        erro=i.raio+ob.raio-abs(choque)
                        i.pos= i.pos+choque/abs(choque)*0.51*erro
                        ob.pos=ob.pos-choque/abs(choque)*0.51*erro
                        i.vel, ob.vel=i.vel.projetar(plano)+ob.vel.projetar(choque),i.vel.projetar(choque)+ob.vel.projetar(plano)
                j.append(ob)

    def tacando(evento):
        global taco1
        global contadordejogadas
        if situacao()==True:
            click=Vetor(evento.x,evento.y)
            direcao=objetosbranco[0].pos-click
            if abs(direcao)<=320:
                objetosbranco[0].vel+=30*direcao
                if len(taco1)==1:
                    tela.delete(taco1[0])
                    taco1.remove(taco1[0])
            

    def adicionarBolap(x,y,i):
        r = raiobola
        p = Vetor(x, y)
        v = Vetor(0, 0)
        b = Bola(tela, r, p, v, cor(i))   
        if i==14:
            objetospreto.append(b)
        elif i%2==0:
            objetosazul.append(b)
        else:
            objetosvermelho.append(b)

    def comecar():
        contador=0
        for i in range(0,5):
            for j in range((5-i),0,-1):
                adicionarBolap((300+i*raiobola*(3**0.5)),(260+j*2*raiobola+i*raiobola),contador)
                contador+=1

    def batendo():
        for i in objetosazul+ objetosvermelho+ objetosbranco+ objetospreto :
                for j in cantos:
                    if abs(i.pos-j.pos) <= i.raio+j.raio:
                        choque=i.pos-j.pos
                        plano=Vetor(choque.y,-choque.x)
                        erro=i.raio+j.raio-abs(choque)
                        i.pos= i.pos+choque/abs(choque)*0.51*erro
                        i.vel = i.vel.projetar(plano)-i.vel.projetar(choque)

    def sumindo():
        for i in objetos:
            for ob in i:
                if i==objetosbranco:
                    for j in buracos:
                        if abs(ob.pos-j.pos) <= j.raio:
                            ob.buraco = j
                            if abs(ob.pos-j.pos) <= (j.raio/10):
                                ob.buraco = None
                                tela.delete(ob.fig)
                                i.remove(ob)
                else:
                    for j in buracos:
                        if abs(ob.pos-j.pos) <= j.raio:
                            ob.buraco = j
                            if abs(ob.pos-j.pos) <= (j.raio/10):
                                i.remove(ob)
                                tela.delete(ob.fig)
                            
                        
    parametro= [ 7,7 ]
    objetosazul = []
    objetosvermelho = []
    objetosbranco = []
    objetospreto = []
    objetos= [objetosazul, objetosvermelho, objetosbranco, objetospreto]
    taco1 = []
    taco2 = []
    janela = Tk()
    janela.wm_title('Sinuca')
    tela = Canvas(janela, width=1280, height=700)
    fundo = tela.create_polygon(115,5,1165,5,1165,635,115,635,fill='darkred')
    mesa = tela.create_polygon(128,28,1152,28,1152,612,128,612,fill='darkgreen')

    
    def cordolado():
        global memoria
        global contadordejogadas
        global memoriadocontadordejogadas
        if memoria!=jogada :
            if jogada==True:
                constroi('blue')
            if jogada==False:
                constroi('red')
            memoria=jogada
        
            

    def constroi(corlado):
        lado1 = tela.create_polygon(199,28,595,28,595,65,199,65,fill=corlado)
        arc11 = tela.create_arc(166,-9,255,65,fill=corlado, outline=corlado, start=180, extent=82)
        arc12 = tela.create_arc(570,-9,616,65,fill=corlado, outline=corlado, start=278, extent=82)
        lado2 = tela.create_polygon(1081,28,682,28,682,65,1081,65,fill=corlado)
        arc21 = tela.create_arc(1030,-9,1117,65,fill=corlado, outline=corlado, start=280, extent=80)
        arc22 = tela.create_arc(661,-9,707,65,fill=corlado, outline=corlado, start=180, extent=82)
        lado3 = tela.create_polygon(199,612,595,612,595,575,199,575,fill=corlado)
        arc31 = tela.create_arc(166,574,255,648,fill=corlado, outline=corlado, start=98, extent=82)
        arc32 = tela.create_arc(570,574,616,648,fill=corlado, outline=corlado, start=0, extent=82)
        lado4 = tela.create_polygon(1079,612,682,612,682,575,1079,575,fill=corlado)
        arc41 = tela.create_arc(1030,574,1116,648,fill=corlado, outline=corlado, start=0, extent=82)
        arc42 = tela.create_arc(661,574,707,648,fill=corlado, outline=corlado, start=98, extent=82)
        lado5 = tela.create_polygon(128,92,154,92,154,547,128,547,fill=corlado)
        arc51 = tela.create_arc(102,62,154,132,fill=corlado, outline=corlado, start=10, extent=80)
        arc52 = tela.create_arc(102,508,154,578,fill=corlado, outline=corlado, start=270, extent=82)
        lado6 = tela.create_polygon(1152,92,1126,92,1126,547,1152,547,fill=corlado)
        arc61 = tela.create_arc(1125,62,1177,132,fill=corlado, outline=corlado, start=90, extent=80)
        arc62 = tela.create_arc(1125,508,1177,578,fill=corlado, outline=corlado, start=188, extent=82)
        
    tela.pack()
    canto1 = Canto(tela,32,Vetor(202,32))
    canto2 = Canto(tela,32,Vetor(581,32))
    canto3 = Canto(tela,32,Vetor(1078,32))
    canto4 = Canto(tela,32,Vetor(697,32))
    canto5 = Canto(tela,32,Vetor(200,609))
    canto6 = Canto(tela,32,Vetor(583,609))
    canto7 = Canto(tela,32,Vetor(1080,609))
    canto8 = Canto(tela,32,Vetor(695,609))
    canto9 = Canto(tela,26,Vetor(125,92))
    canto10 = Canto(tela,26,Vetor(125,548))
    canto11 = Canto(tela,26,Vetor(1154,92))
    canto12 = Canto(tela,26,Vetor(1154,548))
    cantos = [canto1,canto2,canto3,canto4,canto5,canto6,canto7,canto8,canto9,canto10,canto11,canto12]
    buraco1 = Cacapa(tela, 25, Vetor(145,45))
    buraco2 = Cacapa(tela, 25, Vetor(640,35))
    buraco3 = Cacapa(tela, 25, Vetor(1135,45))
    buraco4 = Cacapa(tela, 25, Vetor(145,595))
    buraco5 = Cacapa(tela, 25, Vetor(640,605))
    buraco6 = Cacapa(tela, 25, Vetor(1135,595))
    buracos = [buraco1,buraco2,buraco3,buraco4,buraco5,buraco6]
    BB = Bolabranca(tela, 15, Vetor(950,350),Vetor(0,0),"white")
    objetosbranco.append(BB)
    comecar()
    constroi('blue')



    tela.bind('<Button-2>', apagar)
    tela.bind('<Button-3>', tacada)

    tela.bind('<Button-1>', tacando)
    animar() 
    janela.mainloop()

def apertar2():
    def constroi(corlado):
        lado1 = tela2.create_polygon(199,28,595,28,595,65,199,65,fill=corlado)
        arc11 = tela2.create_arc(166,-9,255,65,fill=corlado, outline=corlado, start=180, extent=82)
        arc12 = tela2.create_arc(570,-9,616,65,fill=corlado, outline=corlado, start=278, extent=82)
        lado2 = tela2.create_polygon(1081,28,682,28,682,65,1081,65,fill=corlado)
        arc21 = tela2.create_arc(1030,-9,1117,65,fill=corlado, outline=corlado, start=280, extent=80)
        arc22 = tela2.create_arc(661,-9,707,65,fill=corlado, outline=corlado, start=180, extent=82)
        lado3 = tela2.create_polygon(199,612,595,612,595,575,199,575,fill=corlado)
        arc31 = tela2.create_arc(166,574,255,648,fill=corlado, outline=corlado, start=98, extent=82)
        arc32 = tela2.create_arc(570,574,616,648,fill=corlado, outline=corlado, start=0, extent=82)
        lado4 = tela2.create_polygon(1079,612,682,612,682,575,1079,575,fill=corlado)
        arc41 = tela2.create_arc(1030,574,1116,648,fill=corlado, outline=corlado, start=0, extent=82)
        arc42 = tela2.create_arc(661,574,707,648,fill=corlado, outline=corlado, start=98, extent=82)
        lado5 = tela2.create_polygon(128,92,154,92,154,547,128,547,fill=corlado)
        arc51 = tela2.create_arc(102,62,154,132,fill=corlado, outline=corlado, start=10, extent=80)
        arc52 = tela2.create_arc(102,508,154,578,fill=corlado, outline=corlado, start=270, extent=82)
        lado6 = tela2.create_polygon(1152,92,1126,92,1126,547,1152,547,fill=corlado)
        arc61 = tela2.create_arc(1125,62,1177,132,fill=corlado, outline=corlado, start=90, extent=80)
        arc62 = tela2.create_arc(1125,508,1177,578,fill=corlado, outline=corlado, start=188, extent=82)
    janelinha = Tk()
    janelinha.wm_title('Instrucoes')
    tela2 = Canvas(janelinha, width=1280, height=700)
    tela2.pack()
    fundo = tela2.create_polygon(115,5,1165,5,1165,635,115,635,fill='darkred')
    mesa = tela2.create_polygon(128,28,1152,28,1152,612,128,612,fill='darkgreen')
    buraco1 = Cacapa(tela2, 25, Vetor(145,45))
    buraco2 = Cacapa(tela2, 25, Vetor(640,35))
    buraco3 = Cacapa(tela2, 25, Vetor(1135,45))
    buraco4 = Cacapa(tela2, 25, Vetor(145,595))
    buraco5 = Cacapa(tela2, 25, Vetor(640,605))
    buraco6 = Cacapa(tela2, 25, Vetor(1135,595))
    frase=tela2.create_text(600,300, text= "Segue abaixo as instruções da Sinuca:\n \nComandos:\n - Botão direito do mouse cria o taco \n - Botão"
                            +" scroll do mouse apaga o taco \n - Botão esquerdo faz a jogada (quanto mais longe da bola mais forte)\n\n"
                            +"Instruções: \n- Jogador azul ganha se todas as bolas azuis forem encaçapadas ou se o vermelho encaçapar a preta \n"
                            +"- Jogador vermelho ganha se todas as bolas vermelhas forem encaçapadas ou se o azul encaçapar a preta\n"
                            +"- Se encaçapar a bola branca, uma bola aleatória do adversário sumirá e a branca retorna à posição de origem \n"
                            +'- Se um jogador encaçapar uma bola de sua cor, ele joga novamente\n'
                            +"- A cor da borda indica quem joga \n- Se um jogador encaçapar uma bola de sua cor, ele joga novamente\n"
                            +'- Se não tem bola azul, vermelha ou preta, retorne ao menu e veja quem ganhou', font='Elephant',
                       fill='black')
    constroi("green")
    
    
botao2=Button(tela1, text="Instruções", command = apertar2, height = 5, width= 10 ,fg = "blue", background= 'green')
botao2.place(x=180, y=200, width=100, height=40)
botao=Button(tela1, text="Jogar", command = apertar, height = 5, width= 10 ,fg = "blue", background= 'green')
botao.place(x=40, y=200, width=100, height=40)
root.mainloop()
