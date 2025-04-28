import pandas as pd
import matplotlib.pyplot as plt

nodes_expanded_data = {
    'Puzzle': ['Puzzle 0 (Trivial)', 'Puzzle 2 (Easy)', 'Puzzle 4 (Oh Boy)', 'Puzzle 1 (Very Easy)', 'Puzzle 3 (Doable)'],
    'Uniform Cost Search': [1, 4, 100701, 4, 29],
    'Misplaced Tile Heuristic': [1, 3, 6195, 2, 5],
    'Manhattan Distance Heuristic': [1, 3, 589, 2, 5]
}

maximum_queue_size_data = {
    'Puzzle': ['Puzzle 0 (Trivial)', 'Puzzle 2 (Easy)', 'Puzzle 4 (Oh Boy)', 'Puzzle 1 (Very Easy)', 'Puzzle 3 (Doable)'],
    'Uniform Cost Search': [1, 4, 32237, 5, 18],
    'Misplaced Tile Heuristic': [1, 3, 3763, 3, 4],
    'Manhattan Distance Heuristic': [1, 3, 369, 3, 4]
}

order = ['Puzzle 0 (Trivial)', 'Puzzle 1 (Very Easy)', 'Puzzle 2 (Easy)', 'Puzzle 3 (Doable)', 'Puzzle 4 (Oh Boy)']
nodes_df = pd.DataFrame(nodes_expanded_data)
queue_df = pd.DataFrame(maximum_queue_size_data)

nodes_df.set_index('Puzzle').reindex(order).plot(kind='bar', stacked=True, ylabel='Number of Nodes Expanded', title='Number of Nodes Expanded', rot=0).set_yscale('log')
queue_df.set_index('Puzzle').reindex(order).plot(kind='line', title='Maximum Queue Size', rot=0).set_yscale('log')
plt.tight_layout()
plt.show()
