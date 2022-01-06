import matplotlib.pyplot as plt

plt.plot([5, 10, 20, 100], "_") # ena linija
plt.plot([20, 20, 20, 40], "") # druga linija

plt.plot(["a","b", "c"], [10, 10, 20], "p", label="Testov")

plt.xlabel("Dan")
plt.ylabel("Število primerov")

plt.xticks([0, 10, 50], ["ena", "dve", "tri"])

plt.legend()

plt.title("Covid v Slo 😂")


plt.bar([4,5,6], [4,5,6])

plt.show() # prikaze graf