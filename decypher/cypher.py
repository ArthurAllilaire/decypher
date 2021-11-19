import matplotlib.pyplot as plt


letter_freq = "etaoinshrdlucwmfygpbvkxjqz"



def get_freq_vals(text):
    """
    Takes a text and returns a dict letter -> % presence

    """
    dic = {}
    for i in text:
        # Only add letters to the frequency distribution
        if not i.isalpha():
            continue
        if dic.get(i):
            dic[i] += 1
        else:
            dic[i] = 1
    if dic.get(" "):
        del dic[" "]
    for i in dic:
        dic[i] /= len(text) * 0.01

    dic = {k: v for k, v in sorted(
        dic.items(), key=lambda item: item[1], reverse=True)}

    return dic


def plot_freq_vals(text):
    results = get_freq_vals(text)
    plt.bar(range(len(results)),
            list(results.values()),
            tick_label=list(results.keys()))
    plt.show()
