# -*- coding: utf-8 -*-
"""SDES.py
"""

def P10(K):
  P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
  
  K_ = list()
  for i in range(0, len(K)):
    K_.append(K[int(P10[i]) - 1])
  return K_

def P8(key):
  P8 = [6, 3, 7, 4, 8, 5, 10, 9]
  K = key[2:]
  K_ = list()
  for i in range(0, len(K)):
    K_.append(K[int(P8[i])-3])
  return K_

def shift(K):
  K_ = list()
  for i in range(1,len(K)):
    K_.append(K[i])
  K_.append(K[0])
  return K_

def gerar_chaves(chave):
  #permutacao inicial
  k_p10 = P10(chave)
  
  #divide a chave em duas chaves que serão usadas tanto para gerar k1 quanto k2
  k_p10_1 = k_p10[:int(len(k_p10)/2)]
  k_p10_2 = k_p10[int(len(k_p10)/2):]

  #rotaciona as chaves divididas uma vez para a esquerda 
  k_shift_1= shift(k_p10_1)
  k_shift_2= shift(k_p10_2)
  
  #une as chaves após o LS-1
  k_shift = k_shift_1 + k_shift_2
  
  #Passa pela regua P8 pra gerar k1
  k1 = P8(k_shift)
 
  
  #rotaciona as chaves divididas duas vezes para a esquerda 
  k2_shift_1 = shift(shift(k_shift_1))
  k2_shift_2 = shift(shift(k_shift_2))
  
  #une as chaves rotacionadas
  k2_shift = k2_shift_1 + k2_shift_2
  
  #passa pela regua P8 para gerar k2
  k2 = P8(k2_shift)

  return k1, k2

def IP (texto):
  PI = [2, 6, 3, 1, 4, 8, 5, 7]
  texto_ = list()
  for i in range(0,8):
    texto_.append(texto[int(PI[i]) - 1])
  return texto_[:int(len(texto_)/2)], texto_[int(len(texto_)/2):]

def IP_inversa(texto):
  PI_inverso = [4, 1, 3, 5, 7, 2, 8, 6]

  texto_ = list()
  for i in range(0,8):
    texto_.append(texto[int(PI_inverso[i]) - 1])
  
  return texto_[:int(len(texto_)/2)], texto_[int(len(texto_)/2):]

def P4(bits):
  P4 = [2,4,3,1]
  bits_  = list()
  for i in range (0,len(P4)):
    bits_.append(bits[int(P4[i]) - 1])
  return bits_

 
def EP(bits):
  EP = [4,1,2,3,2,3,4,1]
  bits_  = list()
  for i in range (0,len(EP)):
    bits_.append(bits[int(EP[i]) - 1])
  return bits_



def xor(x1, x2):
  result_xor = list()
  for i in range(0, 8):
    result_xor.append(int(x1[i]) ^ int(x2[i]))
  return result_xor



def encriptar(texto_claro, chave):
  #gerando chaves
  
  k1,k2 = gerar_chaves(chave)
  print("K1: ", k1)
  print("K2: ", k2)

  
  print()
  #gerando texto cifrado
  L,R = IP(texto_claro)

  print("Resultado do IP com 8 bits:")
  print("L : ", L)
  print("R : ", R)
  print()
  ep = EP(R)
  print("Resultado do EP (em F em fk): ", ep)
  print()
  
  #XOR ep com k1
  result_xor = xor(ep, k1)
  print("Resultado do XOR entre o retorno da EP e K1", result_xor)



def descriptar(texto_cifrado, chave):
  #gerando chaves
  k_p10 = P10(chave)
  k_shift= shift(k_p10)
  k1 = P8(k_shift)
  k2_shift = shift(k_shift)
  k2 = P8(k2_shift)
  
  #gerando texto claro
  texto_ip = IP(texto_cifrado)
  texto_fk2 = fk(texto_ip,k2)
  texto_sw = sw(texto_fk2)
  texto_fk1 = fk(texto_ip,k1)
  texto_claro = IP_inversa(texto_fk1)  
  return texto_claro


