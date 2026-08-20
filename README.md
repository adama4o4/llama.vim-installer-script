DISCLAIMER: WILL ALTER YOUR .vimrc, Script has not been thoroughly tested, nor audited for security, RUN AT YOUR OWN RISK

Requires:
    - Python 3.10+
    - curl 8.18+
    - vim 9.1+

Simple installation script for the [llama.vim](https://github.com/ggml-org/llama.vim) plugin for [vim](https://github.com/vim/vim) w/ [vim-plug](https://github.com/junegunn/vim-plug), configured for [llama.cpp](https://github.com/ggml-org/llama.cpp). Meant for use on linux, may add more configuration options later.

Dependencies can be installed with: sudo apt install vim curl

Run with: python3 installer.py

User will be prompted for the infill link, uses default llama.cpp address if not specified.


This project is licensed under the MIT license.
