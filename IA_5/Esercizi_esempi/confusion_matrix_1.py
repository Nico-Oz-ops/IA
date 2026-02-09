import numpy as np

# Confusion Matrix

# confusion_matrix = np.zeros([2,2])
# # print(confusion_matrix)
# # print(confusion_matrix[0][0])

# # input:  2 liste 

y_real = [1, 0, 1, 1, 2, 2]
y_pred = [1, 0, 0, 1, 2, 0]

# for i in range(len(y_real)): # ciclo su tutti gli indici del campione 
#     real = y_real[i] # etichetta real del i-esimo campione
#     predittivo = y_pred[i] # etichetta predetta per lo stesso campione 
#     confusion_matrix[predittivo][real] += 1 # aggiorno la confusion matrix, aggiungendo 1 alla cella corrispondente alla coppia (predittivo, real)

# print(confusion_matrix)

def confusion_matrix_generalizzat(y_real, y_pred, num_classi):
    confusion_matrix = np.zeros([num_classi, num_classi])

    for i in range(len(y_real)):
        real = y_real[i]
        pred = y_pred[i]
        confusion_matrix[real][pred] += 1
    
    return confusion_matrix

print(confusion_matrix_generalizzat(y_real, y_pred, 3))

# La data confusion matrix calcola la accuracy - con numpy

def accuracy(confusion_matrix):
    true_positives = np.trace(confusion_matrix) # somma degli elementi sulla diagonale principale
    total_samples = np.sum(confusion_matrix) # somma di tutti gli elementi della matrice
    print(true_positives)
    print(total_samples)
    return true_positives / total_samples
cm = [[1, 0, 0],[1, 2, 0],[1, 0, 1]]
print(accuracy(cm))

# La data confusion matrix calcola la accuracy senza numpy
def accuracy(confusion_matrix):
    true_positives = 0
    somma_totale = 0

    for i in range(len(confusion_matrix)):
        for j in range(len(confusion_matrix[i])):
            if i == j: # se sono sulla diagonale principale
                true_positives += confusion_matrix[i][j] # aggiungo il valore dei veri positvi
            somma_totale += confusion_matrix[i][j] # aggiungo il valore alla somma totale dei campioni
        
    return true_positives / somma_totale

cm = [[1, 0, 0],[1, 2, 0],[1, 0, 1]]
print(accuracy(cm))













