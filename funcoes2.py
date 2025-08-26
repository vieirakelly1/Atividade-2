def operacao(n1,n2,n3):
    if n2 == '+':
        print(n1+n3)
    elif n2 == '-':
        print(n1-n3)
    elif n2 == '*':
        print(n1*n3)
    elif n2 == '/':
        print(n1/n3)

def periodo(nome,horario):
    if horario >"18:00":
        print("Boa noite ",nome)

    elif horario >= "12:00":
        print("Boa tarde ",nome)
    else:
        print("Bom dia ",nome)




