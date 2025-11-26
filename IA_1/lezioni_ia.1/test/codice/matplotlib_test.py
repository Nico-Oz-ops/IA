import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)
fig, ax = plt.subplots() # Oggetti di tipo figura e asse per il grafico 
ax.plot(x, y)
plt.savefig('../visual/matplotlib_line.png')
print("matplotlib_line salvata in ../visual")
plt.show()

# import os
# import numpy as np
# import matplotlib.pyplot as plt

# # Percorso della cartella dove si trova lo script
# base_dir = os.path.dirname(__file__)
# save_dir = os.path.join(base_dir, '../visual')
# os.makedirs(save_dir, exist_ok=True)

# x = np.linspace(0, 2 * np.pi, 200)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)

# # Salva correttamente nella cartella "visual" accanto a "codice"
# plt.savefig(os.path.join(save_dir, 'matplotlib_line.png'))
# print(f"matplotlib_line salvata in {save_dir}")
# plt.show()
