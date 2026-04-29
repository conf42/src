#! /bin/bash

DIRS="./docs/assets/headshots ./docs/assets/splash ./docs/assets/podcasts"

# mac (sips built-in)
if [ "$(uname)" == "Darwin" ]; then
    for dir in $DIRS; do
        [ -d "$dir" ] && find "$dir" -iname "*.png" -type f -exec sh -c 'sips -Z 500 -s format jpeg "$0" --out "${0%.png}.jpg"' {} \; || true
    done
# linux (imagemagick)
else
    for dir in $DIRS; do
        [ -d "$dir" ] && find "$dir" -iname "*.png" -type f | xargs --verbose -n 1 bash -c 'convert "$0" -resize 500 "${0%.*}.jpg"' || true
    done
fi

# optimize JPGs (quality only, no resize) if jpegoptim is available
if command -v jpegoptim &> /dev/null; then
    for dir in $DIRS; do
        [ -d "$dir" ] && find "$dir" -iname "*.jpg" -type f -exec jpegoptim --max=80 --strip-all {} \; || true
    done
fi
