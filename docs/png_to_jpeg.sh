#! /bin/bash

find . -iname "*.png" -type f -exec sh -c 'sips -s format jpeg "$0" --out "${0%.png}.jpeg"' {} \;
