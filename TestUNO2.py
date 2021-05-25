import unittest
import nose.tools
import random
from parameterized import parameterized, parameterized_class
from Gerenciador import Gerenciador
from Baralho import Carta


#ATC1 - [Inicio, Espera Jogada, Skip, Espera Jogada, Skip, Espera Jogada, +4, Espera Jogada, +4, Espera Jogada, Skip, Espera Jogada, Número, Espera Jogada, Número, Espera Jogada, Wild, Espera Jogada, +2, Espera Jogada,+2, Espera Jogada, Reverse, Espera Jogada, Skip, Fim] Satisfaz Trs: 01, 07, 09, 08, 11, 12, 13, 19, 20, 21, 25, 26, 27, 31, 34, 41, 43, 48, 49, 50, 51;

@parameterized_class(('carta1','carta2','carta3','carta4','carta5','carta6','carta7','carta8','carta9','carta10','carta11','carta12'),#ATC1 - [Inicio, Espera Jogada, Skip, Espera Jogada, Skip, Espera Jogada, +4, Espera Jogada, +4, Espera Jogada, Skip, Espera Jogada, Número, Espera Jogada, Número, Espera Jogada, Wild, Espera Jogada, +2, Espera Jogada,+2, Espera Jogada, Reverse, Espera Jogada, Skip, Fim]
  [
    ("pula", "pula", "+4", "+4",  "pula" , "5", "5", "escolhacor", "+2","+2", "reverso", "pula"),  
    ("pula", "pula", "+4", "+4",  "pula" , "5", "5", "escolhacor", "+2","+2", "reverso", "pula"),   
    #(True,2,True,True)
  ])


class TestUNO2(unittest.TestCase):
 ##OUTRO MODO DE TESTE##

    def TesteGerenciador1(self):
        
        #Prepara as mãos dos jogadores. Esses irão descartar a primeira carta disponível percorrendo o caminho definido pelo teste
    #Teste do início
        gerenciador = Gerenciador()
        gerenciador.inicializarJogo()
        gerenciador.jogadores[0].cartas.clear()
        gerenciador.jogadores[1].cartas.clear()
        if gerenciador.calcularProxJogador==1:
            atual=1
            prox=0
        else:
            atual=0
            prox=1

        #Teste das cartas
        gerenciador.jogadores[prox].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta1))
        retorno=gerenciador.acaoJogada(prox,gerenciador.jogadores[prox].cartas[0])
        self.assertEqual(retorno, self.carta1)
        
        gerenciador.jogadores[prox].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta2))
        retorno=gerenciador.acaoJogada(prox,gerenciador.jogadores[prox].cartas[0])
        self.assertEqual(retorno, self.carta2)
        gerenciador.jogadores[prox].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta3))
        retorno=gerenciador.acaoJogada(prox,gerenciador.jogadores[prox].cartas[0])
        self.assertEqual(retorno, self.carta3)
        gerenciador.jogadores[prox].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta4))
        retorno=gerenciador.acaoJogada(prox,gerenciador.jogadores[prox].cartas[0])
        self.assertEqual(retorno, self.carta4)
        gerenciador.jogadores[prox].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta5))
        retorno=gerenciador.acaoJogada(prox,gerenciador.jogadores[prox].cartas[0])
        self.assertEqual(retorno, self.carta5)
        gerenciador.jogadores[prox].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta6))
        retorno=gerenciador.acaoJogada(prox,gerenciador.jogadores[prox].cartas[0])
        self.assertEqual(retorno, self.carta6)

        gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta7))
        retorno=gerenciador.acaoJogada(atual,gerenciador.jogadores[atual].cartas[0])
        self.assertEqual(retorno, self.carta7)

        gerenciador.jogadores[prox].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta8))
        retorno=gerenciador.acaoJogada(prox,gerenciador.jogadores[prox].cartas[0])
        self.assertEqual(retorno, self.carta8)

        gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta9))
        retorno=gerenciador.acaoJogada(atual,gerenciador.jogadores[atual].cartas[0])
        self.assertEqual(retorno, self.carta9)
        gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta10))
        retorno=gerenciador.acaoJogada(atual,gerenciador.jogadores[atual].cartas[0])
        self.assertEqual(retorno, self.carta10)
        gerenciador.jogadores[atual].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta11))
        retorno=gerenciador.acaoJogada(atual,gerenciador.jogadores[atual].cartas[0])
        self.assertEqual(retorno, self.carta11)

        gerenciador.jogadores[prox].cartas.append(Carta(gerenciador.pilha_mesa[0].cor,self.carta12))
        retorno=gerenciador.acaoJogada(prox,gerenciador.jogadores[prox].cartas[0])
        self.assertEqual(retorno, self.carta12)
        gerenciador.verificarVencedor(gerenciador.jogadores[prox])

unittest.main(argv=[''], verbosity=2, exit=False)





