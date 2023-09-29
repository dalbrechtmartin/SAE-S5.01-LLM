import subprocess
import time
import os

""" -------------------------------------------------------------------------------
USAGE : 
    subprocess.run( args, 
                    *, 
                    stdin=None, 
                    input=None, 
                    stdout=None, 
                    stderr=None, 
                    capture_output=False, 
                    shell=False, 
                    cwd=None, 
                    timeout=None, 
                    check=False, 
                    encoding=None, 
                    errors=None, 
                    text=None, 
                    env=None, 
                    universal_newlines=None, 
                    **other_popen_kwargs )

DOC : [https://docs.python.org/fr/3/library/subprocess.html#subprocess.run]
----------------------------------------------------------------------------- """

# Dependencies for Stable Diffusion & Llama 2
def install_dependencies():
    dependencies = [
        "GitPython==3.1.32",
        "Pillow==9.5.0",
        "accelerate==0.21.0",
        "basicsr==1.4.2",
        "blendmodes==2022",
        "clean-fid==0.1.35",
        "einops==0.4.1",
        "fastapi==0.94.0",
        "gfpgan==1.3.8",
        "gradio==3.41.2",
        "httpcore==0.15",
        "inflection==0.5.1",
        "jsonmerge==1.8.0",
        "kornia==0.6.7",
        "lark==1.1.2",
        "numpy==1.23.5",
        "omegaconf==2.2.3",
        "open-clip-torch==2.20.0",
        "piexif==1.1.3",
        "psutil==5.9.5",
        "pytorch_lightning==1.9.4",
        "realesrgan==0.3.0",
        "resize-right==0.0.2",
        "safetensors==0.3.1",
        "scikit-image==0.21.0",
        "timm==0.9.2",
        "tomesd==0.1.3",
        "torch", #Llama 2
        "torchdiffeq==0.2.3",
        "torchsde==0.2.5",
        "transformers" #Llama 2
    ]

    # Dependencies log file
    log_file = "logs/dependencies.log"

    if not os.path.exists("logs"):
        os.makedirs("logs")

    # Open log file with append mod
    with open(log_file, 'a') as log:
        for dependency in dependencies:
            # Redirect out/err to log file
            subprocess.run(["pip", "install", dependency], stdout=log, stderr=log)
    

def main():
    print("\n\t\t===============================================")
    print("\t\t           Démarrage de l'instalation")
    print("\t\t===============================================\n\n")

    time.sleep(2)

    print("\t\t1. Installation des dépendances en cours...")
    print("\t\t-----------------------------------------------\n")

    time.sleep(2)
    install_dependencies()

    print("\t\tDépendances installées.\n")
    time.sleep(1)
    print("\t\tPour plus de détails,\n\t\tveuillez consulter le fichier 'depenencies.log'\n\t\tdisponible dans le dossier 'logs'.\n")

    time.sleep(2)

    print("\n\t\t===============================================")
    print("\t\t              Fin de l'installation")
    print("\t\t===============================================\n")

if __name__ == "__main__":
    main()
