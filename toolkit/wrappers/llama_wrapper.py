from toolkit.wrappers.interface import GenericModelWrapper
from ctransformers import AutoModelForCausalLM

class LlamaWrapper(GenericModelWrapper):
    """
    @brief Wrapper class for interacting with a Llama model using the toolkit.
    
    This class extends GenericModelWrapper and provides Llama-specific functionality.
    """

    def __init__(self, model_config):
        """
        @brief Constructor for LlamaWrapper.
        
        @param model_config A dictionary containing configuration parameters for the model.
        """
        super().__init__(model_config)
        
        # Additional llama-specific initialization if needed
        self.llm = AutoModelForCausalLM.from_pretrained(
            model_config["llama_model"],
            model_file=model_config["llama_model_file"],
            model_type="llama",
            gpu_layers=0,
        )

    def generate(self, prompt):
        """
        @brief Generate a response from the Llama model based on the given prompt.
        
        @param prompt The input prompt for generating the response.
        @return The generated response from the Llama model.
        """
        response = self.llm(prompt)
        return response
