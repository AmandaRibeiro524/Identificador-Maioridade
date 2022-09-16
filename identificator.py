print('Identificador')

nome= input('Qual o seu nome?')
idade= int(input('Quantos anos você tem? '))


if idade >=18: 
  print('%s, você é maior de idade!' % (nome))

else: 
    print('%s, você é menor de idade!' % (nome))