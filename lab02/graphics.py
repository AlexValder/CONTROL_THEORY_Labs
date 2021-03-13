import matplotlib.pyplot as plt


def draw_phase_trajectory() -> None:
    plt.xlabel('θ')
    plt.ylabel('dθ/dx')
    plt.title('Phase space trajectory')
    plt.show()
