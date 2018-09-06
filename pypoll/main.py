import pandas as pd

file = 'Resources/election_data.csv'

df = pd.read_csv(file)

#print(df.head(2))

#print(df.count())

#print(df.unique())
#print(df.describe())
#print(df.dtypes)

#print(df['Candidate'].value_counts())
candf=pd.DataFrame(df['Candidate'].value_counts())
#print(candf.iloc[:,1])
newdf=pd.DataFrame(data=candf)

#print(candf.head())

#print(newdf.head())
#x=newdf.max(axis=columns(1))
#print(x)


newcdf=newdf.sort_values('Candidate',ascending=False)
# print(newdf)
# print(newcdf)



newcdf.columns = ['TotalVotes']

df2=newcdf.reset_index()
df2.columns = ['Names','TotalVotes']

sumvotes=newcdf['TotalVotes'].sum()
maxivotes=newcdf['TotalVotes'].max()
minvotes=newcdf['TotalVotes'].min()
winner=df2.iloc[0,0]


# print(sumvotes)
# print(maxivotes)
# print(minvotes)
# print(winner)




print("Election Results")
print("----------------------------")
print(f"Total Votes: {str(sumvotes)}")
print("----------------------------")

percentage=newcdf["TotalVotes"]/sumvotes*100
newcdf['percentage']=percentage
newcdf['percentage']=newcdf['percentage'].map('{:.3f}%'.format)
newcdf['TotalVotes']=newcdf['TotalVotes'].map("({:})".format)
newcdf=newcdf[['percentage','TotalVotes']]
newcdf=newcdf.rename(columns={'percentage':'','TotalVotes':''})
print(newcdf)



print("----------------------------")
print(f"winner: {str(winner)}")
print("----------------------------")

with open("Output.txt", "w") as text_file:
    print("Election Results",file=text_file)
    print("----------------------------",file=text_file)
    print(f"Total Votes: {str(sumvotes)}",file=text_file)
    print("----------------------------",file=text_file)

  
    
    print(newcdf,file=text_file)



    print("----------------------------",file=text_file)
    print(f"winner: {str(winner)}",file=text_file)
    print("----------------------------",file=text_file)



# print(f"Total: ${str(total)}")
# print(f"Average  Change: ${str(avgchange)}")
# print(f"Greatest Increase in Profits:{maxdate} $({(max(avg_chgelist))})")
# print(f"Greatest Increase in Profits:{mindate} $({(min(avg_chgelist))})")





#print(newcdf.iloc[0,:])
#print(df2.iloc[0,:])
#print(index.loc[0])

#print(df2)
#print(df2.iloc[0,0])

# Export file as a CSV, without the Pandas index, but with the header
#file_one_df.to_csv("Output/fileOne.csv", index=False, header=True)
#file_df["avg_cost"] = file_df["avg_cost"].map("${:.2f}".format)
#renamed_df = organized_df.rename(columns={"Membership(Days)":"Membership in Days", "Weight":"Weight in Pounds"})
# thousands_of_dollars = data_file_pd["Amount"]/1000
# data_file_pd["Thousands of Dollars"] = thousands_of_dollars
# percentage=newcdf["TotalVotes"]/sumvotes*100
# newcdf['percentage']=percentage
# newcdf['percentage']=newcdf['percentage'].map('{:.3f}%'.format)
# newcdf['TotalVotes']=newcdf['TotalVotes'].map("({:})".format)
# newcdf=newcdf[['percentage','TotalVotes']]
# newcdf=newcdf.rename(columns={'percentage':'','TotalVotes':''})
# print(newcdf)