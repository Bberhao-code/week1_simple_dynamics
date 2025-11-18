from scipy.integrate import solve_ivp
import numpy as np
import os
from model import vehicle_ode

# 时间
t_span = (0, 20)
t_eval = np.linspace(0, 20, 500)

# 初始条件
state0 = [0.0, 0.0]   # v=0, x=0

# 求解
sol = solve_ivp(vehicle_ode, t_span, state0, t_eval=t_eval)

t = sol.t
v = sol.y[0]
x = sol.y[1]

# 保存数据
np.savez("results/simulation_data.npz", t=t, v=v, x=x)

print("模拟完成！数据已保存到 results/simulation_data.npz")
