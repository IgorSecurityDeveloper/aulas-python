nome = str(input('Digite seu nome completo: ')).strip()

print('O seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()

print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))