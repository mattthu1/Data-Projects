"""Create a historgram with 5 groups/bins for fave_numbers_df . Give it the title "Favorite
Numbers", label the horizontal axis "Number," and the vertical axis "Frequency"."""


import pandas as pd
import matplotlib.pyplot as plt

fave_numbers = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5]
fave_numbers_df = pd.DataFrame(fave_numbers, columns=['Number'])

plt.hist(fave_numbers_df['Number'], bins=5, edgecolor='k')

plt.title("Favorite Numbers")
plt.xlabel("Number")
plt.ylabel("Frequency")

plt.show()