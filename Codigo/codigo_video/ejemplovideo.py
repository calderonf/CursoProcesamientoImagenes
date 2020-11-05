import numpy as np
import cv2

cap = cv2.VideoCapture(2)# 0 es la primera camara listada en su sistema

while(True):
    # Capture cuadro a cuadro
    ret, frame = cap.read()# por favor revise que el cuadro es valido, si no es valido termine el loop usando break.

    # Las operaciones que va a realizarle a cada cuadro irian aquí:
    # por ejemplo acá solo vamos a convertir a escala de grices
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # mostrar el cuadro y esperar una q de quit!! para salir, falta la condicion de salir por error de frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)# en sistemas posix (linux/mac) es necesario hacer esto para que funcione destroyAllWindows
