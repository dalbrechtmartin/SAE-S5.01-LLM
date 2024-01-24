class GenericModelWrapper:
    def __init__(self, model_config):
        self.model_config = model_config  # You can store any common configuration here

    def generate(self, prompt):
        raise NotImplementedError("This method should be implemented by the specific model wrapper.")
