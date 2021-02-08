# deps
python3 -m pip install \
    loguru \
    beautifulsoup4 typogrify \
    pelican pelican-jupyter pelican-render-math \
    git+https://github.com/dclong/dsutil@main

# git submodules
git submodule init && git submodule update --recursive --remote

