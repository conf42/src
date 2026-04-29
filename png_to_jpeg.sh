#! /bin/bash

# mac (sips built-in)
if [ "$(uname)" == "Darwin" ]; then
    find ./docs/assets/headshots -iname "*.png" -type f -exec sh -c 'sips -Z 500 -s format jpeg "$0" --out "${0%.png}.jpg"' {} \;
    find ./docs/assets/splash -iname "*.png" -type f -exec sh -c 'sips -Z 500 -s format jpeg "$0" --out "${0%.png}.jpg"' {} \;
    find ./docs/assets/podcasts -iname "*.png" -type f -exec sh -c 'sips -Z 500 -s format jpeg "$0" --out "${0%.png}.jpg"' {} \;
# linux (imagemagick)
else
    find ./docs/assets/headshots -iname "*.png" -type f | xargs --verbose -n 1 bash -c 'convert "$0" -resize 500 "${0%.*}.jpg"'
    find ./docs/assets/splash -iname "*.png" -type f | xargs --verbose -n 1 bash -c 'convert "$0" -resize 500 "${0%.*}.jpg"'
    find ./docs/assets/podcasts -iname "*.png" -type f | xargs --verbose -n 1 bash -c 'convert "$0" -resize 500 "${0%.*}.jpg"'
fi

# optimize JPGs (quality only, no resize) if jpegoptim is available
if command -v jpegoptim &> /dev/null; then
    find ./docs/assets/headshots -iname "*.jpg" -type f -exec jpegoptim --max=80 --strip-all {} \;
    find ./docs/assets/splash -iname "*.jpg" -type f -exec jpegoptim --max=80 --strip-all {} \;
    find ./docs/assets/podcasts -iname "*.jpg" -type f -exec jpegoptim --max=80 --strip-all {} \;
fi
