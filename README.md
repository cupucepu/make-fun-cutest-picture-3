# Otter Hug — make.fun cutest-picture-01 entry

A fluffy baby sea otter hugging a tiny baby harp seal pup, cheek to
cheek, in warm golden-hour light with soft garden bokeh. Two unlikely
friends, one very tight hug.

## How the entry works

1. `main.py` copies the vendored `picture.jpg` to `/output/entry.png`.
2. It reads the output back and compares it byte for byte with the source.
3. It parses the JPEG header (stdlib only) and checks the image is
   1024x1024.

Any mismatch or wrong size fails loudly; on success it prints a
confirmation line.

## Why this picture

The top entries in this contest are all photorealistic baby animals
hugging another baby animal. An otter and a seal pup are two different
species that would never meet in a garden — that unlikely friendship,
cheek to cheek, is the whole joke and the whole charm.
