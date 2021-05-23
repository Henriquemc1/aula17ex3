valor = float(input('Preço do produto:'))
quantidade = int(input(' Digite a quantidade do produto'))
pagamento = int(input('Digite a forma de pagamento :\n' '1- À vista em dinheiro ou cheque, recebe 10% de desconto,\n' '2- À vista no cartão de crédito ou débito, recebe 5% de desconto,\n' '3- Em duas vezes, preço normal de etiqueta sem juros,\n' '4- Em três vezes, preço normal de etiqueta mais juros de 10%,\n'))
if pagamento == 1:
  total = (valor * quantidade * 0.90)
  print('Valor total da compra é de R$',total)
elif pagamento == 2:
  total = (valor * quantidade * 0.95)
  print('Valor total da compra é de R$',total)
elif pagamento == 3:
  total = (valor * quantidade)
  parcela = total /2 
  print('Valor total da compra é de R$',total,'Parcelado em duas vezes de',parcela) 
elif pagamento == 4:
  juros = (valor * quantidade * 0.1)
  total = (valor * quantidade + juros)
  parcela = total /3
  print('Valor total da compra é de R$',total,'Parcelado em três vezes de',parcela)
  
