from abc import ABC, abstractmethod 

class AbstractClass(ABC):
    def __init__(self, name) -> None:   
        self.name = name

    @abstractmethod
    def getName(self):
        pass 

    @abstractmethod
    def setName(self):
        pass 

class AbstractClassInherit(AbstractClass):
    def __init__(self, name, language) -> None:
        super().__init__(name)
        self.language = language

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getLanguage(self):
        return self.language

    def setLanguage(self):
        return self.language


# jocefyne = AbstractClassInherit("Jocefyneroot", "Python")
# print(jocefyne.getLanguage())
# print(jocefyne.getName())
# jocefyne.setLanguage(("JavaScript"))
# print(jocefyne.getLanguage())



