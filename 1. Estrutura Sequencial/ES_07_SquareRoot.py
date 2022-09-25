# Faça um programa que calcule a área de um quadrado, em seguida mostre
# o dobro dessa área para o usuário


# Objetivo do algoritmo é obter a raíz quadrada sem o uso da função sqrt da lib 'math'

def isPerfectSquare(_value_):
    if _value_ is not None and _value_ > 1:
        if float(_value_) % int(_value_) == 0:
            return True
    else:
        return False


def Mult(_value_):
    return _value_ * _value_


def isPair(_value_):
    if _value_ % 2 == 0:
        return True
    else:
        return False


def getSquareRoot(_value_):
    _sqrt_ = float(_value_)
    if float(_value_) is not None:
        while Mult(_sqrt_) >= _value_:
            print(_value_, _sqrt_, Mult(_sqrt_))
            if isPair(_sqrt_) and Mult(_value_) > _value_:
                _sqrt_ = _sqrt_ / 2
            elif not isPair(_sqrt_) and Mult(_value_) > _value_:
                _sqrt_ = _sqrt_ / 3

            if Mult(_sqrt_) <= _value_:
                return float(_sqrt_)

    return float(_sqrt_)


if __name__ == "__main__":
    task = float(input("Informe um valor para obter a raíz quadrada: "))
    r = getSquareRoot(task)
    if isPerfectSquare(r):
        print(f"--> Raíz de {task} = {r}. [Quadrado perfeito!]")
    else:
        print(f"--> Raíz de {task} = {r}.")














