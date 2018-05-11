import pandas as pd
import numpy as np

with open('general/matches_2017-2018.json') as rounds_json:
	rounds = pd.read_json(rounds_json)

print(rounds)
rounds = np.asarray(rounds)
print(rounds[:,11])