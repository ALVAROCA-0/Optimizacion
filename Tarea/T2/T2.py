from scipy.optimize import linprog, minimize

# 1. Mezcla de fertilizantes

# 1.1. Variables de descisión
# A, B, C en Kg

# 1.2. Función objetivo
# Max G
# Donde:
#   G = 180 x1 + 220 x2
c = [-180, -220]    # En negativos para maximizar

# 1.3. restricciones
# Forma planteada por el problema
# 120 >= 3 x1 + 4 x2
# 80  >= 2 x1 + 1 x2
# 150 >= 5 x1 + 3 x2
# Forma normal para scipy
# 3 x1 + 4 x2 <= 120
# 2 x1 + 1 x2 <=  80
# 5 x1 + 3 x2 <= 150

A_ub = [
    [3, 4],
    [2, 1],
    [5, 3]
]

b_ub = [
    120,
    80,
    150
]

# Límites de las variables (x1, x2 >= 0)
bounds = [(0, None), (0, None)]


resultado = linprog(c, A_ub, b_ub, bounds=bounds, method="highs")


# Impresión de los resultados a consola
print("="*40)
print(f"{"1. Máxima ganancia de fertilizantes":^40}")
print("="*40)

print(f"Estado: {resultado.message}\n")
for i, fert in enumerate(resultado.x, 1):
    print(f"Fertilizante {i}: {fert:.4f} Ton")

print()
#Como se nego antes para maximizar se debe volver a negar para obtener el resultado
print(f"Ganancia Máxima: {-resultado.fun:.4f}\n")

x1, x2 = resultado.x
print("Verificación:")
res = ["A", "B", "C"]
for comp, (a1, a2), b in zip(res, A_ub, b_ub):
    print(f"Compuesto {comp}: {a1 * x1 + a2*x2: .2f} Kg (Máximo {b} Kg)")


# 2. Producción semanal de una fábrica
print("="*40)
print(f"{"2. Producción semanal de una fábrica":^40}")
print("="*40)

S = 200
M = 80
for i in range(16):
    print(f"Semana {i:>3}")
    print(f"Sillas: {S}")
    print(f"Mesas : {M}")
    S, M = 0.6*S + 0.2*M + 40, 0.1*S + 0.5*M + 20

# 4. Modelo logístico de pesca
print("="*40)
print(f"{"4. Modelo logísitico de pesca":^40}")
print("="*40)

H = 80
K = 1000
r = 0.4
P = 400
E = 0
for i in range(3):
    print(f"Año {i:>2}")
    print(f"número de pesces: {P}")
    n_P = P + r * P * (1 - P / K) - H
    E = abs(n_P - P)
    P = n_P

while E > 1E-5 and i < 100:
    n_P = P + r * P * (1 - P / K) - H
    E = abs(n_P - P)
    P = n_P
    i += 1

print(f"En el año {i:<3} la población de pesces es: {P:<.4f}")