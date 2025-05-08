
import tkinter as tk
from tkinter import ttk, simpledialog
import matplotlib.pyplot as plt
import numpy as np

def graphs(v_data, t_data, M_data, V_data, w_data):
    import matplotlib.pyplot as plt
    data_elements = {
        "Deflection": v_data,
        "Angle": t_data,
        "Moment": M_data,
        "Shear": V_data,
        "Load": w_data
    }
    for data_name, data in data_elements.items():
        plt.figure(dpi=100)
        for y_vals, x_vals in data:
            plt.plot(x_vals, y_vals, color="green", label=data_name)
        plt.title(data_name)
        plt.xlabel("x (longitud)")
        plt.ylabel(data_name)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.autoscale()
    plt.show()
    data_elements = {
        "Deflection": v_data,
        "Angle": t_data,
        "Moment": M_data,
        "Shear": V_data,
        "Load": w_data
    }
    for data_name, data in data_elements.items():
        plt.figure()
        for data_tuple in data:
            plt.plot(data_tuple[1], data_tuple[0], color="green")
        plt.title(data_name)
        plt.xlabel("x")
        plt.ylabel(data_name)
        plt.grid(True)
    plt.show()

def array_fill(v, theta, M, V, w, d_range):
    v_data = [v(i) for i in d_range]
    t_data = [theta(i) for i in d_range]
    M_data = [M(i) for i in d_range]
    V_data = [V(i) for i in d_range]
    w_data = [w(i) for i in d_range]
    return [v_data, t_data, M_data, V_data, w_data]

def fix_support_and_single_load():
    L = float(simpledialog.askstring("Entrada", "Longitud L:"))
    E = float(simpledialog.askstring("Entrada", "Módulo de elasticidad E:"))
    I = float(simpledialog.askstring("Entrada", "Momento de inercia I:"))
    P = float(simpledialog.askstring("Entrada", "Carga puntual P:"))
    v = lambda x: -P/(6*E*I)*(3*L*x**2 - x**3)
    theta = lambda x: -P/(6*E*I)*(6*L*x - 3*x**2)
    M = lambda x: -P*(L - x)
    V = lambda x: -P
    w = lambda x: 0
    d_range = np.linspace(0, L, 50)
    
    v_data, t_data, M_data, V_data, w_data = array_fill(v, theta, M, V, w, d_range)
    graphs(
        [(v_data, d_range)],
        [(t_data, d_range)],
        [(M_data, d_range)],
        [(V_data, d_range)],
        [(w_data, d_range)]
    )
    

def fix_support_and_single_moment():
    L = float(simpledialog.askstring("Entrada", "Longitud L:"))
    E = float(simpledialog.askstring("Entrada", "Módulo de elasticidad E:"))
    I = float(simpledialog.askstring("Entrada", "Momento de inercia I:"))
    M0 = float(simpledialog.askstring("Entrada", "Momento M₀:"))
    v = lambda x: M0/(2*E*I)*x**2
    theta = lambda x: M0/(E*I)*x
    M = lambda x: M0
    V = lambda x: 0
    w = lambda x: 0
    d_range = np.linspace(0, L, 50)
    
    v_data, t_data, M_data, V_data, w_data = array_fill(v, theta, M, V, w, d_range)
    graphs(
        [(v_data, d_range)],
        [(t_data, d_range)],
        [(M_data, d_range)],
        [(V_data, d_range)],
        [(w_data, d_range)]
    )
    

def fix_support_and_single_displaced_load():
    L = float(simpledialog.askstring("Entrada", "Longitud L:"))
    E = float(simpledialog.askstring("Entrada", "Módulo de elasticidad E:"))
    I = float(simpledialog.askstring("Entrada", "Momento de inercia I:"))
    P = float(simpledialog.askstring("Entrada", "Carga puntual P:"))
    a = float(simpledialog.askstring("Entrada", "Distancia a desde empotramiento:"))
    v1 = lambda x: -P/(6*E*I)*(3*a*x**2 - x**3)
    theta1 = lambda x: -P/(6*E*I)*(6*a*x - 3*x**2)
    M1 = lambda x: -P*(a - x)
    V1 = lambda x: -P
    w1 = lambda x: 0
    r1 = np.linspace(0, a, 50)
    d1 = array_fill(v1, theta1, M1, V1, w1, r1)
    v2 = lambda x: -P*a**2/(6*E*I)*(3*x - a)
    theta2 = lambda x: -P*a**2/(6*E*I)*3
    M2 = lambda x: 0
    V2 = lambda x: 0
    w2 = lambda x: 0
    r2 = np.linspace(a, L, 50)
    d2 = array_fill(v2, theta2, M2, V2, w2, r2)
    graphs(
        [(d1[0], r1), (d2[0], r2)],
        [(d1[1], r1), (d2[1], r2)],
        [(d1[2], r1), (d2[2], r2)],
        [(d1[3], r1), (d2[3], r2)],
        [(d1[4], r1), (d2[4], r2)]
    )

def fix_support_and_dist_load():
    L = float(simpledialog.askstring("Entrada", "Longitud L:"))
    E = float(simpledialog.askstring("Entrada", "Módulo de elasticidad E:"))
    I = float(simpledialog.askstring("Entrada", "Momento de inercia I:"))
    q = float(simpledialog.askstring("Entrada", "Carga distribuida q:"))
    v = lambda x: -q/(24*E*I)*(x**4 - 4*L*x**3 + 6*L**2*x**2)
    theta = lambda x: -q/(24*E*I)*(4*x**3 - 12*L*x**2 + 12*L**2*x)
    M = lambda x: -q*(L - x)**2 / 2
    V = lambda x: -q*(L - x)
    w = lambda x: q
    d_range = np.linspace(0, L, 50)
    
    v_data, t_data, M_data, V_data, w_data = array_fill(v, theta, M, V, w, d_range)
    graphs(
        [(v_data, d_range)],
        [(t_data, d_range)],
        [(M_data, d_range)],
        [(V_data, d_range)],
        [(w_data, d_range)]
    )
    

def cantilever_triangular_dist_load():
    L = float(simpledialog.askstring("Entrada", "Longitud L:"))
    E = float(simpledialog.askstring("Entrada", "Módulo de elasticidad E:"))
    I = float(simpledialog.askstring("Entrada", "Momento de inercia I:"))
    q = float(simpledialog.askstring("Entrada", "Carga triangular máxima q:"))
    v = lambda x: -q*x**2/(120*L*E*I)*(10*L**3 - 10*L**2*x + 5*L*x**2 - x**3)
    theta = lambda x: -q/(120*L*E*I)*(20*L**3*x - 30*L**2*x**2 + 20*L*x**3 - 5*x**4)
    M = lambda x: -q*(L - x)**3 / (6*L)
    V = lambda x: -q*(L - x)**2 / (2*L)
    w = lambda x: q*(L - x)/L
    d_range = np.linspace(0, L, 50)
    
    v_data, t_data, M_data, V_data, w_data = array_fill(v, theta, M, V, w, d_range)
    graphs(
        [(v_data, d_range)],
        [(t_data, d_range)],
        [(M_data, d_range)],
        [(V_data, d_range)],
        [(w_data, d_range)]
    )
    

def simply_supported_intermediate_load():
    L = float(simpledialog.askstring("Entrada", "Longitud L:"))
    E = float(simpledialog.askstring("Entrada", "Módulo de elasticidad E:"))
    I = float(simpledialog.askstring("Entrada", "Momento de inercia I:"))
    P = float(simpledialog.askstring("Entrada", "Carga puntual P:"))
    a = float(simpledialog.askstring("Entrada", "Distancia a desde apoyo izquierdo:"))
    b = L - a
    v = lambda x: -P*b*x/(6*L*E*I)*(L**2 - b**2 - x**2)
    theta = lambda x: -P*b/(6*L*E*I)*(L**2 - b**2 - 3*x**2)
    M = lambda x: P*b*(L - x)/L
    V = lambda x: P*b/L
    w = lambda x: 0
    d_range = np.linspace(0, a, 50)
    
    v_data, t_data, M_data, V_data, w_data = array_fill(v, theta, M, V, w, d_range)
    graphs(
        [(v_data, d_range)],
        [(t_data, d_range)],
        [(M_data, d_range)],
        [(V_data, d_range)],
        [(w_data, d_range)]
    )
    

def simply_supported_end_moment():
    L = float(simpledialog.askstring("Entrada", "Longitud L:"))
    E = float(simpledialog.askstring("Entrada", "Módulo de elasticidad E:"))
    I = float(simpledialog.askstring("Entrada", "Momento de inercia I:"))
    M0 = float(simpledialog.askstring("Entrada", "Momento extremo M₀:"))
    divisions = int(simpledialog.askstring("Entrada", "Número de divisiones:"))
    v = lambda x: -M0*x/(6*E*I*L)*(L**2 - x**2)
    theta = lambda x: -M0/(6*E*I*L)*(L**2 - 3*x**2)
    M = lambda x: M0*(1 - 2*x/L)
    V = lambda x: -2*M0/L
    w = lambda x: 0
    d_range = np.linspace(0, L, divisions)
    
    v_data, t_data, M_data, V_data, w_data = array_fill(v, theta, M, V, w, d_range)
    graphs(
        [(v_data, d_range)],
        [(t_data, d_range)],
        [(M_data, d_range)],
        [(V_data, d_range)],
        [(w_data, d_range)]
    )
    

def simply_supported_dist_load():
    L = float(simpledialog.askstring("Entrada", "Longitud L:"))
    E = float(simpledialog.askstring("Entrada", "Módulo de elasticidad E:"))
    I = float(simpledialog.askstring("Entrada", "Momento de inercia I:"))
    q = float(simpledialog.askstring("Entrada", "Carga distribuida q:"))
    v = lambda x: -q*x/(24*E*I)*(x**3 - 2*L*x**2 + L**3)
    theta = lambda x: -q/(24*E*I)*(4*x**3 - 6*L*x**2)
    M = lambda x: q*(L*x - x**2/2)
    V = lambda x: q*(L - x)
    w = lambda x: q
    d_range = np.linspace(0, L, 50)
    
    v_data, t_data, M_data, V_data, w_data = array_fill(v, theta, M, V, w, d_range)
    graphs(
        [(v_data, d_range)],
        [(t_data, d_range)],
        [(M_data, d_range)],
        [(V_data, d_range)],
        [(w_data, d_range)]
    )
    

def simply_supported_ramped_load():
    L = float(simpledialog.askstring("Entrada", "Longitud L:"))
    E = float(simpledialog.askstring("Entrada", "Módulo de elasticidad E:"))
    I = float(simpledialog.askstring("Entrada", "Momento de inercia I:"))
    w0 = float(simpledialog.askstring("Entrada", "Carga máxima w₀:"))
    divisions = int(simpledialog.askstring("Entrada", "Número de divisiones:"))
    v = lambda x: -w0*x/(360*E*I*L)*(3*x**4 - 10*L**2*x**2 + 7*L**4)
    theta = lambda x: -w0/(360*E*I*L)*(15*x**4 - 30*L**2*x**2)
    M = lambda x: w0*(x**3 - 2*L**2*x)
    V = lambda x: w0*(3*x**2 - 2*L**2)
    w = lambda x: w0 * x / L
    d_range = np.linspace(0, L, divisions)
    
    v_data, t_data, M_data, V_data, w_data = array_fill(v, theta, M, V, w, d_range)
    graphs(
        [(v_data, d_range)],
        [(t_data, d_range)],
        [(M_data, d_range)],
        [(V_data, d_range)],
        [(w_data, d_range)]
    )
    

# UI FINALLLL
root = tk.Tk()
root.title("Análisis de Vigas")
root.geometry("600x550")
label = ttk.Label(root, text="Seleccione un caso estructural:", font=("Arial", 12))
label.pack(pady=10)


casos = [
    ("1) Cantilever con carga puntual en el extremo", fix_support_and_single_load),
    ("2) Cantilever con momento en el extremo", fix_support_and_single_moment),
    ("3) Cantilever con carga puntual desplazada", fix_support_and_single_displaced_load),
    ("4) Cantilever con carga distribuida uniforme", fix_support_and_dist_load),
    ("5) Cantilever con carga triangular", cantilever_triangular_dist_load),
    ("6) Simplemente apoyada con carga puntual intermedia", simply_supported_intermediate_load),
    ("7) Simplemente apoyada con momento en el extremo", simply_supported_end_moment),
    ("8) Simplemente apoyada con carga distribuida uniforme", simply_supported_dist_load),
    ("9) Simplemente apoyada con carga triangular", simply_supported_ramped_load),
]

for texto, funcion in casos:
    boton = ttk.Button(root, text=texto, command=funcion)
    boton.pack(pady=5, fill='x', padx=40)

root.mainloop()
