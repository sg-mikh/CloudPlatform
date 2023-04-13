from abc import ABC, abstractmethod


class BasePage(ABC):

    @property
    @abstractmethod
    def page_path(self):
        raise NotImplementedError
