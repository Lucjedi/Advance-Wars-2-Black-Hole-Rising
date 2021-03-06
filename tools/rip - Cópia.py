
#!/usr/bin/python
import sys
import binascii
import os
print ('---------------------------------------')

def pressexit():
   print ('Aperte ENTER para sair...')
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

   gravandodump = open(raw_input('Digite um nome para o arquivo extraido: '), 'w')
   gravandodump.truncate
   

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
      arquivodump = open('dump.txt', "rbU")
   except:
      print ('Erro: Arquivo nao encontrado!')
      pressexit()
      sys.exit(0)

   gravandoinsert = open('NEWSR.txt', 'wb')
   gravandoinsert.truncate

   soma = int('142145784')

   ponteiros = []
   ponteiros.insert(0,str(soma))
   
   while True:
      def Gravar(valor):
         try:
            gravandoinsert.write(binascii.a2b_hex(''.join(valor)))
         except:
            print (valor)

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
            print ('Erro: Caracter %s nao encontrado na tabela (table.txt).') % (hexCapturado)
   del table
   gravandoinsert.close
   arquivodump.close
   contentrom = arquivo.read(offset)

   try:
      gravandonewrom = open('tradu.gba', 'wb')
      gravandonewrom.truncate
   except:
      print ('Erro: Nao foi possivel criar o arquivo traduzido.')
      
   
   
   gravandonewrom.write(contentrom)
   
   for valores in reversed(ponteiros):
      valores = hex(int(valores))[2:].zfill(8)
      invertvalores = valores[6:8]+valores[4:6]+valores[2:4]+valores[0:2]
      gravandonewrom.write(binascii.a2b_hex(''.join(invertvalores)))
      contentrom = arquivo.read(4)
      contentrom = arquivo.read(16)
      gravandonewrom.write(contentrom)
   del ponteiros
   contentrom = arquivo.read(offcontentlg) # 18332
   gravandonewrom.write(contentrom)
   gravandoinsert = open('NEWSR.txt', 'rb')
   contentrom = gravandoinsert.read()
   gravandonewrom.write(contentrom)
   gravandonewrom.write('\x00')
   gravandoinsert.close
   del contentrom
   arquivo.seek(offset)

   while True:
      finalarq = gravandonewrom.tell()
      if finalarq == int('8243184'):
         break
      else:
         gravandonewrom.write('\xff')
   arquivo.seek(int('8243184'))
   contentrom = arquivo.read()
   gravandonewrom.write(contentrom)
   gravandonewrom.close
   arquivo.close
   pressexit()

#7928044

def language():
   global languageselect
   global offcontentlg
   global offset
   try:
      languageselect = 'EN'
      if languageselect == 'EN':
         offcontentlg = int('18332')
         offset = int('7843164')
      elif languageselect == 'FR':
         offcontentlg = int('18328')
         offset = int('7843168')
      elif languageselect == 'DE':
         offcontentlg = int('18324')
         offset = int('7843172')
      elif languageselect == 'ES':
         offcontentlg = int('18320')
         offset = int('7843176')
      elif languageselect == 'IT':
         offcontentlg = int('18316')
         offset = int('7843180')
      else:
         sys.exit(0)
   except:
      print ('Idioma nao encontrado.')
      pressexit()
      sys.exit(0)
      
selectDI = 'I'

try:
   mapa = open('table.txt','rbU')
except:
   print ('Erro ao abrir o arquivo table.txt.')
   sys.exit(0)

def openfile(option):
   global arquivo
   try:
      arquivo = open('bh.gba', option)
   except:
      print ('Erro: Arquivo nao encontrado!')
      pressexit()
      sys.exit(0)

if selectDI == 'D':
   openfile ("rbU")
   optionlg = 'Escolha o Idioma para EXTRAIR.'
   language()
   dump()
elif selectDI == 'I':
   openfile ("rb")
   optionlg = 'Escolha o Idioma no qual deseja SUBSTITUIR.'
   language()
   insert()
else:
   print ('Opcoes diferente do esperado.')
   pressexit()
   sys.exit(0)
