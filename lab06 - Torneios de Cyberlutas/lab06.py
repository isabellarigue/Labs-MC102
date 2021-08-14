class Medalutador:
   def __init__(self, ID, H, Hi, K, BonusA, BonusD, T, Bd, Be, P, Medapeca= 'D2'):
      self.ID = ID
      self.H = H  #valor da habilidade inicial, mas que pode ser alterado devido às batalhas
      self.Hi = H #valor da habilidade inicial, que não irá ser modificado, para possibilitar comparações
      self.K = K
      self.BonusA = BonusA
      self.BonusD = BonusD
      self.T = T
      self.Bd = Bd
      self.Be = Be
      self.P = P
      self.Medapeca = Medapeca #valor qualquer que irá ser alterado

   def obter_ID(self):
      return self.ID

   def obter_H(self):
      return self.H

   def obter_Hi(self):
      return self.Hi

   def obter_BonusA(self):
      return self.BonusA

   def obter_BonusD(self):
      return self.BonusD

   def obter_T(self):
      return self.T[0]

   def obter_Bd(self):
      return self.Bd[0]

   def obter_Be(self):
      return self.Be[0]

   def obter_P(self):
      return self.P[0]

   def obter_K(self):
      return self.K

   def obter_ataque (self):
     A = self.BonusA + self.Bd[0] + self.Be[0]
     return A

   def obter_defesa (self):
     D = self.BonusD + self.T[0] + self.P[0]
     return D 

   def obter_Medapeca(self):
      return self.Medapeca

   def altera_H (self, novo_H):
      self.H = novo_H

   def altera_Medapeca (self, nova_Medapeca):
      self.Medapeca = nova_Medapeca

   def adiciona_T (self, novo_T):
      self.T.append(novo_T)
      self.T = ordena (self.T)

   def remove_T (self):
      self.T.pop(0)

   def adiciona_Be (self, novo_Be):
      self.Be.append(novo_Be)
      self.Be = ordena (self.Be)

   def remove_Be (self):
      self.Be.pop(0)

   def adiciona_Bd (self, novo_Bd):
      self.Bd.append(novo_Bd)
      self.Bd = ordena (self.Bd)

   def remove_Bd (self):
      self.Bd.pop(0)

   def adiciona_P (self, novo_P):
      self.P.append(novo_P)
      self.P = ordena (self.P)

   def remove_P (self):
      self.P.pop(0)


class Torneio (Medalutador):
  def __init__ (self):
    self.lista_de_medalutadores = []

  def adiciona_medalutador (self, medalutador):
    self.lista_de_medalutadores.append(medalutador)


def ordena (lista):
  ''' Ordena os valores de uma lista de forma decrescente.'''
  lista1 = []
  for x in lista:
    lista1.append(x)
  lista_ordenada = sorted(lista1, reverse=True)
  return lista_ordenada

#separando os dados:
contador = 0
torneio = Torneio ()
n = int(input()) #entrada numero medalutadores
lista1 = []
lista2 = []
torso = []
b_esquerdo = []
b_direito = []
pernas = []
while contador < n:
    lista1.append (str(input())) #entrada H, K, M
    separados = lista1[contador].split(' ')
    habilidade = int(separados[0])
    recuperacao = int(separados[1])
    num_medapecas = int(separados[2])
    num = 0
    bonus = str(input())
    separar = bonus.split(' ')
    bonus_ataque = int(separar [0])
    bonus_defesa = int(separar [1])
    while num < num_medapecas:
        lista2.append (str(input())) #entrada medapeças
        separados2 = lista2[num].split(' ')
        if separados2[0] == 'T':
            torso.append(int(separados2[1]))
        elif separados2[0] == 'D':
            b_direito.append(int(separados2[1])) 
        elif separados2[0] == 'E':
            b_esquerdo.append(int(separados2[1]))
        else: #pernas
            pernas.append(int(separados2[1]))
        num +=1
    
    medalutador = Medalutador (ID = contador+1, H= habilidade, Hi= habilidade, K= recuperacao, BonusA= bonus_ataque, BonusD= bonus_defesa, T=ordena(torso), Bd=ordena(b_direito), Be=ordena(b_esquerdo), P=ordena(pernas) )
    torneio.adiciona_medalutador(medalutador)

    lista2.clear()
    torso.clear()
    b_direito.clear()
    b_esquerdo.clear()
    pernas.clear()
    contador += 1   

def medapeca_ganha (vencedor, perdedor):
    '''Define qual medapeca é de mais vantajosa para o vencedor. Retira tal medapeca do perdedor e dá ao vencedor.'''
    torso = perdedor.obter_T() - vencedor.obter_T()
    braco_esquerdo = perdedor.obter_Be() - vencedor.obter_Be()
    braco_direito = perdedor.obter_Bd() - vencedor.obter_Bd()
    pernas = perdedor.obter_P() - vencedor.obter_P()
    if torso >= braco_esquerdo and torso >= braco_direito and torso >= pernas:
        vencedor.altera_Medapeca('T'+ str(perdedor.obter_T()))
        vencedor.adiciona_T(perdedor.obter_T())
        perdedor.remove_T()
    elif braco_esquerdo > torso and braco_esquerdo >= braco_direito and braco_esquerdo >= pernas:
        vencedor.altera_Medapeca('E'+ str(perdedor.obter_Be()))
        vencedor.adiciona_Be(perdedor.obter_Be())
        perdedor.remove_Be()
    elif braco_direito > torso and braco_direito > braco_esquerdo and braco_direito >= pernas:
        vencedor.altera_Medapeca('D'+ str(perdedor.obter_Bd()))
        vencedor.adiciona_Bd(perdedor.obter_Bd())
        perdedor.remove_Bd()
    else: #pernas é maior
        vencedor.altera_Medapeca('P'+ str(perdedor.obter_P()))
        vencedor.adiciona_P(perdedor.obter_P())
        perdedor.remove_P()   

def batalhar (i, j):
   '''Faz a batalha entre os medalutadores i e j, define quem vence e perde, e altera as habilidades e as medapecas conforme isso.'''
   if (i.obter_ataque() > j.obter_defesa() or j.obter_ataque() > i.obter_defesa()) and (i.obter_ataque() - j.obter_defesa()) != (j.obter_ataque() - i.obter_defesa()):
      if (i.obter_ataque() - j.obter_defesa()) > (j.obter_ataque() - i.obter_defesa()):
         vencedor = i
         perdedor = j
      else:
         vencedor = j
         perdedor = i
   elif i.obter_H() != j.obter_H():
      if i.obter_H() > j.obter_H():
         vencedor = i
         perdedor = j
      else:
         vencedor = j 
         perdedor = i
   else:
      if i.obter_ID() < j.obter_ID():
         vencedor = i
         perdedor = j
      else:
         vencedor = j
         perdedor = i 

   if vencedor.obter_H() >= perdedor.obter_H():
      vencedor.altera_H(vencedor.obter_H() - perdedor.obter_H())
   else:
      vencedor.altera_H(0)

   perdedor.altera_H(perdedor.obter_H()//2)

   if vencedor.obter_H() + vencedor.obter_K() < vencedor.obter_Hi():
      vencedor.altera_H(vencedor.obter_H() + vencedor.obter_K())
 
   else:
      vencedor.altera_H(vencedor.obter_Hi())


   if perdedor.obter_H() + perdedor.obter_K() < perdedor.obter_Hi():
      perdedor.altera_H(perdedor.obter_H() + perdedor.obter_K())
   else:
      perdedor.altera_H(perdedor.obter_Hi())

   medapeca_ganha (vencedor, perdedor)

   return vencedor 

def imprimir_ficha_tecnica (i,j):
    print(f'\tA{i.obter_ID()} = E{i.obter_Be()} + D{i.obter_Bd()} + {i.obter_BonusA()} = {i.obter_ataque()}')
    print(f'\tD{i.obter_ID()} = T{i.obter_T()} + P{i.obter_P()} + {i.obter_BonusD()} = {i.obter_defesa()}')
    print(f'\tH{i.obter_ID()} = {i.obter_H()}')
    print(f'\tA{j.obter_ID()} = E{j.obter_Be()} + D{j.obter_Bd()} + {j.obter_BonusA()} = {j.obter_ataque()}')
    print(f'\tD{j.obter_ID()} = T{j.obter_T()} + P{j.obter_P()} + {j.obter_BonusD()} = {j.obter_defesa()}')
    print(f'\tH{j.obter_ID()} = {j.obter_H()}')
   
def imprimir_resultado_da_batalha (k):
    print(f'Medalutador {k.obter_ID()} venceu e recebeu a {k.obter_Medapeca()}\n')

def simular_torneios_de_cyberlutas(lista_de_medalutadores):
  lista_torneio_principal = []
  lista_de_repescagem     = []
  for medalutador in lista_de_medalutadores:
    lista_torneio_principal.append(medalutador)
  while len(lista_torneio_principal) >= 2 or len(lista_de_repescagem) >= 2:
    lista_torneio_principal = aplicar_rodada_de_batalhas(lista_torneio_principal, lista_de_repescagem)
    lista_de_repescagem     = aplicar_rodada_de_batalhas(lista_de_repescagem, None)
  i = lista_torneio_principal.pop(0)
  j = lista_de_repescagem.pop(0)
  print('Cyberluta Final')
  print(f'Medalutadores: {i.obter_ID()} vs {j.obter_ID()}')
  imprimir_ficha_tecnica(i, j)
  k = batalhar(i, j)
  print(f'Campeao: medalutador {k.obter_ID()}')

def aplicar_rodada_de_batalhas(lista_de_medalutadores, lista_de_repescagem):
  if len(lista_de_medalutadores) < 2:
    return lista_de_medalutadores
  lista_de_vencedores = []
  while len(lista_de_medalutadores) >= 2:
    i = lista_de_medalutadores.pop(0) 
    j = lista_de_medalutadores.pop(0)
    if i.obter_ID() > j.obter_ID():
      i, j = j, i
    if lista_de_repescagem != None:
      print('Cyberluta do Torneio Principal')
    else:
      print('Cyberluta da Repescagem')
    print(f'Medalutadores: {i.obter_ID()} vs {j.obter_ID()}')
    imprimir_ficha_tecnica(i, j)
    k = batalhar(i, j)
    imprimir_resultado_da_batalha(k)
    if lista_de_repescagem != None:
      if i == k:
        lista_de_repescagem.append(j)
      else:
        lista_de_repescagem.append(i)
    lista_de_vencedores.append(k)
  lista_de_vencedores.extend(lista_de_medalutadores)
  return lista_de_vencedores

simular_torneios_de_cyberlutas(torneio.lista_de_medalutadores)