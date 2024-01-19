import scipy.optimize

# Objective Function: 50x_1 + 80x_2
# Constraint 1: 5x_1 + 2x_2 <=20
# Constraint 2: -10x_1 + -12x_2 <= -90

result = scipy.optimize.linprog(
    [50, 80], # Cost Function: 50x_1 + 80x_2
    A_ub=[[5, 2], [-10, -12]], # Coefficients for inequalities
    b_ub =[20, -90], # Constraints for inequalities
)

if result.success:
    print(f"X1: {round(result.x[0], 2)} hours")
    print(f"x2: {round(result.x[1], 2)} hours")
else:
    print("There is no solution. You can't always get what you want")

if __name__ == "__main__":
    print("Hello World")