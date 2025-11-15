import yaml
from InterfaceAdapter import IdentityAdapter

class YAMLIdentityAdapter(IdentityAdapter):
    """Adapter para exportar metadatos en formato YAML compatible con Terraform."""
    def __init__(self, metadata):
        self.data = [
            {"user": user, "identity": user, "role": permission}
            for permission, users in metadata.items()
            for user in users
        ]

    def outputs(self):
        """Devuelve los metadatos listos para exportar."""
        return self.data
