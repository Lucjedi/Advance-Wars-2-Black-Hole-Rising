#!/usr/bin/python
import sys
import binascii
print ('---------------------------------------')

def dump():
   ## Verifica arquivo de entrada
   try:
   #    arquivo = open(raw_input("Filename Army 2's rom: "), "rbU")
       arquivo = open('bh.gba', "rbU")
   except:
       print ('Error: File not found!')
       raw_input('Press ENTER to exit...')
       sys.exit(0)

   try:
       languageselect = raw_input("Select Language to Dump.\nEN: English\nFR: Fran\xe7ais\nDE: Deutsch\nES: Espa\xf1ol\nIT: Italiano:\n")
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
       print ('Dump %s language.') % (languageselect)
   except:
       raw_input('Language not found\nPress ENTER to exit...')
       sys.exit(0)

   try:
       mapa = open('table.txt','rbU')
   except:
       print ('Failed to open file table.txt.')
       sys.exit(0)

   table = {}
   try:
       for i in mapa.readlines():
           table[i.split(';')[0]] = i.split(';')[1]
   except:
       print ('Failed to create table.')
       sys.exit(0)

   gravando = open('dump.txt', 'w')
   gravando.truncate

   gravandoPT = open('dumpPT.txt', 'w')
   gravandoPT.truncate

   # Position first pointer
   arquivo.seek(offset)

   def capturePONT():
      def captureTXT():
         arquivo.seek(capHex)
         while True:
            hexCapturado = arquivo.read(1)
            if hexCapturado.encode("hex") == '00':
               gravando.write('\n')
               break
            elif hexCapturado.encode("hex") == '0a':
               gravando.write('#')
            else:
               try:
                  gravando.write(table[hexCapturado.encode("hex")])
               except:
                  gravando.write('$'+hexCapturado.encode("hex"))

      global capHex
      arquivo.seek(offset)
      OffhexCapturado = arquivo.read(4).encode("hex")
      capHex = int(OffhexCapturado[6:8]+OffhexCapturado[4:6]+OffhexCapturado[2:4]+OffhexCapturado[0:2], 16) - 134217728

      captureTXT()
   while True:
      if offset >= int('7909724'):
          raw_input('Press ENTER to exit...')
          break
      else:
          gravandoPT.write(str(offset)+'\n')
          capturePONT()
      offset += 20
   
   arquivo.close
   gravando.close
   gravandoPT.close

def insert():
   try:
      mapa = open('table.txt','rbU')
   except:
      print ('Failed to open file table.txt.')
      sys.exit(0)

   table = {}

   try:
      for i in mapa.readlines():
         table[i.split(';')[1]] = i.split(';')[0]
   except:
      print ('Failed to create table.')
      sys.exit(0)

   try:
   #    arquivo = open(raw_input("Filename PT-BR: "), "rbU")
       arquivo = open('dumpPTBR.txt', "rbU")
   except:
       print ('Error: File PT-BR not found!')
       raw_input('Press ENTER to exit...')
       sys.exit(0)

   gravando = open('NEWSR.txt', 'wb')
   gravando.truncate

   while True:
      def Gravar(valor):
         gravando.write(binascii.a2b_hex(''.join(valor)))
         
      hexCapturado = arquivo.read(1)
      if hexCapturado == '':
         break
      elif hexCapturado == '\n':
         Gravar('00')
      elif hexCapturado == '$':
         hexCapturado = arquivo.read(2)
         Gravar(hexCapturado)
      else:
         try:
            Gravar(table[hexCapturado])
         except:
            print ('ERRO NAO IDENTIFICADO. %s') % (hexCapturado)
   raw_input('Press ENTER to exit...')
   arquivo.close
   gravando.close

#7928044

try:
   selectDI = raw_input("Select 1 to Dump or 2 to Insert:\n")
   if selectDI == '1':
       dump()
   elif selectDI == '2':
       insert()
   else:
       sys.exit(0)
except:
    raw_input('Dump/insert not found\nPress ENTER to exit...')
    sys.exit(0)
