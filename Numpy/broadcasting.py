import numpy as np

ages = np.array([12, 18, 20, 26, 67, 81, 74, 48, 17])

teenagers = ages[ages < 18]

adults = ages[(ages >= 18 & (ages <=65))]
seniors = ages[ages >= 65]

print("Teenagers: ", teenagers)
print("Adults : ", adults)
print("Seniors : ", seniors)

evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print("Evens : ", evens)
print("Odds: ", odds)