from InquirerPy import prompt

print('Bem vindo(a) a Calculadora Regra de 3 em Python\n')
# Funções
def n_s_cal():
    x = float(input('Digite o \"x\": '))
    y = float(input('Digite o \"y\": '))
    z = float(input('Digite o \"z\": '))
    r = (z*y)/x
    rr = round(r, 3)
    print(f'\nA resposta é {rr}\n')
def i_s_cal():
    x = float(input('Digite o \"x\": '))
    y = float(input('Digite o \"y\": '))
    z = float(input('Digite o \"z\": '))
    r = (x * y) / z
    rr = round(r, 3)
    print(f'\nA resposta é {rr}\n')
def n_c_cal():
    x = float(input('Digite o \"x\": '))
    y = float(input('Digite o \"y\": '))
    z = float(input('Digite o \"z\": '))
    a = float(input('Digite o \"a\": '))
    b = float(input('Digite o \"b\": '))
    r = (z * a * b) / (x * y)
    rr = round(r, 3)
    print(f'\nA resposta é {rr}\n')
def i_c_cal():
    x = float(input('Digite o \"x\": '))
    y = float(input('Digite o \"y\": '))
    z = float(input('Digite o \"z\": '))
    a = float(input('Digite o \"a\": '))
    b = float(input('Digite o \"b\": '))
    r = (x * y * z) / (a * b)
    rr = round(r, 3)
    print(f'\nA resposta é {rr}\n')

# Perguntas
p1 = [
    {
        "type": "list",
        "message": "O você quer acessar?",
        "choices": ["Modo", "Representação", "Sair"]
    },
]
p2 = [
    {
        "type": "list",
        "message": "Qual Modo?",
        "choices" : ["Simples", "Composto"]
    },
]
p3 = [
    {
        "type": "list",
        "message": "Qual Modo?",
        "choices" : ["Normal", "Inverso"]
    },
]

f = True

while f == True:
    r1 = prompt(p1)
    if r1 == {0: 'Modo'}:
        r2 = prompt(p2)
        if r2 == {0: 'Simples'}:
            r3 = prompt(p3)
            if r3 == {0: 'Normal'}:
                n_s_cal()
                f = True
            else:
                i_s_cal()
                f = True
        else:
            r3 = prompt(p3)
            if r3 == {0: 'Normal'}:
                n_c_cal()
                f = True
            else:
                i_c_cal()
                f = True
    elif r1 == {0: 'Representação'}:
        r2 = prompt(p2)
        if r2 == {0: 'Simples'}:
            print('\n x == y\n z == ?\n')
            f = True
        else:
            print('\n x == y == z\n a == b == ?\n')
            f = True
    else:
        print('\nOkay ...\n')
        f = False