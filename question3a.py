import scipy.stats as stats

def calculator(k_percentage, bb_percentage):
    intercept = 0.77
    slope_k = -0.74
    slope_bb = 1.45
    residual_std_error = 0.220
    ops = intercept + slope_k * k_percentage + slope_bb * bb_percentage
    return ops 

batter_a = calculator(0.2,0.2)
batter_b = calculator(0.05,0.1)

print(batter_a)
print(batter_b)