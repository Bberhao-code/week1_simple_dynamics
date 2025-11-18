import numpy as np

# 参数
m = 1000.0      # 质量 kg
F = 2000.0      # 恒定推力 N

def vehicle_ode(t, state):
    """
    state[0] = v (速度)
    state[1] = x (位置)
    """
    v, x = state
    dvdt = F / m
    dxdt = v
    return [dvdt, dxdt]
