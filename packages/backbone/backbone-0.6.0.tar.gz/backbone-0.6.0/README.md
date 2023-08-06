# Backbone

[![PyPI Version](https://img.shields.io/pypi/v/backbone.svg)](https://pypi.python.org/pypi/backbone/)

[Backbone](https://backbone.dev) is a framework for building end-to-end encrypted applications.

With Backbone, you and your users can share sensitive data securely and build tamper-proof infrastructure. Preserve user privacy, reduce compliance requirements and protect yourself from sophisticated cyber attacks. 

#### Basic Usage

```python
# Import the synchronous backbone module
from backbone import sync as backbone

# Login to your user account
with backbone.from_master_secret(user_name="dumbledore", master_secret="the-deathly-hallows") as client:
    # Operate within the hogwarts workspace
    workspace = client.with_workspace("hogwarts")
    
    # Create a spells namespace and store an end-to-end-encrypted incantation
    workspace.namespace.create("spells")
    workspace.entry.set("spells/disarm", "expelliarmus")
```

#### Documentation
Our [developer documentation](https://backbone.dev/docs) is the best resource to get started quickly. From our motivation behind the project, architecture overview to instructions on how to build and collaborate with Backbone.

#### Community
Backbone has a [Discord community](https://discord.gg/36M4yb6XSG) to provide support, discuss features and build together. Join us to help make Backbone better for everyone.

#### License

The Backbone Python SDK and Backbone Python CLI are developed and distributed under the BSL 1.1 license with a transition to the Apache 2.0 license planned on October 5th 2026.
