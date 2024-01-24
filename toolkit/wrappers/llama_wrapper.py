from toolkit.wrappers.interface import GenericModelWrapper
from ctransformers import AutoModelForCausalLM

class LlamaWrapper(GenericModelWrapper):
    def __init__(self, model_config):
        super().__init__(model_config)
        # Additional llama-specific initialization if needed
        self.llm = AutoModelForCausalLM.from_pretrained(
            model_config["llama_model"],
            model_file=model_config["llama_model_file"],
            model_type="llama",
            gpu_layers=0,
        )

    def generate(self, prompt):
        response = self.llm(prompt)
        return response
