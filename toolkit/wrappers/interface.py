class GenericModelWrapper:
    def __init__(self, model_config):
        """
        @brief Constructor for GenericModelWrapper class.

        Initializes an instance of the GenericModelWrapper class with the provided model configuration.

        @param model_config The configuration for the model. You can store any common configuration here.
        """
        self.model_config = model_config

    def generate(self, prompt):
        """
        @brief Generate method for the model wrapper.

        This method should be implemented by the specific model wrapper. It is responsible for generating output
        based on the given prompt.

        @param prompt The input prompt for generating the model output.

        @throw NotImplementedError This exception is raised if the method is not implemented by the specific model wrapper.
        """
        raise NotImplementedError("This method should be implemented by the specific model wrapper.")
