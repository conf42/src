#! /bin/bash

# mac (sips built-in)
if [ "$(uname)" == "Darwin" ]; then
    find ./docs/assets/headshots -iname "*.png" -type f -exec sh -c 'sips -s format jpeg "$0" --out "${0%.png}.jpg"' {} \;
    find ./docs/assets/splash -iname "*.png" -type f -exec sh -c 'sips -s format jpeg "$0" --out "${0%.png}.jpg"' {} \;
    find ./docs/assets/podcasts -iname "*.png" -type f -exec sh -c 'sips -s format jpeg "$0" --out "${0%.png}.jpg"' {} \;
# linux (imagemagick)
else
    find ./docs/assets/headshots -iname "*.png" -type f | xargs --verbose -n 1 bash -c 'convert "$0" "${0%.*}.jpg"'
    find ./docs/assets/splash -iname "*.png" -type f | xargs --verbose -n 1 bash -c 'convert "$0" "${0%.*}.jpg"'
    find ./docs/assets/podcasts -iname "*.png" -type f | xargs --verbose -n 1 bash -c 'convert "$0" "${0%.*}.jpg"'
fi
