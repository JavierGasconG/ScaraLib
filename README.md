# ScaraLib
Librería para relizar calculos con el robot scara SR6iA de Fanuc
Hay tres funciones directa, inversa y jacoviana
La función directa recive los parametros angulo theta 1, angulo theta 2, angulo theta 3 y exatension del brazo y devuelve una matriz con numpy de 4*4.
La función inversa revcira la tres coordenadas cartesianas en el expacio y la orientacion de la pinza y devolvera un array con 4 elementos que seran angulo theta 1, angulo theta 2, angulo theta 3 y exatension del brazo.
La función jacobiara recive angulo theta 1, angulo theta 2, angulo theta 3 y exatension del brazo y devuelve una matriz tipo numpy de 6*4.
