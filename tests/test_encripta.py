from applicationCesar.cesar import encripta


def test_encripta_victor_retorna():
    assert encripta("victor") == "ivpgbe"


def test_encripta_deve_retornar_minusculas():
    assert encripta("A").islower()


def test_encripta_deve_preservar_os_espacos():
    resultado = encripta("e a")
    assert resultado[1] == " "
