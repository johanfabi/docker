#!/bin/bash

# This script checks the availability of a given URL by sending a HEAD request and checking the response code.

URL="https://www.google.com"

# Send a HEAD request to the URL and extract the response code using curl, head, and awk.
response=$(curl -s -I "$URL" | head -n 1 | awk '{print $2}')

# Check if the response code is 200 (OK) and display the appropriate message.
if [ "$response" = "200" ]; then
    echo "La URL $URL está disponible."
else
    echo "Advertencia: La URL $URL no está disponible (código de estado: $response)."
fi
