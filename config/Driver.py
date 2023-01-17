from abc import ABC, abstractmethod


class Driver(ABC):

    @abstractmethod
    def get_driver(self):
        """
        Return suitable browser driver
        :return:
        """