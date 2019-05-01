import pandas as pd

train = pd.read_csv("train.csv")
train_shape = train.shape
print(train_shape)

test = pd.read_csv("test.csv")
test_shape = test.shape
print(test_shape)

print(train.head(10))
