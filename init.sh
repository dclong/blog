# deps
python3 -m pip install \
    pelican \
    pelican-jupyter \
    pelican-render-math \
    beautifulsoup4 \
    typogrify \
    git+https://github.com/dclong/dsutil@main

# git submodules
git submodule init && git submodule update --recursive --remote

