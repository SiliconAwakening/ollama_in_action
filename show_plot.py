import matplotlib.pyplot as plt

data = {
    'A': 5.2,
    'B': 3.8,
    'C': 7.1
}

fig, ax = plt.subplots()
ax.bar(list(data.keys()), list(data.values()))

# Add some text for clarity
for i, v in enumerate(data.values()):
    ax.text(i, v + 0.2, str(v), ha='center')

# Set the chart title and labels
ax.set_title('Gene Expression Chart')
ax.set_xticks(list(range(len(data))))
ax.set_xticklabels(list(data.keys()))
ax.set_ylabel('Expression Level')
plt.show()