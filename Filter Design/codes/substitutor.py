import sympy as sp

sl, s, z = sp.symbols('sl s z')

Ha_LP = 0.3125 / (sl**4 + 1.1068*sl**3 + 1.6125*sl**2 + 0.914*sl +0.3366)
sub = (s**2 + 0.897**2)/(0.142 * s)
new = Ha_LP.subs(sl, sub)
newsimp = sp.simplify(new)
print('Bandpass TF (unnormalized):')
print(newsimp)

# transfer function
Ha_BP_s = 0.3125*s**4/(2459.49884228438*s**8 + 386.54861124693*s**7 + 7995.70886809889*s**6 + 939.498094358654*s**5 + 9682.63756497282*s**4 + 755.928622203822*s**3 + 5176.38708295219*s**2 + 201.353311074093*s + 1030.82790553413)

# Here z denotes z^{-1}, for simplicity
substitution1 = ((1 - z) / (1 + z))
substituted_expression = Ha_BP_s.subs(s, substitution1)
simplified_expression = sp.simplify(substituted_expression)
print("\nDigital TF:")
print(simplified_expression)