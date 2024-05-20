#!/bin/bash

# This script lists all the files in the specified directory.
RUTA="/etc/"

for archivo in "$RUTA"/*
do
    if [ -f "$archivo" ]; then
        echo "Archivo encontrado: $(basename "$archivo")"
    fi
done
