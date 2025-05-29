def classificar_impar_par():

    while True:

        try:
            numero =(input('Digite um numero inteiro,(ou digite fim:) '))
            if numero.lower() == 'fim':
                break

            else:
                numero = int(numero)
            if numero % 2 == 0:
                return 'e par.'
            else:
                return 'e impar.'
                
        except ValueError:
            print('Entrada invalida. Por favor, digite um numero inteiro ou fim.')
            
print(classificar_impar_par())