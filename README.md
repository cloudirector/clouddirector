```python
import os

class Cloudirector:
    def __init__(self):
        self.experience = None
        self.website = "https://cloudirector.github.io/"
    def say_hello(self):
        print("wsp nerds go look at my spaghetti code")
    def open_website(self):
        os.system(f"/bin/chromium {self.website}")

me = Cloudirector()
me.say_hello()
me.open_website()
```
