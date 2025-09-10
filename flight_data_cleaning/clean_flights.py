import pandas as pd

#
df=pd.read_csv("flight_data_cleaning/data/airlines_flights_data.csv")

#prints the no of rows and columns 
print(df.shape)

#prints first five records
#print(df.head())

# Print column names
print("Columns:", df.columns.tolist())

print("dataType\n", df.dtypes)


#changing the type of column
df['index']=df['index'].astype("float64")
print(df.dtypes)

#find the min, max and average of price
min_price= df['price'].min()
max_price=df['price'].max()
average_price=df['price'].mean()
print("Minimun price:", min_price)
print("Maximum price:", max_price)
print("Average price:", average_price)

price_state=df['price'].agg(['min','max','mean'])
print("One line statement", price_state)

average_duration=df['duration'].mean()
print("average duration: ",average_duration)

#uniques airlne no
unique_airlines= df['airline'].unique()
print("unique_airlines", unique_airlines)
print(len(unique_airlines))

#flights going from Delhi → Mumbai
d_to_m= df[(df['source_city']=='Delhi') & (df['destination_city']=='Mumbai')]
print("Delhi to Mumbai ", d_to_m)
print(len(d_to_m))

cheapest_flight_row = df.loc[df['price'].min()]
cheapest_airline = cheapest_flight_row['airline']
cheapest_price = cheapest_flight_row['price']

print("Airline with the cheapest flight:", cheapest_airline)
print("Cheapest price:", cheapest_price)