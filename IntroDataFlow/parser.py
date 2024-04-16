"""
This file implements a parser: a function that reads a text file, and returns
a control-flow graph of instructions plus an environment mapping variables to
integer values. The text file has the following format:

    [First line] A dictionary describing the environment
    [n-th line] The n-th instruction in our program.

As an example, the program below sums up the numbers a, b and c:

    {"a": 1, "b": 3, "c": 5}
    x = add a b
    l2 = x = add x c
"""

# from lang import Env, Inst
from lang import * 

def line2env(line: str) -> Env:
    """
    Maps a string (the line) to a dictionary in python. This function will be
    useful to read the first line of the text file. This line contains the
    initial environment of the program that will be created. If you don't like
    the function, feel free to drop it off.

    Example
        >>> line2env('{"zero": 0, "one": 1, "three": 3, "iter": 9}').get('one')
        1
    """
    import json

    env_dict = json.loads(line)
    env_lang = Env()
    for k, v in env_dict.items():
        env_lang.set(k, v)
    return env_lang


def file2cfg_and_env(lines):
    """
    Builds a control-flow graph representation for the strings stored in
    `lines`. The first string represents the environment. The other strings
    represent instructions.

    Example:
        >>> l0 = '{"a": 0, "b": 3}'
        >>> l1 = 'bt a 1'
        >>> l2 = 'x = add a b'
        >>> env, prog = file2cfg_and_env([l0, l1, l2])
        >>> interp(prog[0], env).get("x")
        3

        >>> l0 = '{"a": 1, "b": 3, "x": 42, "z": 0}'
        >>> l1 = 'bt a 2'
        >>> l2 = 'x = add a b'
        >>> l3 = 'x = add x z'
        >>> env, prog = file2cfg_and_env([l0, l1, l2, l3])
        >>> interp(prog[0], env).get("x")
        42

        >>> l0 = '{"a": 1, "b": 3, "c": 5}'
        >>> l1 = 'x = add a b'
        >>> l2 = 'x = add x c'
        >>> env, prog = file2cfg_and_env([l0, l1, l2])
        >>> interp(prog[0], env).get("x")
        9
    """
    # TODO: Imlement this method.
    env = line2env(lines[0])
    insts = []

    insts_prev = []
    
    # a ideia é criar uma lista prévia de instruções e
    # e depois passar pela lista fixando os Branches
    
    bt_count = 0
    bt_dict = {}
    for line in lines[1:]: 
        tokens = line.split()
        
        if tokens[0] != 'bt':
            instruction = tokensToInsts(tokens)
        else:
            instruction = Bt(tokens[1], None, None)
            bt_dict[bt_count] = tokens
            bt_count += 1
        
        insts_prev.append(instruction)
        
    
    cnt = 0
    for instruction, line in zip(insts_prev, lines[1:]): 
        tokens = line.split()
        
        if tokens[0] == 'bt':
            cond = tokens[1]
            true_dst = int(tokens[2])
            false_dst = cnt+1
            instruction.add_true_next(insts_prev[true_dst])
        
        insts.append(instruction)
        
        if cnt > 0: 
            insts[cnt-1].add_next(instruction)

        
        cnt +=1 



    return (env, insts)


def tokensToInsts(tokens): 
    if tokens[2] == 'add': 
        return Add(tokens[0], tokens[3], tokens[4])

    if tokens[2] == 'mul':
        return Mul(tokens[0], tokens[3], tokens[4])
            
    if tokens[2] == 'lth':
        return Lth(tokens[0], tokens[3], tokens[4])
            
    if tokens[2] == 'geq': 
        return Geq(tokens[0], tokens[3], tokens[4])