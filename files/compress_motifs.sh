#!/bin/bash

# Find and compress all files ending in .motifs
for file in *.motifs; do
    if [[ -f "$file" ]]; then
        echo "Compressing: $file"
        bzip2 "$file"
    fi
done

echo "Compression complete!"

