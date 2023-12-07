import sys
from ctransformers import AutoModelForCausalLM

def main():
    if len(sys.argv) == 1:
        print("Utilisation: " + sys.argv[0] + " <prompt>")
    else:
        prompt = sys.argv[1]

        print("Vérification du modèle en cours...")
        # Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
        llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-13B-Ensemble-v5-GGUF", model_file="llama-2-13b-ensemble-v5.Q5_K_M.gguf", model_type="llama", gpu_layers=0)
        print("Génération de la réponse en cours...")

        response = llm(prompt)

        print("Question : " + prompt + "\n\n")
        print("Réponse : " + response + "\n\n")

        print("Taille de la réponse : " + str(len(response)))

if __name__ == "__main__":
    main()
