def bike_model_dynamics(t, state, delta, params):
    beta, r, x, y, psi = state
    m, Iz, a, b, Cf, Cr, v = params

    # Tire slip angles（关键）
    alpha_f = delta - beta - a * r / v
    alpha_r = -beta + b * r / v

    # Lateral forces
    Fyf = Cf * alpha_f
    Fyr = Cr * alpha_r

    # Dynamics
    beta_dot = (Fyf + Fyr) / (m * v) - r
    r_dot = (a * Fyf - b * Fyr) / Iz
    x_dot = v * np.cos(psi + beta)
    y_dot = v * np.sin(psi + beta)
    psi_dot = r

    return [beta_dot, r_dot, x_dot, y_dot, psi_dot]
