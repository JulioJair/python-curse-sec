def info(trinomial, seed):
    bits_required = trinomial[0]
    period_expected = 2 ** trinomial[0] - 1
    print(f'{bits_required} bit LFSR x^{trinomial[0]}+x^{trinomial[1]}+1')
    print(f'Periodo: {period_expected} (si el polinomio es primitivo)')
    print(f'Semilla: {seed}')


def generate_key(initial_seed):
    seed = initial_seed.copy()
    s = []
    while True:
        seed.insert(0, seed[0] ^ seed[3])
        s.append(seed.pop())
        if seed == initial_seed:
            break
    return s


def generate_key_faster(initial_seed, trinomial):
    period = 2 ** trinomial[0] - 1
    seed = initial_seed.copy()
    s = []
    for i in range(period):
        seed.insert(0, seed[0] ^ seed[3])
        s.append(seed.pop())
    # print(seed == initial_seed)
    return s

#
# trinomial = [4, 1, 0]
# seed = [1, 0, 0, 1]
# info(trinomial, seed)
#
# key = generate_key(seed)
# print(f'{len(key)} iteraciones')
# print(f'Llave generada: {key}')
#
# trinomial = [17, 3, 0]
# seed = [1] * 17
# info(trinomial, seed)
#
# key = generate_key_faster(seed,trinomial)
# print(f'{len(key)} iteraciones')
# # print(f'Llave generada: {key}')
