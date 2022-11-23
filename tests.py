from main import App

app = App()

cpf = "12285095902"
produtos_2a10 = [10, 18, 16, 56, 30, 0, 36, 15, 18]
produtos_3a11 = [11, 20, 18, 64, 35, 0, 45, 20, 27]


def test_produtos_dv1():
    assert app.produtos(cpf, range(2, 11)) == produtos_2a10


def test_produtos_dv2():
    assert app.produtos(cpf, range(3, 12)) == produtos_3a11


def test_dv1():
    assert app.dv1(cpf) == 0


def test_dv2():
    assert app.dv2(cpf) == 2


def test_valida_cpf():
    assert app.valida_cpf(cpf)


def test_gera_cpf():
    assert len(app.gera_cpf()) == 11


def test_gera_cpf_valido():
    cpf = app.gera_cpf_valido()
    assert app.valida_cpf(cpf)


def test_gera_lista_cpfs():
    for i in app.gera_lista_cpfs(10):
        assert app.valida_cpf(i)
