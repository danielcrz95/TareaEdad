#!/usr/bin/env python
# coding: utf-8

# ## Tarea 1 Geoinformatica
# - Gustavo Daniel Cruz Gutiérrez
# - Crear un algoritmo que compare las edades de los usuarios e imprima cual es el mas grande.

# In[3]:


nombre1 = input("Escriba el nombre: ")
edad1 = input("Escriba la edad: ")
nombre2 = input("Escriba el segundo nombre: ")
edad2 = input("Escriba la segunda edad: ")
if edad1>edad2:
    print("El mayor es:",nombre1)
else:
    print("El mayor es:",nombre2)

