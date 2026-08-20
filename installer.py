"""

DISCLAIMER: WILL ALTER YOUR .vimrc, Script has not been thouroughly tested, nor audited for security, RUN AT YOUR OWN RISK

"""


from os import path
from subprocess import run


link = "\n"

def get_plug():

    global link = "https://localhost:8012/infill"
    print("Plug not found. Installing...")
    run(["curl", "-fLo", "~/.vim/autoload/plug.vim", "https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"])
    with open("~/.vimrc", "a") as f:
        f.write(f"\ncall plug#begin\nPlug \'ggml-org/llama.vim\'\ncall plug#end\ng:llama_config.endpoint = \"{link}\"")

def install():

    global link = input("enter endpoint (defaults to https://localhost:8012/infill, enter to skip): ")
    
    if link == "\n":
        global link = "https://localhost:8012/infill"

    if path.isfile("~/.vim/autoload/plug.vim"):
        lines = []
        print("Plug already installed.")
        with open(".vimrc", "r") as f:
            lines = f.readlines()
    
        with open(".vimrc", "w") as f:
    
            for j in lines:
    
                if j == "call plug#end":
                    f.write("\nPlug \'ggml-org/llama.vim\'")
                f.write(j)
    
            f.write(f"g:llama_config.endpoint = \"{link}\"")

    else:
        get_plug()

    run(["vim", "-c", "PlugInstall"])

install()
