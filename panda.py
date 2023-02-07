#  *** *** pandas  *** ***

# Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning,
# exploring, and manipulating data. The name "Pandas" has a reference to both "Panel Data",
# and "Python Data Analysis
# Pandas allows you to transform metadata (column/row labels) flexibly; in SQL you cannot. And poof,
# just like that, it's gone! Unfortunately, SQL doesn't give you the ability to operate on column names
# in the same way as Pandas. You'll need to manually specify how each column name will change

# example
import pandas as pd
import numpy as np
import re

data = np.array([[1,2],[3,4]])
heading = ["Rank","Sank"]
mydata = (pd.DataFrame(data=data,columns=heading))
print(mydata)

#  ################### #### How we can read the data #### #######################
# If you want to read a csv file
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke) # by mentioning poke.head(20) and poke.tail(20) we can see top and bottom 20 datas

# when you want to read a xlsx or excel work book
poke = pd.read_excel("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.xlsx")
print(poke.head(20))

# when dealing with text or txt file.
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.txt",delimiter="\t")
print(poke.tail(20))

# when you want the headings
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.columns)

# when you want to print a particular column
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke["Name"].head(20)) #it can be used= print(poke["Name"][0:20]) or print(poke.Name[0:5])

# when you want to print multiple column
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke[["Name","HP"]])  # it must be in nested square brackets to get them

# when try to print a particular row
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.iloc[55])  # iloc can be used to look at the serial no alone it cannot be used on string
print(poke.iloc[0:5]) # this prints 0 to 4 from the list

# to read a specific location for that you need row and column info
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.iloc[2,1]) # in this 2 is the row and 1 is the column

# to read a through all column and row
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
for index, row in poke.iterrows():
    print(row) # print(index,row)

# to read a through particular columns and all row
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
for index, row in poke.iterrows():
    print(row[['Name','HP']])

# to search a particular word from entire file and info along with it  *************
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.loc[poke['Name']=='Ivysaur'])

# to have the description of the data
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.describe())

# To sort the data
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
# print(poke.sort_values('Name').head(20))  # as a default it sorts in ascending order
# print(poke.sort_values('Names', ascending = False))
print(poke.sort_values(['Type 1', 'HP'], ascending=[1,0])) # in this the type is from
                                                           # ascending and HP in descending

#  ################### #### How to can change the data #### #####################

# adding a column to a already exist data  # but always double check if you use math when creating
# whether the total adds up or not 
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
poke["Total"]=poke['HP']+poke['Attack']+poke['Defense']+poke["Sp. Atk"]+poke["Sp. Def"]+poke["Speed"]
print(poke.head(20))
poke["Totals"]=poke['HP']+6 # way is also possible
print(poke.head(20))
poke['Totals']=poke.iloc[:,4:10].sum(axis=1) # axis = 0 is vertical we use horizontal cause of row need
print(poke.head(20))

# if you want to drop or delete any column
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
poke = poke.drop(columns=['Generation','Type 2'])
print(poke.columns) # to make the drop work you must assign it to a variable or dataframe

# arranging and moving of column
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
poke['Totals']=poke.iloc[:,4:10].sum(axis=1) # axis = 0 is vertical we use horizontal cause of row need
colum = list(poke.columns.values)
poke = poke[colum[0:10]+[colum[-1]]+colum[10:12]]
# print(poke.columns) # the reason I have inserted a list in column[-1] as it assume it as a string
    # and a list and we can concade list to a list only and single number is consider as string

# saving the file   # we need a active dataframe to make this work "__"  # index = false removes index
poke.to_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\Edited_pokidex.csv",index=False)

poke.to_excel("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\Edited_pokidex.xlsx",index=False)

poke.to_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\Edited_pokidex.txt",index=False,sep="/t")

# *** ****** ***********  filtering the data  *** ************* **********
# in pandas we don't use "and" instead we use "&".
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.loc[(poke["Type 1"] == "Electric") & (poke["Type 2"] == "Water")])

# in pandas we use | instead of "or".  | = or
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.loc[(poke["Type 1"] == "Electric") | (poke["Type 1"] == "Water")])

# we can you greater than and less than in pandas
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.loc[poke["HP"]>150])


# in pandas if you do not want somthing then use ~, this means not! THAT is (! and not) = ~
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.loc[ ~ poke["Name"].str.contains("Mega")])

# regular expression in pandas re.I means I = ignore the capitalization of the Types
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.loc[poke["Type 1"].str.contains("fire|grass", flags=re.I, regex=True)])

# Find the word using the starting or ending character, ^ this will get all the name with starting with
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.loc[poke["Name"].str.contains("^pi[a-z]", flags=re.I, regex=True)])
# for ending with pi
print(poke.loc[poke["Name"].str.contains("pi$", flags=re.I, regex=True)])

# if you want to change a data
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
poke.loc[poke["Type 1"] == "Electric", "Type 1"] = "Lightning"
print(poke.loc[poke["Type 1"]=="Lightning"])
poke.loc[poke["Type 1"] == "Electric", "Legendary"] = "True"  # we can use it to change other column also

# if you want to change two or more columns
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
poke.loc[poke["Speed"] > 80, ["Generation","Legendary"]] = "Epicuuu"
# or
poke.loc[poke["Speed"] > 80, ["Generation","Legendary"]] = ["Epicuuu","Dumdum"]
print(poke)

# groupby in pandas
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
print(poke.groupby(["Type 1"]).mean().sort_values("HP",ascending=False))

# count
poke = pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv")
# print(poke.groupby(["Type 1"]).count()["HP"])

print(poke.groupby(["Type 1","Type 2"]).count()["HP"])

# when working with large size of data
for poke in pd.read_csv("E:\\Task\\Knowledge\\PyNotes\\New\\Panda\\pandas-master\\pokemon_data.csv", chunksize=10):
    print(poke)

