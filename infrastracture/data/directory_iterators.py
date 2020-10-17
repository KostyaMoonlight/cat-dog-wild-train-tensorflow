import numpy as np
import os
import tensorflow as tf

class DirectoryIterators:
    def __init__(self, generators, config, logger):
        self.config = config
        self.logger = logger
        self.__create_directory_iterators(generators)
    
    def __create_directory_iterators(self, generators):
        directories = self.__get_directories()
        iterator_configs = self.__get_iterator_configs()
        directory_iterators = map(self.__create_directory_iterator, 
                                  zip(directories, generators, iterator_configs))
        self.train_iterator, self.validation_iterator, self.test_iterator = directory_iterators
        self.logger.info("Iterators created.")


    def __create_directory_iterator(self, directory, generator, config):
        return  tf.keras.preprocessing.image.DirectoryIterator(
            directory, 
            generator, 
            **self.config
            )
       

    def __get_iterator_configs(self):
        train = self.config["iterator"]["train"]
        validation = self.config["iterator"]["validation"]
        test = self.config["iterator"]["test"]
        return [train, validation, test]

    def __get_directories(self):
        source = self.config["source"]
        train_directory = os.path.join(source, "train")
        validation_directory = os.path.join(source, "validation")
        test_directory = os.path.join(source, "test")
        directories = [train_directory, validation_directory, test_directory]
        for directory in directories:
            self.__validate_directory(directory)
        self.logger.info("Directory valdiated.")
        return directories

    def __validate_directory(self, directory):
        if not os.path.exists(directory):
            message = f"Directory {directory} does not exist!"
            self.logger.error(message)
            raise Exception(message)
        

    