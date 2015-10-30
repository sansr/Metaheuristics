#!/bin/bash

echo "Compilando...."
cd galib247/; make >> /dev/null; cd ..
echo "Ejecutando juego de cifras..."
echo "Parametros = [25 6 9 75 50 3 852]"
./cipher_game 25 6 9 75 50 3 852 >> scores.dat
