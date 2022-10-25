from random import choice


class App:
    def __init__(self):
        self.cpfs = []

    def start(self, tem_mascara):
        cpfs_mascara = [self.cpf_com_mascara(i) for i in self.cpfs]
        print(cpfs_mascara) if tem_mascara else print(self.cpfs)

    def pega_produtos(self, cpf_em_lista, range):
        fatores = [i for i in range][::-1]
        multiplicadores = zip(cpf_em_lista, fatores)
        produtos = [int(i[0]) * i[1] for i in multiplicadores]
        return produtos

    def dv1(self, cpf):
        produtos = self.pega_produtos(cpf, range(2, 11))
        dv1 = (sum(produtos) * 10) % 11
        return 0 if dv1 == 10 else dv1

    def dv2(self, cpf):
        produtos = self.pega_produtos(cpf, range(3, 12))
        dv1_contagem = self.dv1(cpf)
        dv2 = ((sum(produtos) + (dv1_contagem * 2)) * 10) % 11
        return 0 if dv2 == 10 else dv2

    def valida_cpf(self, cpf):
        dv1, dv2 = self.dv1(cpf), self.dv2(cpf)
        numero_controle = (dv1 * 10) + dv2
        return True if numero_controle == int(cpf[-2:]) else False

    def gera_cpf(self):
        numeros = [str(i) for i in range(0, 10)]
        cpf, c = [], 0
        while c < 11:
            cpf.append(choice(numeros))
            c += 1
        return "".join(cpf)

    def gera_cpf_valido(self):
        while True:
            novo_cpf = self.gera_cpf()
            cpf_valido = self.valida_cpf(novo_cpf)
            if cpf_valido:
                break
        return novo_cpf

    def gera_lista_cpfs(self, qtd):
        c = 0
        while c < qtd:
            self.cpfs.append(self.gera_cpf_valido())
            c += 1
        return self.cpfs

    def cpf_com_mascara(self, cpf):
        cpf_mascara = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:11]
        return cpf_mascara


if __name__ == "__main__":
    app = App()
    x_cpfs = int(input("Quantos CPF's vocẽ deseja gerar? "))
    app.gera_lista_cpfs(x_cpfs)
    while True:
        tem_mascara = input("CPF's com máscara? (S/N) ").lower()
        if tem_mascara == "s":
            e_mascarado = True
            break
        elif tem_mascara == "n":
            e_mascarado = False
            break
        else:
            print("comando não reconhecido")
    app.start(e_mascarado)
