
altura = float(input('Qual é a sua altura em cm: '))
peso = float(input('Qual é o seu peso em kg: '))

IMC = peso / (altura/100)**2

print(IMC)

if IMC < 18.5:
  print(f'Seu IMC é de {IMC}, e é classificado como Magreza')

elif IMC >= 18.5 and IMC < 24.9:
  print(f'Seu IMC é de {IMC}, e é classificado como Normal')

elif IMC >= 25 and IMC < 29.9:
  print(f'Seu IMC é de {IMC}, e é classificado como Sobrepeso')

elif IMC >= 30 and IMC < 39.9:
  print(f'Seu IMC é de {IMC}, e é classificado como Obesidade')

else:
    print(f'Seu IMC é de {IMC}, e é classificado como Obesidade Grave')


# MENOR QUE 18,5: MAGREZA
# ENTRE 18,5 E 24,9: NORMAL
# ENTRE 25,0 E 29,9: SOBREPESO
# ENTRE 30,0 E 39,9: OBESIDADE
# MAIOR QUE 40,0: OBESIDADE GRAVE