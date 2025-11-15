import json
import access
from InterfaceAdapter import IdentityAdapter

class AWSIdentityAdapter(IdentityAdapter):
    def __init__(self, metadata):
        self.users = []
        for policy, users in metadata.items():
            for user in users:
                arn = f"arn:aws:iam::123456789012:user/{user}"
                self.users.append((user, arn, policy))

    def outputs(self):
        return self.users


class AWSProjectUsers:
    def __init__(self, users):
        self.users = users
        self.resources = self._build()

    def _build(self):
        aws_resources = {"resource": []}
        for (user, arn, policy) in self.users:
            user_res = {
                "aws_iam_user": {
                    user: {"name": user}
                }
            }
            attach_res = {
                "null_resource": {
                    f"attach_{user}_{policy}": {
                        "triggers": {
                            "user": user,
                            "arn": arn,
                            "policy": policy
                        }
                    }
                }
            }
            aws_resources["resource"].extend([user_res, attach_res])
        return aws_resources


if __name__ == "__main__":
    metadata = access.Infrastructure().resources
    users = AWSIdentityAdapter(metadata).outputs()
    with open("main_AWS.tf.json", "w") as f:
        json.dump(AWSProjectUsers(users).resources, f, indent=4)
