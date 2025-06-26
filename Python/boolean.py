from typing import List, Tuple
from itertools import combinations, product

def to_binary(n: int, digits: int) -> str:
    return format(n, f'0{digits}b')

def is_power_of_two(x: int) -> bool:
    return x != 0 and ((x & (x - 1)) == 0)

def combine_terms(a: str, b: str) -> Tuple[bool, str]:
    """Combine two binary terms if they differ by only one bit"""
    diff = 0
    result = ''
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
            result += 'X'
        else:
            result += a[i]
    return (diff == 1, result)

def get_prime_implicants(minterms: List[int], num_vars: int) -> List[str]:
    """Generate prime implicants using Quine–McCluskey-like logic"""
    terms = [to_binary(m, num_vars) for m in minterms]
    unchecked = set(terms)
    checked = set()
    new_combinations = True
    prime_implicants = set()

    while new_combinations:
        new_terms = set()
        used_terms = set()
        for a, b in combinations(unchecked, 2):
            can_combine, combined = combine_terms(a, b)
            if can_combine:
                new_terms.add(combined)
                used_terms.add(a)
                used_terms.add(b)
        prime_implicants.update(unchecked - used_terms)
        checked.update(used_terms)
        unchecked = new_terms
        new_combinations = bool(new_terms)

    prime_implicants.update(unchecked)
    return list(prime_implicants)

def binary_to_boolean_expr(binary_term: str, var_names: List[str]) -> str:
    expr = ''
    for i, bit in enumerate(binary_term):
        if bit == '1':
            expr += var_names[i]
        elif bit == '0':
            expr += var_names[i] + "'"
    return expr or '1'

def simplify_kmap(num_vars: int, minterms: List[int]) -> str:
    if num_vars < 2 or num_vars > 4:
        return "Only 2 to 4 variables are supported."

    var_names = ['A', 'B', 'C', 'D'][:num_vars]
    prime_implicants = get_prime_implicants(minterms, num_vars)

    # Convert to Boolean expressions
    simplified_terms = [binary_to_boolean_expr(p, var_names) for p in prime_implicants]
    return ' + '.join(simplified_terms)

# Example usage:
results = {
    "2-variable": simplify_kmap(2, [0, 2]),
    "3-variable": simplify_kmap(3, [1, 3, 5, 7]),
    "4-variable": simplify_kmap(4, [4, 5, 6, 7, 12, 13, 14, 15])
}
print(results)
