#!/bin/bash

# Find and decompress all .bz2 files back to .motifs
for file in *.bz2; do
    if [[ -f "$file" ]]; then
        echo "Decompressing: $file"
        bzip2 -d "$file"
    fi
done

echo "Decompression complete!"

