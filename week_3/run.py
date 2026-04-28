import datasets
import regression

X, Y = datasets.load_linear_example()
model = regression.LinearRegression()
model.fit(X, Y)
print(model.theta)

print(model.predict(X))