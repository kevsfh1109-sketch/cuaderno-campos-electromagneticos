from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import os

from scipy.constants import (
    epsilon_0,
    pi,
    G,
    e,
    m_e
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAFICAS_DIR = os.path.join(BASE_DIR, "..", "graficas")

os.makedirs(GRAFICAS_DIR, exist_ok=True)

k = 1 / (4 * pi * epsilon_0)


q1 = np.array([1, 2, 3, 4, 5]) * 1e-6
q2 = 1e-6
r = 1

Fe = k * np.abs(q1 * q2) / r**2

plt.figure(figsize=(8, 5))
plt.plot(q1 * 1e6, Fe, marker="o")

plt.xlabel(r"$q_1\;(\mu C)$")
plt.ylabel(r"$F_e\;(N)$")
plt.title("Fuerza eléctrica para diferentes valores de carga")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(GRAFICAS_DIR, "fuerza_electrica_carga.png"),
    dpi=300
)

plt.show()


q1 = 1e-6
q2 = 1e-6
r = np.linspace(0.1, 5, 500)

Fe = k * np.abs(q1 * q2) / r**2

plt.figure(figsize=(8, 5))
plt.plot(r, Fe)

plt.xlabel(r"Distancia $r\;(m)$")
plt.ylabel(r"$F_e\;(N)$")
plt.title("Fuerza eléctrica en función de la distancia")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(GRAFICAS_DIR, "fuerza_electrica_distancia.png"),
    dpi=300
)

plt.show()


m1 = np.array([1, 2, 3, 4, 5])
m2 = 1
r = 1

Fg = G * m1 * m2 / r**2

plt.figure(figsize=(8, 5))
plt.plot(m1, Fg, marker="o")

plt.xlabel(r"$m_1\;(kg)$")
plt.ylabel(r"$F_g\;(N)$")
plt.title("Fuerza gravitacional para diferentes valores de masa")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(GRAFICAS_DIR, "fuerza_gravitacional.png"),
    dpi=300
)

plt.show()


r = 1

Fe_electron = k * e**2 / r**2
Fg_electron = G * m_e**2 / r**2

print("==============================================")
print("COMPARACIÓN ENTRE DOS ELECTRONES")
print("==============================================")
print()

print("Fuerza eléctrica entre dos electrones:")
print(f"{Fe_electron:.5e} N")
print()

print("Fuerza gravitacional entre dos electrones:")
print(f"{Fg_electron:.5e} N")
print()

print("Relación Fe/Fg:")
print(f"{Fe_electron / Fg_electron:.5e}")
print()

fuerzas = [Fe_electron, Fg_electron]
nombres = [r"$F_e$", r"$F_g$"]

plt.figure(figsize=(7, 5))
plt.bar(nombres, fuerzas)

plt.yscale("log")
plt.ylabel("Fuerza (N)")
plt.title("Comparación de fuerzas entre dos electrones")

plt.grid(axis="y", which="both")
plt.tight_layout()

plt.savefig(
    os.path.join(GRAFICAS_DIR, "comparacion_electron.png"),
    dpi=300
)

plt.show()


r = np.linspace(0.1, 5, 500)
cargas = [1, 2, 3, 4, 5]

plt.figure(figsize=(9, 6))

for q in cargas:

    q_coulomb = q * 1e-6
    E = k * np.abs(q_coulomb) / r**2

    plt.plot(
        r,
        E,
        label=rf"$q={q}\,\mu C$"
    )

plt.xlabel(r"Distancia $r\;(m)$")
plt.ylabel(r"Campo eléctrico $E\;(N/C)$")
plt.title("Campo eléctrico para diferentes valores de carga")

plt.yscale("log")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()

plt.savefig(
    os.path.join(GRAFICAS_DIR, "campo_electrico_2d.png"),
    dpi=300
)

plt.show()


q = 1e-6

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)

X, Y = np.meshgrid(x, y)

R2 = X**2 + Y**2
R2[R2 < 0.05] = np.nan

E = k * np.abs(q) / R2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(
    X,
    Y,
    E,
    rcount=400,
    ccount=400,
    linewidth=0,
    antialiased=True
)

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel(r"$E$ (N/C)")

ax.set_title("Campo eléctrico producido por una carga puntual")

plt.tight_layout()

plt.savefig(
    os.path.join(GRAFICAS_DIR, "campo_electrico_3d.png"),
    dpi=400
)

plt.show()


r = np.linspace(0.1, 5, 500)
masas = [1, 2, 3, 4, 5]

plt.figure(figsize=(9, 6))

for M in masas:

    g = G * M / r**2

    plt.plot(
        r,
        g,
        label=rf"$M={M}\,kg$"
    )

plt.xlabel(r"Distancia $r\;(m)$")
plt.ylabel(r"Campo gravitacional $g\;(N/kg)$")
plt.title("Campo gravitacional para diferentes valores de masa")

plt.yscale("log")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()

plt.savefig(
    os.path.join(GRAFICAS_DIR, "campo_gravitacional_2d.png"),
    dpi=300
)

plt.show()


M = 1

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)

X, Y = np.meshgrid(x, y)

R2 = X**2 + Y**2
R2[R2 < 0.05] = np.nan

g = G * M / R2

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(
    X,
    Y,
    g,
    rcount=400,
    ccount=400,
    linewidth=0,
    antialiased=True
)

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel(r"$g$ (N/kg)")

ax.set_title("Campo gravitacional producido por una masa puntual")

plt.tight_layout()

plt.savefig(
    os.path.join(GRAFICAS_DIR, "campo_gravitacional_3d.png"),
    dpi=400
)

plt.show()


M = 1

r = np.linspace(0.1, 5, 500)

V = -G * M / r

plt.figure(figsize=(9, 6))

plt.plot(
    r,
    V,
    label=r"$V(r)=-\frac{GM}{r}$"
)

plt.xlabel(r"Distancia $r\;(m)$")
plt.ylabel(r"Potencial gravitacional $V\;(J/kg)$")
plt.title("Potencial gravitacional de una masa puntual")

plt.axhline(0, linewidth=1)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig(
    os.path.join(GRAFICAS_DIR, "potencial_gravitacional.png"),
    dpi=300
)

plt.show()


M = 1

x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)

X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2)
R[R < 0.2] = np.nan

V = -G * M / R

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(
    X,
    Y,
    V,
    rcount=400,
    ccount=400,
    linewidth=0,
    antialiased=True
)

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel(r"$V$ (J/kg)")

ax.set_title("Potencial gravitacional de una masa puntual")

plt.tight_layout()

plt.savefig(
    os.path.join(GRAFICAS_DIR, "potencial_gravitacional_3d.png"),
    dpi=400
)

plt.show()


print("==============================================")
print("GRÁFICAS GENERADAS CORRECTAMENTE")
print("==============================================")
print()

print("Las imágenes fueron guardadas en:")
print(os.path.abspath(GRAFICAS_DIR))

import os
import numpy as np
import matplotlib.pyplot as plt

EPSILON_0 = 8.8541878128e-12

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAFICAS_DIR = os.path.join(BASE_DIR, "..", "graficas")

os.makedirs(GRAFICAS_DIR, exist_ok=True)


def guardar(fig, nombre):
    ruta = os.path.join(GRAFICAS_DIR, nombre)
    fig.savefig(
        ruta,
        dpi=300,
        bbox_inches="tight"
    )
    plt.close(fig)


def hilo_infinito():
    lambdas = [
        -5e-6,
        -2.5e-6,
        -1e-6,
        2.5e-6,
        5e-6
    ]

    s = np.linspace(0.05, 2, 500)

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    for lam in lambdas:
        E = lam / (
            2 * np.pi * EPSILON_0 * s
        )

        ax.plot(
            s,
            E,
            label=f"λ = {lam * 1e6:.1f} μC/m"
        )

    ax.axhline(
        0,
        linewidth=0.8
    )

    ax.set_title(
        "Campo eléctrico de un hilo infinito"
    )

    ax.set_xlabel(
        "Distancia radial s (m)"
    )

    ax.set_ylabel(
        "Eₛ (N/C)"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    ax.legend()

    guardar(
        fig,
        "07_hilo_infinito_2D.png"
    )

    theta = np.linspace(
        0,
        2 * np.pi,
        250
    )

    s3d = np.linspace(
        0.05,
        2,
        250
    )

    S, T = np.meshgrid(
        s3d,
        theta
    )

    X = S * np.cos(T)
    Y = S * np.sin(T)

    lam = 5e-6

    E = lam / (
        2 * np.pi * EPSILON_0 * S
    )

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    ax.plot_surface(
        X,
        Y,
        E,
        cmap="viridis",
        linewidth=0
    )

    ax.set_title(
        "Campo eléctrico de un hilo infinito"
    )

    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("Eₛ (N/C)")

    guardar(
        fig,
        "07_hilo_infinito_3D.png"
    )


def espira_circular():
    lambdas = [
        -5e-6,
        -2.5e-6,
        -1e-6,
        2.5e-6,
        5e-6
    ]

    a = 1.0

    x = np.linspace(
        -3,
        3,
        600
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    for lam in lambdas:
        E = (
            lam * a * x
            /
            (
                2 * EPSILON_0 *
                (a**2 + x**2)**(3 / 2)
            )
        )

        ax.plot(
            x,
            E,
            label=f"λ = {lam * 1e6:.1f} μC/m"
        )

    ax.axhline(
        0,
        linewidth=0.8
    )

    ax.set_title(
        "Campo eléctrico sobre el eje de una espira cargada"
    )

    ax.set_xlabel(
        "x (m)"
    )

    ax.set_ylabel(
        "Eₓ (N/C)"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    ax.legend()

    guardar(
        fig,
        "08_espira_circular_2D_campo.png"
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    for lam in lambdas:
        V = (
            lam * a
            /
            (
                2 * EPSILON_0 *
                np.sqrt(a**2 + x**2)
            )
        )

        ax.plot(
            x,
            V,
            label=f"λ = {lam * 1e6:.1f} μC/m"
        )

    ax.axhline(
        0,
        linewidth=0.8
    )

    ax.set_title(
        "Potencial eléctrico sobre el eje de una espira"
    )

    ax.set_xlabel(
        "x (m)"
    )

    ax.set_ylabel(
        "V (V)"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    ax.legend()

    guardar(
        fig,
        "08_espira_circular_2D_potencial.png"
    )

    lam = 5e-6

    x3d = np.linspace(
        -3,
        3,
        500
    )

    E = (
        lam * a * x3d
        /
        (
            2 * EPSILON_0 *
            (a**2 + x3d**2)**(3 / 2)
        )
    )

    R = np.abs(E)

    phi = np.linspace(
        0,
        2 * np.pi,
        200
    )

    X, PHI = np.meshgrid(
        x3d,
        phi
    )

    R_surface = np.tile(
        R,
        (
            len(phi),
            1
        )
    )

    Y = R_surface * np.cos(PHI)
    Z = R_surface * np.sin(PHI)

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    ax.plot_surface(
        X,
        Y,
        Z,
        cmap="viridis",
        linewidth=0,
        antialiased=True
    )

    ax.set_title(
        "Geometría tridimensional del campo eléctrico de una espira"
    )

    ax.set_xlabel("x (m)")
    ax.set_ylabel("E")
    ax.set_zlabel("E")

    ax.set_box_aspect(
        (2.5, 1, 1)
    )

    guardar(
        fig,
        "08_espira_circular_3D_campo.png"
    )


def disco():
    sigmas = [
        -5e-6,
        -2.5e-6,
        -1e-6,
        2.5e-6,
        5e-6
    ]

    a = 1.0

    z = np.linspace(
        -3,
        3,
        600
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    for sigma in sigmas:
        E = (
            np.sign(z)
            * sigma
            /
            (2 * EPSILON_0)
            *
            (
                1 -
                np.abs(z)
                /
                np.sqrt(z**2 + a**2)
            )
        )

        E[z == 0] = 0

        ax.plot(
            z,
            E,
            label=f"σ = {sigma * 1e6:.1f} μC/m²"
        )

    ax.axhline(
        0,
        linewidth=0.8
    )

    ax.axvline(
        0,
        linewidth=0.8
    )

    ax.set_title(
        "Campo eléctrico sobre el eje de un disco"
    )

    ax.set_xlabel(
        "z (m)"
    )

    ax.set_ylabel(
        "Eᶻ (N/C)"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    ax.legend()

    guardar(
        fig,
        "09_disco_2D_campo.png"
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    for sigma in sigmas:
        V = (
            sigma
            /
            (2 * EPSILON_0)
            *
            (
                np.sqrt(z**2 + a**2)
                -
                np.abs(z)
            )
        )

        ax.plot(
            z,
            V,
            label=f"σ = {sigma * 1e6:.1f} μC/m²"
        )

    ax.axhline(
        0,
        linewidth=0.8
    )

    ax.set_title(
        "Potencial eléctrico sobre el eje de un disco"
    )

    ax.set_xlabel(
        "z (m)"
    )

    ax.set_ylabel(
        "V (V)"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    ax.legend()

    guardar(
        fig,
        "09_disco_2D_potencial.png"
    )

    rho = np.linspace(
        0.01,
        3,
        300
    )

    theta = np.linspace(
        0,
        2 * np.pi,
        300
    )

    R, T = np.meshgrid(
        rho,
        theta
    )

    sigma = 5e-6

    E3D = (
        sigma
        /
        (2 * EPSILON_0)
        *
        (
            1 -
            R /
            np.sqrt(R**2 + a**2)
        )
    )

    X = R * np.cos(T)
    Y = R * np.sin(T)

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    ax.plot_surface(
        X,
        Y,
        E3D,
        cmap="viridis",
        linewidth=0
    )

    ax.set_title(
        "Geometría tridimensional del campo eléctrico de un disco"
    )

    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("|E| (N/C)")

    guardar(
        fig,
        "09_disco_3D_campo.png"
    )


def dipolo_electrico():
    Q = 1e-6
    s = 0.5

    p = Q * s
    a = 1.0

    r = np.linspace(
        0.35,
        3,
        500
    )

    theta = np.linspace(
        0,
        2 * np.pi,
        600
    )

    R, T = np.meshgrid(
        r,
        theta
    )

    V = (
        p * np.cos(T)
        /
        (
            4 * np.pi *
            EPSILON_0 *
            R**2
        )
    )

    Er = (
        2 * p * np.cos(T)
        /
        (
            4 * np.pi *
            EPSILON_0 *
            R**3
        )
    )

    Etheta = (
        p * np.sin(T)
        /
        (
            4 * np.pi *
            EPSILON_0 *
            R**3
        )
    )

    E = np.sqrt(
        Er**2 +
        Etheta**2
    )

    V0 = (
        p /
        (
            4 * np.pi *
            EPSILON_0 *
            a**2
        )
    )

    E0 = (
        p /
        (
            4 * np.pi *
            EPSILON_0 *
            a**3
        )
    )

    V_norm = V / V0
    E_norm = E / E0

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="polar"
    )

    niveles = np.linspace(
        -8,
        8,
        41
    )

    contorno = ax.contourf(
        T,
        R,
        np.clip(
            V_norm,
            -8,
            8
        ),
        levels=niveles,
        cmap="coolwarm"
    )

    ax.contour(
        T,
        R,
        V_norm,
        levels=[0],
        linewidths=2
    )

    ax.set_title(
        "Potencial eléctrico normalizado de un dipolo"
    )

    fig.colorbar(
        contorno,
        ax=ax,
        pad=0.1,
        label="V / V₀"
    )

    guardar(
        fig,
        "10_dipolo_2D_potencial.png"
    )

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="polar"
    )

    niveles = np.linspace(
        0,
        16,
        41
    )

    contorno = ax.contourf(
        T,
        R,
        np.clip(
            E_norm,
            0,
            16
        ),
        levels=niveles,
        cmap="viridis"
    )

    ax.set_title(
        "Magnitud del campo eléctrico normalizado de un dipolo"
    )

    fig.colorbar(
        contorno,
        ax=ax,
        pad=0.1,
        label="|E| / E₀"
    )

    guardar(
        fig,
        "10_dipolo_2D_campo.png"
    )

    theta3d = np.linspace(
        0,
        np.pi,
        300
    )

    phi3d = np.linspace(
        0,
        2 * np.pi,
        400
    )

    TH, PH = np.meshgrid(
        theta3d,
        phi3d
    )

    R_esfera = np.ones_like(
        TH
    )

    V_esfera = np.cos(
        TH
    )

    Er_esfera = (
        2 *
        np.cos(TH)
    )

    Etheta_esfera = np.sin(
        TH
    )

    E_esfera = np.sqrt(
        Er_esfera**2 +
        Etheta_esfera**2
    )

    X = (
        R_esfera *
        np.sin(TH) *
        np.cos(PH)
    )

    Y = (
        R_esfera *
        np.sin(TH) *
        np.sin(PH)
    )

    Z = (
        R_esfera *
        np.cos(TH)
    )

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    ax.plot_surface(
        X,
        Y,
        Z,
        facecolors=plt.cm.coolwarm(
            (V_esfera + 1) / 2
        ),
        linewidth=0,
        antialiased=True
    )

    ax.set_title(
        "Potencial eléctrico del dipolo en coordenadas esféricas"
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_box_aspect(
        (1, 1, 1)
    )

    guardar(
        fig,
        "10_dipolo_3D_potencial.png"
    )

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    E_color = (
        E_esfera -
        np.min(E_esfera)
    ) / (
        np.max(E_esfera) -
        np.min(E_esfera)
    )

    ax.plot_surface(
        X,
        Y,
        Z,
        facecolors=plt.cm.viridis(
            E_color
        ),
        linewidth=0,
        antialiased=True
    )

    ax.set_title(
        "Magnitud del campo eléctrico del dipolo en coordenadas esféricas"
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_box_aspect(
        (1, 1, 1)
    )

    guardar(
        fig,
        "10_dipolo_3D_campo.png"
    )


def cuadrupolo_electrico():
    Q = 1e-6
    s = 0.5

    A = (
        Q * s**2
        /
        (
            16 * np.pi *
            EPSILON_0
        )
    )

    r = np.linspace(
        0.35,
        3,
        500
    )

    theta = np.linspace(
        0,
        2 * np.pi,
        600
    )

    R, T = np.meshgrid(
        r,
        theta
    )

    V = (
        A *
        (
            3 * np.cos(T)**2 -
            1
        )
        /
        R**3
    )

    Er = (
        3 * A *
        (
            3 * np.cos(T)**2 -
            1
        )
        /
        R**4
    )

    Etheta = (
        6 * A *
        np.sin(T) *
        np.cos(T)
        /
        R**4
    )

    E = np.sqrt(
        Er**2 +
        Etheta**2
    )

    V0 = A
    E0 = 3 * A

    V_norm = V / V0
    E_norm = E / E0

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="polar"
    )

    niveles = np.linspace(
        -10,
        10,
        41
    )

    contorno = ax.contourf(
        T,
        R,
        np.clip(
            V_norm,
            -10,
            10
        ),
        levels=niveles,
        cmap="coolwarm"
    )

    ax.contour(
        T,
        R,
        V_norm,
        levels=[0],
        linewidths=2
    )

    ax.set_title(
        "Potencial eléctrico normalizado de un cuadrupolo"
    )

    fig.colorbar(
        contorno,
        ax=ax,
        pad=0.1,
        label="V / V₀"
    )

    guardar(
        fig,
        "11_cuadrupolo_2D_potencial.png"
    )

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="polar"
    )

    niveles = np.linspace(
        0,
        20,
        41
    )

    contorno = ax.contourf(
        T,
        R,
        np.clip(
            E_norm,
            0,
            20
        ),
        levels=niveles,
        cmap="viridis"
    )

    ax.set_title(
        "Magnitud del campo eléctrico normalizado de un cuadrupolo"
    )

    fig.colorbar(
        contorno,
        ax=ax,
        pad=0.1,
        label="|E| / E₀"
    )

    guardar(
        fig,
        "11_cuadrupolo_2D_campo.png"
    )

    theta3d = np.linspace(
        0,
        np.pi,
        300
    )

    phi3d = np.linspace(
        0,
        2 * np.pi,
        400
    )

    TH, PH = np.meshgrid(
        theta3d,
        phi3d
    )

    R_esfera = np.ones_like(
        TH
    )

    V_esfera = (
        3 * np.cos(TH)**2 -
        1
    )

    Er_esfera = (
        3 *
        (
            3 * np.cos(TH)**2 -
            1
        )
    )

    Etheta_esfera = (
        6 *
        np.sin(TH) *
        np.cos(TH)
    )

    E_esfera = np.sqrt(
        Er_esfera**2 +
        Etheta_esfera**2
    )

    X = (
        R_esfera *
        np.sin(TH) *
        np.cos(PH)
    )

    Y = (
        R_esfera *
        np.sin(TH) *
        np.sin(PH)
    )

    Z = (
        R_esfera *
        np.cos(TH)
    )

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    ax.plot_surface(
        X,
        Y,
        Z,
        facecolors=plt.cm.coolwarm(
            (V_esfera + 1) / 2
        ),
        linewidth=0,
        antialiased=True
    )

    ax.set_title(
        "Potencial eléctrico del cuadrupolo en coordenadas esféricas"
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_box_aspect(
        (1, 1, 1)
    )

    guardar(
        fig,
        "11_cuadrupolo_3D_potencial.png"
    )

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    E_color = (
        E_esfera -
        np.min(E_esfera)
    ) / (
        np.max(E_esfera) -
        np.min(E_esfera)
    )

    ax.plot_surface(
        X,
        Y,
        Z,
        facecolors=plt.cm.viridis(
            E_color
        ),
        linewidth=0,
        antialiased=True
    )

    ax.set_title(
        "Magnitud del campo eléctrico del cuadrupolo en coordenadas esféricas"
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_box_aspect(
        (1, 1, 1)
    )

    guardar(
        fig,
        "11_cuadrupolo_3D_campo.png"
    )


def esfera_uniforme():
    rho0 = 1e-6
    a = 1.0

    r = np.linspace(
        0.001,
        3 * a,
        700
    )

    E = np.where(
        r <= a,
        rho0 * r /
        (3 * EPSILON_0),
        rho0 * a**3 /
        (
            3 *
            EPSILON_0 *
            r**2
        )
    )

    V = np.where(
        r <= a,
        rho0 *
        (
            3 * a**2 -
            r**2
        )
        /
        (
            6 *
            EPSILON_0
        ),
        rho0 * a**3 /
        (
            3 *
            EPSILON_0 *
            r
        )
    )

    Qt = (
        4 *
        np.pi *
        rho0 *
        a**3 /
        3
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    ax.plot(
        r,
        E,
        linewidth=2
    )

    ax.axvline(
        a,
        linestyle="--",
        linewidth=1
    )

    ax.set_title(
        "Campo eléctrico de una esfera uniformemente cargada"
    )

    ax.set_xlabel(
        "r (m)"
    )

    ax.set_ylabel(
        "|E| (N/C)"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    guardar(
        fig,
        "12_esfera_uniforme_2D_campo.png"
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    ax.plot(
        r,
        V,
        linewidth=2
    )

    ax.axvline(
        a,
        linestyle="--",
        linewidth=1
    )

    ax.set_title(
        "Potencial eléctrico de una esfera uniformemente cargada"
    )

    ax.set_xlabel(
        "r (m)"
    )

    ax.set_ylabel(
        "V (V)"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    guardar(
        fig,
        "12_esfera_uniforme_2D_potencial.png"
    )

    theta = np.linspace(
        0,
        2 * np.pi,
        300
    )

    R, T = np.meshgrid(
        r,
        theta
    )

    E3D = np.where(
        R <= a,
        rho0 * R /
        (
            3 *
            EPSILON_0
        ),
        rho0 * a**3 /
        (
            3 *
            EPSILON_0 *
            R**2
        )
    )

    X = R * np.cos(T)
    Y = R * np.sin(T)

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    ax.plot_surface(
        X,
        Y,
        E3D,
        cmap="viridis",
        linewidth=0
    )

    ax.set_title(
        "Geometría tridimensional del campo eléctrico de una esfera"
    )

    ax.set_xlabel(
        "x (m)"
    )

    ax.set_ylabel(
        "y (m)"
    )

    ax.set_zlabel(
        "|E| (N/C)"
    )

    guardar(
        fig,
        "12_esfera_uniforme_3D_campo.png"
    )

    V3D = np.where(
        R <= a,
        rho0 *
        (
            3 * a**2 -
            R**2
        )
        /
        (
            6 *
            EPSILON_0
        ),
        rho0 * a**3 /
        (
            3 *
            EPSILON_0 *
            R
        )
    )

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    ax.plot_surface(
        X,
        Y,
        V3D,
        cmap="coolwarm",
        linewidth=0
    )

    ax.set_title(
        "Geometría tridimensional del potencial de una esfera"
    )

    ax.set_xlabel(
        "x (m)"
    )

    ax.set_ylabel(
        "y (m)"
    )

    ax.set_zlabel(
        "V (V)"
    )

    guardar(
        fig,
        "12_esfera_uniforme_3D_potencial.png"
    )

    print(
        f"Carga total esfera uniforme: {Qt:.4e} C"
    )


def esfera_densidad_variable():
    rho0 = 1e-6
    a = 1.0

    r = np.linspace(
        0.001,
        3 * a,
        700
    )

    rmax = (
        np.sqrt(5) *
        a /
        3
    )

    E = np.where(
        r <= a,
        rho0 /
        EPSILON_0 *
        (
            r / 3 -
            r**3 /
            (5 * a**2)
        ),
        2 *
        rho0 *
        a**3 /
        (
            15 *
            EPSILON_0 *
            r**2
        )
    )

    V = np.where(
        r <= a,
        rho0 /
        EPSILON_0 *
        (
            a**2 / 4 -
            r**2 / 6 +
            r**4 /
            (20 * a**2)
        ),
        2 *
        rho0 *
        a**3 /
        (
            15 *
            EPSILON_0 *
            r
        )
    )

    Qt = (
        8 *
        np.pi *
        rho0 *
        a**3 /
        15
    )

    Emax = (
        rho0 /
        EPSILON_0 *
        (
            rmax / 3 -
            rmax**3 /
            (5 * a**2)
        )
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    ax.plot(
        r,
        E,
        linewidth=2
    )

    ax.scatter(
        rmax,
        Emax,
        s=70,
        zorder=5
    )

    ax.axvline(
        rmax,
        linestyle="--",
        linewidth=1
    )

    ax.axvline(
        a,
        linestyle="--",
        linewidth=1
    )

    ax.annotate(
        r"$r_{\max}=\sqrt{5}a/3$",
        xy=(
            rmax,
            Emax
        ),
        xytext=(
            rmax + 0.2,
            Emax
        ),
        arrowprops=dict(
            arrowstyle="->"
        )
    )

    ax.set_title(
        "Campo eléctrico de una esfera con densidad radial variable"
    )

    ax.set_xlabel(
        "r (m)"
    )

    ax.set_ylabel(
        "|E| (N/C)"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    guardar(
        fig,
        "13_esfera_variable_2D_campo.png"
    )

    fig, ax = plt.subplots(
        figsize=(10, 6)
    )

    ax.plot(
        r,
        V,
        linewidth=2
    )

    ax.axvline(
        a,
        linestyle="--",
        linewidth=1
    )

    ax.set_title(
        "Potencial eléctrico de una esfera con densidad radial variable"
    )

    ax.set_xlabel(
        "r (m)"
    )

    ax.set_ylabel(
        "V (V)"
    )

    ax.grid(
        True,
        alpha=0.3
    )

    guardar(
        fig,
        "13_esfera_variable_2D_potencial.png"
    )

    theta = np.linspace(
        0,
        2 * np.pi,
        300
    )

    R, T = np.meshgrid(
        r,
        theta
    )

    E3D = np.where(
        R <= a,
        rho0 /
        EPSILON_0 *
        (
            R / 3 -
            R**3 /
            (5 * a**2)
        ),
        2 *
        rho0 *
        a**3 /
        (
            15 *
            EPSILON_0 *
            R**2
        )
    )

    X = R * np.cos(T)
    Y = R * np.sin(T)

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    ax.plot_surface(
        X,
        Y,
        E3D,
        cmap="viridis",
        linewidth=0
    )

    ax.set_title(
        "Geometría tridimensional del campo eléctrico"
    )

    ax.set_xlabel(
        "x (m)"
    )

    ax.set_ylabel(
        "y (m)"
    )

    ax.set_zlabel(
        "|E| (N/C)"
    )

    guardar(
        fig,
        "13_esfera_variable_3D_campo.png"
    )

    V3D = np.where(
        R <= a,
        rho0 /
        EPSILON_0 *
        (
            a**2 / 4 -
            R**2 / 6 +
            R**4 /
            (20 * a**2)
        ),
        2 *
        rho0 *
        a**3 /
        (
            15 *
            EPSILON_0 *
            R
        )
    )

    fig = plt.figure(
        figsize=(11, 8)
    )

    ax = fig.add_subplot(
        111,
        projection="3d"
    )

    ax.plot_surface(
        X,
        Y,
        V3D,
        cmap="coolwarm",
        linewidth=0
    )

    ax.set_title(
        "Geometría tridimensional del potencial eléctrico"
    )

    ax.set_xlabel(
        "x (m)"
    )

    ax.set_ylabel(
        "y (m)"
    )

    ax.set_zlabel(
        "V (V)"
    )

    guardar(
        fig,
        "13_esfera_variable_3D_potencial.png"
    )

    print(
        f"Carga total esfera variable: {Qt:.4e} C"
    )

    print(
        f"Radio del campo máximo: {rmax:.4f} m"
    )

    print(
        f"Campo máximo: {Emax:.4e} N/C"
    )


EPSILON_0 = 8.8541878128e-12

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAFICAS_DIR = os.path.join(BASE_DIR, "..", "graficas")
os.makedirs(GRAFICAS_DIR, exist_ok=True)

def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(os.path.join(GRAFICAS_DIR, nombre), dpi=300, bbox_inches="tight")
    plt.close(fig)

def energia_esfera():
    Q = 1e-6
    R = 1.0

    r = np.linspace(R, 5 * R, 600)

    dWdr = Q**2 / (8 * np.pi * EPSILON_0 * r**2)

    W_acumulada = Q**2 / (8 * np.pi * EPSILON_0) * (1 / R - 1 / r)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(r, dWdr, linewidth=2)

    ax.axvline(R, linestyle="--", linewidth=1)

    ax.set_title("Contribución diferencial de energía del campo eléctrico")
    ax.set_xlabel("Distancia radial r (m)")
    ax.set_ylabel(r"$dW/dr$ (J/m)")
    ax.grid(True, alpha=0.3)

    guardar(fig, "15_energia_esfera_2D.png")

def polinomios_legendre():
    x = np.linspace(-1, 1, 800)

    P0 = np.ones_like(x)
    P1 = x
    P2 = (3 * x**2 - 1) / 2
    P3 = (5 * x**3 - 3 * x) / 2
    P4 = (35 * x**4 - 30 * x**2 + 3) / 8
    P5 = (63 * x**5 - 70 * x**3 + 15 * x) / 8

    fig, ax = plt.subplots(figsize=(11, 7))

    ax.plot(x, P0, label=r"$P_0(x)$")
    ax.plot(x, P1, label=r"$P_1(x)$")
    ax.plot(x, P2, label=r"$P_2(x)$")
    ax.plot(x, P3, label=r"$P_3(x)$")
    ax.plot(x, P4, label=r"$P_4(x)$")
    ax.plot(x, P5, label=r"$P_5(x)$")

    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)

    ax.set_title("Polinomios de Legendre desde $P_0$ hasta $P_5$")
    ax.set_xlabel("x")
    ax.set_ylabel("$P_n(x)$")
    ax.set_xlim(-1, 1)
    ax.grid(True, alpha=0.3)
    ax.legend()

    guardar(fig, "16_polinomios_legendre_P0_P5.png")

energia_esfera()
polinomios_legendre()
hilo_infinito()
espira_circular()
disco()
dipolo_electrico()
cuadrupolo_electrico()
esfera_uniforme()
esfera_densidad_variable()
print("Gráficas generadas correctamente.")