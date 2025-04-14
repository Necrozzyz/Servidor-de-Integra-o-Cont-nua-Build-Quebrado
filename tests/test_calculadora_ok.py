from src.calculadora_ok import soma, subtrai, multiplica, divide

def test_soma():
    assert soma(2, 3) == 5

def test_subtrai():
    assert subtrai(5, 2) == 3

def test_multiplica():
    assert multiplica(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divisao_por_zero():
    try:
        divide(10, 0)
        assert False  # Não deveria chegar aqui
    except ValueError:
        assert True