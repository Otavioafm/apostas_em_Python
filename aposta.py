from random import randint
Fnum=0
Vnum=0
jogador=str
saldo=0
inicar=str
comecar=str


print("{}\nBem vindo a casa de aposta do Talison\nAcerte o número e ganhe Erre e perca R$100\nApostas vão de 1 a 5!!\n{}".format("="*42,"="*42))

while True:
  
 saldo=int(input("\nValor mínimo R$20\nDigite quanto você quer apostar: "))
 while saldo>=20:
  if saldo==0:
   break 
  print(f"\nSeu saldo para apostas são de R${saldo}")
  comecar=str(input("Digite |iniciar|: ")).strip().upper()
  print("{}".format("_"*41))
 
  while comecar=="INICIAR":
   Fnum=randint(1,5)
   Vnum=randint(1,5)
   print(f"\nOpinião da casa: {randint(1,99)}% vai cair {Vnum}")
   jogador=int(input("Faça o seu palpite: "))
  
   if jogador==Vnum:
    saldo+=20
    print(f"\nVOCÊ ACERTOU!🤑\nSaldo atual: R${saldo}")
  
   else:
    saldo-=10
    print(f"\nVOCÊ ERROU!😕\nSaldo atual: R${saldo}")
     
   if saldo==0:
    print(f"\nVOCÊ PERDEU TUDO‼️\nBoa sorte na próxima ... saldo atual R${saldo}😰")
    break
   
           
   while jogador==Vnum:
     print(f"\nOpinião da casa: {randint(1,99)}% vai cair {Fnum}")
     jogador=int(input("Faça o seu palpite: "))
     
     if jogador==Vnum:
      saldo+=10
      print(f"\nVOCÊ ACERTOU!😎\nSaldo atual: R${saldo}")
      
     else:
      saldo-=20
      print(f"\nVOCÊ ERROU!😣\nSaldo atual: R${saldo}")
     
     if saldo==0:
      print(f"\nVOCÊ PERDEU TUDO‼️\nBoa sorte na próxima ... saldo atual R${saldo}😱")
      break
 break