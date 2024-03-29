from lang import *

def test_min(m, n):
    """
    Stores in the variable 'answer' the minimum of 'm' and 'n'

    Examples:
        >>> test_min(3, 4)
        3

        >>> test_min(4, 3)
        3
    """
    env = Env({"m": m, "n": n, "x": m, "zero": 0})
    m_min = Add("answer", "m", "zero")
    n_min = Add("answer", "n", "zero")
    p = Lth("p", "n", "m")
    b = Bt("p", n_min, m_min)
    p.add_next(b)
    interp(p, env)
    return env.get("answer")

def test_min3(x, y, z):
    """
    Stores in the variable 'answer' the minimum of 'x', 'y' and 'z'

    Examples:
        >>> test_min3(3, 4, 5)
        3

        >>> test_min3(5, 4, 3)
        3
    """
    # TODO: Implement this method
    env = Env({"x": x, "y": y, "z": z, "zero": 0})
    
    x_min = Add("answer", "x", "zero")
    y_min = Add("answer", "y", "zero")
    z_min = Add("answer", "z", "zero")
    aux_min = Add("answer", "aux", "zero")
    
    x_aux = Add("aux", "x", "zero")
    y_aux = Add("aux", "y", "zero")
    
    p = Lth("p", "x", "y")
    b = Bt("p", x_aux, y_aux)

    p2 = Lth("p2", "aux", "z")
    b2 = Bt("p2", aux_min, z_min)
    
    p.add_next(b)
    
    
    p2.add_next(b2)
    
    interp(p, env)
    interp(p2, env)
    
    return env.get("answer")

def test_div(m, n):
    """
    Stores in the variable 'answer' the integer division of 'm' and 'n'.

    Examples:
        >>> test_div(30, 4)
        7

        >>> test_div(4, 3)
        1

        >>> test_div(1, 3)
        0
    """
    # TODO: Implement this method
    
    env = Env({"m": m, "n": n, "sum_acc": n, "answer": 0, "zero": 0, "one": 1})
    
    sum_n_to_acc = Add("sum_acc", "sum_acc", "n")
    sum_1_to_answer = Add("answer", "answer", "one")
    ret = Add("answer", "answer", "zero")

    condition = Lth("condition", "m", "sum_acc")

    branch = Bt("condition", ret, sum_n_to_acc)

    condition.add_next(branch)
    branch.add_next(sum_n_to_acc)
    sum_n_to_acc.add_next(sum_1_to_answer)
    sum_1_to_answer.add_next(condition)

    interp(condition, env)    
    
    return env.get("answer")

def test_fact(n):
    """
    Stores in the variable 'answer' the factorial of 'n'.

    Examples:
        >>> test_fact(3)
        6
    """
    # TODO: Implement this method
    
    env = Env({"n": n, "zero": 0, "one": 1, "answer": 1, "counter": 1 })
    
    n_mult = Mul("answer", "answer", "counter")
    counter_add = Add("counter", "counter", "one")
    
    ret = Add("answer", "answer", "zero")

    condition = Lth("condition", "n", "counter")
    
    branch = Bt("condition", ret, n_mult)

    condition.add_next(branch)

    n_mult.add_next(counter_add)
    counter_add.add_next(condition)

    interp(condition,env)
    
    return env.get("answer")