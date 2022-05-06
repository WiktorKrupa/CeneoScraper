import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
id = input()

opinions = pd.read_json(f"opinions/"+id+".json")
print(opinions)