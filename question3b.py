import math

intercept = -0.63
slope_k = -6.52
slope_bb = 13.7

k_c = 0.20
bb_c = 0.14

k_d = 0.25
bb_d = 0.20

def logistic_function(intercept, slope_k, slope_bb, k, bb):
    return 1 / (1 + math.exp(-(intercept + slope_k * k + slope_bb * bb)))

def marginal_effect(slope, probability):
    return slope * probability * (1 - probability)

prob_c = logistic_function(intercept, slope_k, slope_bb, k_c, bb_c)
prob_d = logistic_function(intercept, slope_k, slope_bb, k_d, bb_d)

marginal_effect_c = marginal_effect(slope_bb, prob_c)
marginal_effect_d = marginal_effect(slope_bb, prob_d)

print(abs(marginal_effect_c))
print(abs(marginal_effect_d))

#since batter C has a higher marginal effect, so the marginal effect of varying BB% is larger for batter C.