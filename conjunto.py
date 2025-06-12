# Conjuntos A y B
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Unión (A ∪ B)
union = A | B
print("Unión (A ∪ B):", union)

# Intersección (A ∩ B)
interseccion = A & B
print("Intersección (A ∩ B):", interseccion)

# Diferencia (A - B)
diferencia = A - B
print("Diferencia (A - B):", diferencia)

# Diferencia simétrica (A Δ B)
diferencia_simetrica = A ^ B
print("Diferencia simétrica (A Δ B):", diferencia_simetrica)

# Subconjunto (A ⊆ B)
es_subconjunto = A.issubset(B)
print("A es subconjunto de B:", es_subconjunto)

# Superconjunto (A ⊇ B)
es_superconjunto = A.issuperset(B)
print("A es superconjunto de B:", es_superconjunto)

# Conjunto vacío
vacio = set()
print("Conjunto vacío:", vacio)

# Pertenencia
print("¿3 pertenece a A?", 3 in A)
print("¿5 pertenece a A?", 5 in A)

# Conjuntos disjuntos (sin elementos en común)
C = {7, 8, 9}
disjuntos = A.isdisjoint(C)
print("A y C son disjuntos:", disjuntos)
