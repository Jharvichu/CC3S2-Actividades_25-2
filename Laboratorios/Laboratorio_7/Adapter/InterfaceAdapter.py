from abc import ABC, abstractmethod

class IdentityAdapter(ABC):
    @abstractmethod
    def outputs(self):
        """Debe retornar una lista de tuplas (user, identity, role)."""
        pass
