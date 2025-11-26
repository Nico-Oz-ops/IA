def teorema_bayes(p_a_dato_b, p_b, p_a):
    """
    Calcola P(B|A) = P(A|B) · P(B) / P(A)
    
    Args:
        p_a_dato_b: P(A|B) - verosimiglianza
        p_b: P(B) - probabilità a priori
        p_a: P(A) - evidenza
    
    Returns:
        P(B|A) - probabilità a posteriori
    """
    return (p_a_dato_b * p_b) / p_a

def teorema_bayes_completo(p_a_dato_b, p_b, p_a_dato_non_b):
    """
    Calcola P(B|A) usando la legge della probabilità totale per P(A)
    """
    p_non_b = 1 - p_b
    p_a = p_a_dato_b * p_b + p_a_dato_non_b * p_non_b
    return teorema_bayes(p_a_dato_b, p_b, p_a)

print("Inversione della Condizionalità con Bayes")
print(f"P(Difettoso | Fabbrica A) = {p_difettoso_dato_a:.2%}")
print(f"P(Fabbrica A | Difettoso) = {p_a_dato_difettoso:.2%}")
print(f"\nInterpretazione: Dato un prodotto difettoso,")
print(f"c'è una probabilità del {p_a_dato_difettoso:.2%} che provenga dalla Fabbrica A")

# === ESEMPIO: fabbriche A e B ===
# Supponiamo:
# Fabbrica A produce il 60% dei prodotti
# Fabbrica B il restante 40%
# Difettosità:
#   A: 2%
#   B: 5%

p_fabbrica_a = 0.60                 # P(A)
p_difettoso_dato_a = 0.02           # P(D | A)
p_difettoso_dato_b = 0.05           # P(D | B)

# Probabilità totale di difetto:
p_difettoso = (
    p_difettoso_dato_a * p_fabbrica_a
    + p_difettoso_dato_b * (1 - p_fabbrica_a)
)

# Calcolo Bayes: P(A | D)
p_a_dato_difettoso = teorema_bayes(
    p_a_dato_b=p_difettoso_dato_a,
    p_b=p_fabbrica_a,
    p_a=p_difettoso
)

# Output
print("Inversione della Condizionalità con Bayes")
print(f"P(Difettoso | Fabbrica A) = {p_difettoso_dato_a:.2%}")
print(f"P(Fabbrica A) = {p_fabbrica_a:.2%}")
print(f"P(Difettoso) = {p_difettoso:.2%}")
print(f"P(Fabbrica A | Difettoso) = {p_a_dato_difettoso:.2%}")

print("\nInterpretazione:")
print(f"Dato un prodotto difettoso, la probabilità che provenga dalla Fabbrica A è {p_a_dato_difettoso:.2%}.")