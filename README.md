# Week 1 — Simple 1D Vehicle Dynamics

本项目通过一个最简单的车辆动力学模型（1D 匀加速）来学习：

- ODE 微分方程求解（使用 scipy.solve_ivp）
- 速度 v(t) 和位置 x(t) 的数值模拟
- 使用 matplotlib 绘制曲线

---

## 🚗 模型介绍

车辆动力学模型如下：

\[
m \frac{dv}{dt} = F
\]
\[
\frac{dx}{dt} = v
\]

其中：

- \( m = 1000 \, kg \)
- \( F = 2000 \, N \)（恒定油门）
- 初始速度 \( v(0) = 0 \)
- 初始位置 \( x(0) = 0 \)

---

## 📁 文件结构

