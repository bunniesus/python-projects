import pandas as pd

artworks = pd.read_csv("ArtDiscovery/data/artworks.csv")

print(artworks.head())
print(artworks.shape)
print(artworks.columns)

print("\nShape:")
print(artworks.shape)

print("\nColumns:")
print(artworks.columns)

print("\nInfo:")
print(artworks.info())

print("\nMissing values:")
print(artworks.isnull().sum())