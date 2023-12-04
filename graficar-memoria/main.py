import subprocess as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()


def convertir_a_gb(number, isRounded=True, decimals=2):
    number_GB = number / (1024 ** 2)
    
    if isRounded:
        number_GB = round(number_GB, decimals)
    
    return number_GB

def obtener_total_ram():
    command = "cat /proc/meminfo | grep MemTotal | awk '{print $2}'"
    result = sp.run(command, shell=True, stdout=sp.PIPE, text=True)

    mem_total = int(result.stdout.strip())
    return mem_total

def obtener_libre_ram():
    command = "cat /proc/meminfo | grep MemFree | awk '{print $2}'"
    result = sp.run(command, shell=True, stdout=sp.PIPE, text=True)

    mem_free = int(result.stdout.strip())
    return mem_free

def graficar(frame):
    memoria_total = convertir_a_gb(obtener_total_ram())
    memoria_libre = convertir_a_gb(obtener_libre_ram())

    # Actualizar datos del gráfico
    etiquetas = ['Memoria ocupada', 'Memoria libre']
    valores = [memoria_libre, (memoria_total-memoria_libre)]

    ax.clear()
    bars = ax.bar(etiquetas, valores, color=['green', 'red'])
    
    # Agregar etiquetas con los valores totales
    for bar, valor in zip(bars, valores):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, f'{valor:.2f} GB', ha='center', va='bottom')

    ax.set_ylabel('Memoria (GB)')
    ax.set_title('Uso de Memoria')
    
    
def run():
    # Configurar la animación
    animation = FuncAnimation(fig, graficar, interval=1000)  # 5000 ms = 5 segundos
    plt.show()

if __name__ == "__main__":
    run()
