from collections import Counter
import matplotlib.pyplot as plt

def frequency_analysis(text):
    text = ''.join(filter(str.isalpha, text.lower()))
    counts = Counter(text)
    sorted_counts = dict(sorted(counts.items()))
    plt.bar(sorted_counts.keys(), sorted_counts.values())
    plt.title("Letter Frequency")
    plt.xlabel("Letter")
    plt.ylabel("Count")
    plt.show()
