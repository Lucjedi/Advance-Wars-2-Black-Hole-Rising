#!/usr/bin/python
import sys
import binascii
import os
print ('---------------------------------------')

def pressexit():
   raw_input('Aperte ENTER para sair...')
def dump():
   global languageselect
   global offset
   ## Verifica arquivo de entrada

   table = {}
   try:
       for i in mapa.readlines():
           table[i.split(';')[0]] = i.split(';')[1]
           mapa.close
   except:
       print ('Erro ao criar a tabela para extrair.')
       sys.exit(0)

   #gravandodump = open('dump.txt', 'w')
   gravandodump = open(raw_input("Insira o nome do arquivo a ser extra\xeddo: "), 'w')
   gravandodump.truncate

   print ('Aguarde o processamento de extra\xe7\xe3o %s.') % (languageselect)

   # Position first pointer
   arquivo.seek(offset)

   def capturePONT():
      def captureTXT():
         arquivo.seek(capHex)
         while True:
            hexCapturado = arquivo.read(1)
            if hexCapturado.encode("hex") == '00':
               gravandodump.write('\n')
               break
            if hexCapturado == '\n':
               gravandodump.write('#')
            else:
               try:
                  gravandodump.write(table[hexCapturado.encode("hex")])
               except:
                  gravandodump.write('$'+hexCapturado.encode("hex"))
         gravandodump.close

      global capHex
      arquivo.seek(offset)
      OffhexCapturado = arquivo.read(4).encode("hex")
      capHex = int(OffhexCapturado[6:8]+OffhexCapturado[4:6]+OffhexCapturado[2:4]+OffhexCapturado[0:2], 16) - 134217728

      captureTXT()
   while True:
      if offset >= int('7909724'):
          pressexit()
          break
      else:
          capturePONT()
      offset += 20

   arquivo.close

def insert():

   table = {}

   try:
      for i in mapa.readlines():
         table[i.split(';')[1]] = i.split(';')[0]
         mapa.close
   except:
      print ('Erro ao criar a tabela para inserir.')
      sys.exit(0)

   try:
   #    arquivodump = open(raw_input("Digite o nome do arquivo extraido: "), "rbU")
       arquivodump = open(raw_input("Digite o nome do arquivo extra\xeddo: "), "rbU")
   except:
       print ('Erro: Arquivo n\xe3o encontrado!')
       pressexit()
       sys.exit(0)
   
   num_lines = sum(1 for line in arquivodump)
   if num_lines != int(int('3328')):
      print ('O arquivo extra\xeddo deve conter 3328 linhas traduzidas. O lido foi %s.') % (num_lines)
      sys.exit(0)

   gravandoinsert = open('NEWSR.txt', 'wb')
   gravandoinsert.truncate

   soma = int('142145784')

   ponteiros = []
   ponteiros.insert(0,str(soma))

   print ('Aguarde o primeiro processamento de inser\xe7\xe3o no Idioma Ingl\xeas.')
   
   while True:
      def Gravar(valor):
         gravandoinsert.write(binascii.a2b_hex(''.join(valor)))

      hexCapturado = arquivodump.read(1)
      if hexCapturado == '':
         break
      elif hexCapturado == '\n':
         hexCapturado = arquivodump.read(1)
         if hexCapturado == '':
            break
         else:
            arquivodump.seek(arquivodump.tell()-1)
            Gravar('00')
            soma += 1
            ponteiros.insert(0,str(soma))
      elif hexCapturado == '$':
         hexCapturado = arquivodump.read(2)
         Gravar(hexCapturado)
         soma += 1
      else:
         try:
            Gravar(table[hexCapturado])
            soma += 1
         except:
            print ('Erro: Caracter %s n\xe3ao encontrado na tabela (table.txt).') % (hexCapturado)
   del table
   gravandoinsert.close
   arquivodump.close
   contentrom = arquivo.read(int('7843164'))
   
   gravandonewrom = open(raw_input("Digite o nome da nova Rom traduzida: "), 'wb')
   gravandonewrom.truncate
   print ('Aguarde o segundo processamento de inser\xe7\xe3o no Idioma Ingl\xeas.')
   gravandonewrom.write(contentrom)
   
   for valores in reversed(ponteiros):
      valores = hex(int(valores))[2:].zfill(8)
      invertvalores = valores[6:8]+valores[4:6]+valores[2:4]+valores[0:2]
      gravandonewrom.write(binascii.a2b_hex(''.join(invertvalores)))
      contentrom = arquivo.read(4)
      contentrom = arquivo.read(16)
      gravandonewrom.write(contentrom)
   del ponteiros
   contentrom = arquivo.read(18332)
   gravandonewrom.write(contentrom)
   gravandoinsert = open('NEWSR.txt', 'rb')
   contentrom = gravandoinsert.read()
   gravandonewrom.write(contentrom)
   gravandoinsert.close
   del contentrom
   arquivo.close

   while True:
      finalarq = gravandonewrom.tell()
      if finalarq == int('8388608'):
         break
      else:
         gravandonewrom.write('\xff')
   gravandonewrom.close
   pressexit()

#7928044

def language():
   global languageselect
   global offset
   try:
       languageselect = raw_input('Escolha o idioma conforme as op\xe7\xf5es para '+optionlg+'.\nEN: English\nFR: Fran\xe7ais\nDE: Deutsch\nES: Espa\xf1ol\nIT: Italiano\n').upper()
       if languageselect == 'EN':
           offset = int('7843164')
       elif languageselect == 'FR':
           offset = int('7843168')
       elif languageselect == 'DE':
           offset = int('7843172')
       elif languageselect == 'ES':
           offset = int('7843176')
       elif languageselect == 'IT':
           offset = int('7843180')
       else:
           sys.exit(0)
   except:
       print ('Idioma n\xe3o encontrado.')
       pressexit()
       sys.exit(0)

selectDI = raw_input("Aperte D para extrair ou I para inserir:\n").upper()

try:
   mapa = open('table.txt','rbU')
except:
   print ('Erro ao abrir o arquivo table.txt.')
   sys.exit(0)

def openfile(option):
   global arquivo
   try:
      arquivo = open(raw_input("Insira o nome da rom original: "), option)
      #arquivo = open('bh.gba', option)
   except:
      print ('Erro: Arquivo n\xe3o encontrado!')
      pressexit()
      sys.exit(0)

if selectDI == 'D':
   openfile ("rbU")
   optionlg = 'Extrair'
   language()
   dump()
elif selectDI == 'I':
   openfile ("rb")
   optionlg = 'Inserir'
   #language()
   insert()
else:
   print ('Op\xe7\xe3o diferente do esperado.')
   pressexit()
   sys.exit(0)

