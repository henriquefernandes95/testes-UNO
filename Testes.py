import unittest
import nose.tools
import random
from parameterized import parameterized, parameterized_class
from Gerenciador import Gerenciador
from Baralho import Carta
#Organiza as múltiplas entradas com o parameterized para as execuções
# Parametros em Pair-wise para testSelecionarCarta

#ATC1 - [Inicio, Espera Jogada, Skip, Espera Jogada, Skip, Espera Jogada, +4, Espera Jogada, +4, Espera Jogada, Skip, Espera Jogada, Número, Espera Jogada, Número, Espera Jogada, Wild, Espera Jogada, +2, Espera Jogada,+2, Espera Jogada, Reverse, Espera Jogada, Skip, Fim] Satisfaz Trs: 01, 07, 09, 08, 11, 12, 13, 19, 20, 21, 25, 26, 27, 31, 34, 41, 43, 48, 49, 50, 51;

@parameterized_class(('carta1','carta2','carta3','carta4','carta5','carta6','carta7','carta8','carta9','carta10','carta11','carta12'),#ATC1 - [Inicio, Espera Jogada, Skip, Espera Jogada, Skip, Espera Jogada, +4, Espera Jogada, +4, Espera Jogada, Skip, Espera Jogada, Número, Espera Jogada, Número, Espera Jogada, Wild, Espera Jogada, +2, Espera Jogada,+2, Espera Jogada, Reverse, Espera Jogada, Skip, Fim]
  [
    ("pula", "pula", "+4", "+4",  "pula" , "5", "5", "escolhacor", "+2","+2", "reverso", "pula"),    
    #(True,2,True,True)
  ])
class TestUNO0(unittest.TestCase):
  def testSelecionarCarta(self):

    #Prepara as mãos dos jogadores. Esses irão descartar a primeira carta disponível percorrendo o caminho definido pelo teste
    #Teste do início
    gerenciador = Gerenciador()
    gerenciador.inicializarJogo()
    gerenciador.jogadores[0].cartas.clear()
    gerenciador.jogadores[1].cartas.clear()
    if gerenciador.calcularProxJogador==1:
        atual=0
        not_atual=1
    else:
        atual=1
        not_atual=0

    #Teste das cartas
    gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta1))
    gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta2))
    gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta3))
    gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta4))
    gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta5))
    gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta6))

    gerenciador.jogadores[not_atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta7))

    gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta8))

    gerenciador.jogadores[not_atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta9))
    gerenciador.jogadores[not_atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta10))
    gerenciador.jogadores[not_atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta11))

    gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta12))

        #gerenciador.jogadores[i].cartas.append(Carta())
    #gerenciador.jogadores[gerenciador.atual_jogador].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta1))
    #print(gerenciador.jogadores[gerenciador.atual_jogador].cartas)
    gerenciador.gerenciarJogo()
    




   



## Parametros em All-combinations para testCompraCarta
#@parameterized_class(('monteVazio','mesaTam','specCompra'),
#  [
#    (True,9,True),# (q1b1, q2b1) Monte de compra vazio e mais do que uma carta na mesa
#    (True,1,False),# (q1b1, q2b2) Monte de compra vazio e somente uma carta na mesa
#    (False,9,True),# (q1b2, q2b1) Monte de compra não vazio e mais do que uma carta na mesa
#    (False,1,True),# (q1b2, q2b2) Monte de compra não vazio e somente uma carta na mesa 
#  ])
#class TestUNOCompraCarta(unittest.TestCase):
#  def testCompraCarta(self):
#    monte = Monte()
#    mesa = Mesa(monte)
#    maoTeste = Mao(monte)
#    monte._monte = []
#    mesa._mesa = []
#    carta1 = Carta('azul',"0")
#    if not(self.monteVazio):
#      monte._monte.append(carta1)
#    for i in range(0,self.mesaTam):
#      mesa._mesa.append(carta1)
#    if self.specCompra:
#      retornoEsperado = carta1
#    else:
#      retornoEsperado = Carta('null', "null")
#    comprada = maoTeste.comprarCarta(monte, mesa)
#    self.assertEqual(comprada.cor,retornoEsperado.cor)
#    self.assertEqual(comprada.tipo,retornoEsperado.tipo)


## Parametros em Each-Choice para testJogarCarta
#@parameterized_class(('maoTam','possuiCarta','specJogar'),
#  [
#    (9,True,True),# (q1b1,q2b1) Mais do que duas cartas na mão e com cartas possíveis de se jogar 
#    (2,False,False),# (q1b2,q2b2) Somente duas cartas na mão e sem cartas possíveis de se jogar
#    (1,True,True),# (q1b3,q2b1) Somente uma carta na mão e com carta possível de se jogar
#  ])
#class TestUNOJogarCarta(unittest.TestCase):
#  def testJogarCarta(self):
#    monte = Monte()
#    mesa = Mesa(monte)
#    maoTeste = Mao(monte)
#    monte._monte = []
#    mesa._mesa = []
#    maoTeste._mao=[]
#    carta1 = Carta('azul',"0")
#    carta2 = Carta('verde',"1")
#    mesa.empilhaMesa(carta1)
#    if self.possuiCarta:
#      for i in range(self.maoTam):
#        maoTeste._mao.append(carta1)
#    else:
#      for i in range(self.maoTam):
#        maoTeste._mao.append(carta2)
#    if self.specJogar:
#      retornoEsperado = 1
#    else:
#      retornoEsperado = 0
#    self.assertEqual(maoTeste.jogarCarta(mesa, monte),retornoEsperado)
unittest.main(argv=[''], verbosity=2, exit=False)



