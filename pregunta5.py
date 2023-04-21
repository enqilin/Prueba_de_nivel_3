"""Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria– que resuelva las siguientes actividades:

realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
 determinar si un número está cargado en el árbol o no;
 eliminar tres valores del árbol;
 determinar la altura del subárbol izquierdo y del subárbol derecho;
 determinar la cantidad de ocurrencias de un elemento en el árbol;
"""

class NodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

class ArbolBinario(object):
    def insertar_nodo(raiz, nodo):
        if raiz is None:
            raiz= NodoArbol(nodo)
        
        elif nodo<raiz.info:
            raiz.izq=ArbolBinario.insertar_nodo(raiz.izq, nodo)
        else:
            raiz.der= ArbolBinario.insertar_nodo(raiz.der, nodo)
        return raiz
    def eliminar_nodo(raiz, clave):
        x= None
        if raiz is not None:
            if clave<raiz.info:
                raiz.izq, x= ArbolBinario.eliminar_nodo(raiz.izq, clave)
            elif clave>raiz.info:
                raiz.der, x= ArbolBinario.eliminar_nodo(raiz.der, clave)
            else:
                x= raiz.info
                if raiz.izq is None:
                    raiz= raiz.der
                elif raiz.der is None:
                    raiz= raiz.izq
                else:
                    raiz.izq, aux= ArbolBinario.remplazar(raiz.izq)
                    raiz.info= aux.info
        return raiz, x
    def arbolvacio(raiz):
        return raiz is None
    def preorden(raiz):
        if raiz is not None:
            print(raiz.info)
            ArbolBinario.preorden(raiz.izq)
            ArbolBinario.preorden(raiz.der)
    def inorden(raiz):
        if raiz is not None:
            ArbolBinario.inorden(raiz.izq)
            print(raiz.info)
            ArbolBinario.inorden(raiz.der)
    def postorden(raiz):
        if raiz is not None:
            ArbolBinario.postorden(raiz.der)
            print(raiz.info)
            ArbolBinario.postorden(raiz.izq)
    def por_nivel(raiz):
    

        
