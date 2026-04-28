import dataset1

df = dataset1.create_dataset()
df = dataset1.add_noise(df)

dataset1.save_dataset(df)

df2 = dataset1.load_dataset()
print(df2)