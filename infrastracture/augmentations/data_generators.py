import tensorflow as tf

class DataGenerators:
    def __init__(self, config, logger):
        self.logger=logger
        self.__init_generators(config)

    def __init_generators(self, config):
        self.train = self.__create_data_generator(config["augmentation"]["train"])
        self.validation = self.__create_data_generator(config["augmentation"]["validation"])
        self.test = self.__create_data_generator(config["augmentation"]["test"])
        self.logger.info("Generators created.")

    def __create_data_generator(self, config):
        return tf.keras.preprocessing.image.ImageDataGenerator(**config)

    def get_generators(self):
        return [self.train, self.validation, self.test]