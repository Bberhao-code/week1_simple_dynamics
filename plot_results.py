import numpy as np
import matplotlib.pyplot as plt

# 读取数据
data = np.load("results/simulation_data.npz")
t = data["t"]
v = data["v"]
x = data["x"]

# ----------- 速度曲线 ----------
plt.figure()
plt.plot(t, v)
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.savefig("results/velocity.png", dpi=200)

# ----------- 位置曲线 ----------
plt.figure()
plt.plot(t, x)
plt.title("Position vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True)
plt.savefig("results/position.png", dpi=200)

plt.show()
print("图像已保存到 results/ 文件夹")
