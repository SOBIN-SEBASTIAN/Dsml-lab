import numpy as np
grades = np.array([85, 90, 78, 92, 88, 76, 95, 89, 84, 91])
print("Grades :")
print(grades)
print("\n Average of Grade in the class :")
print(np.mean(grades))
above_90=grades[grades>90]
print("\n Number of students scored above 90 :-")
print(np.count_nonzero(above_90))
print("\n Standard deviation of the grades :-")
print(np.std(grades))