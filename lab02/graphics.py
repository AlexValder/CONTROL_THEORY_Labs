import matplotlib.pyplot as plt
from typing import List


def draw_phase_trajectory(xs: List[float], ys: List[float]) -> None:
    plt.xlabel('θ')
    plt.ylabel('dθ/dx')
    plt.title('Phase space trajectory')
    plt.show()
