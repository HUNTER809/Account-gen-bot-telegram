import glob
from pathlib import Path
from AccountGen.utils import load_plugins
import logging
from . import HackerSpoilt

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "AccountGen/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully deployed AccountGenerator Bot!")
print("Enjoy! Do visit @HackerSpoilt")

if __name__ == "__main__":
    HackerSpoilt.run_until_disconnected()
              level=logging.WARNING)

path = "AccountGen/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully deployed AccountGenerator Bot!")
print("Enjoy! Do visit @HackerSpoilt")

if __name__ == "__main__":
    HackerSpoilt.run_until_disconnected()
)
