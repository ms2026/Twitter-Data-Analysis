import streamlit as st, pandas as pd, datetime as dt

# Step 1 : Data Ingestion
# Data Ingestion into In-Memory Dataframe [can be Replaced with PySpark DF / RDDs]
df = pd.read_csv('correct_twitter_201904.tsv',sep = '\t')   # Tab Delimited Files
df['created_date'] = df['created_at'].apply(lambda x : x.split(' ')[0])
df['created_time'] = df['created_at'].apply(lambda x : x.split(' ')[1][0:5])
df['created_hour'] = df['created_time'].apply(lambda x : int(x.split(':')[0]))
df = df.iloc[:,[18,46,47,48, 16,17,14,26,45]]     # Read only required columns
df = df.fillna('')      # Replace NaN values with Empty String

# Streamlit App Title
st.set_page_config(layout="wide",page_title="Twitter Data Analysis")
st.header('Twitter Data Analysis',False)



# Identify Search Term and Filter Dataframe
search = st.text_input('🔍Enter Search Term',placeholder='music')
if not search:
    # Provide Default Value
    search = 'music' 

# Step 2 : Data Transformation
fdf = df.query('text.str.contains(@search)')


# Step 3 : Data Visualization

col1,col2,col3 = st.columns(3)

with col1:
    #How many unique users posted a tweet containing the term?
    st.write('👤How many unique users posted a tweet containing the term?')
    unq_users = fdf['author_id'].nunique()
    # Display Single Value Result
    st.subheader(unq_users)

with col2:
    #How many likes did tweets containing the term get, on average?
    st.write('❤️How many likes did tweets containing the term get, on average?')
    if unq_users == 0:
        avg_likes = 0
    else:
        avg_likes = round(fdf['like_count'].mean())
    # Display Single Value Result    
    st.subheader(avg_likes)

with col3:
    #Which user posted the most tweets containing the term?
    st.write('🌟Which user posted the most tweets containing the term?')
    rdf = fdf.groupby(fdf['author_handle'],as_index=False).size()
    rdf.columns = ['Author','Count']
    rdf = rdf.sort_values(by='Count',ascending = False)
    if rdf.shape[0] > 0:
        most_posted_user = rdf.iloc[0,0]
    else:
        most_posted_user = 'No Data Found'
    
    #Display Single Value Result
    st.subheader(most_posted_user)



#How many tweets were posted containing the term on each day?
st.subheader('📊Number of Tweets containing the term on each day')
tdf = fdf.groupby(fdf['created_date'],as_index=False).size()
tdf.columns = ['Date','Count']
rdf1 = tdf.sort_values(by='Count',ascending = False)
rdf1.fillna(0,inplace=True)
#Plotting the data
if rdf1.shape[0]>0:
    st.bar_chart(rdf1,x='Date',y='Count')
else:
    st.write('No Data Found')


#What times of day were the tweets posted at? [Search Term] ---> Hourly Distr
st.subheader('🕒What times of day were the tweets posted at?')
tdf = fdf.groupby(fdf['created_hour'],as_index=False).size()
tdf.columns = ['Hour','Count']
tdf.fillna(0,inplace=True)
# Plotting the data
if tdf.shape[0]>0:
    st.line_chart(tdf,x='Hour',y='Count')
else:
    st.write('No Data Found')

#Where (in terms of place IDs) did the tweets come from? [Search Term] ---> Place Distr 
st.subheader('📍Where (in terms of place IDs) did the tweets come from?')
fdf = fdf.query('place_id !="" ')
tdf = fdf.groupby(fdf['place_id'],as_index=False).size()
tdf.columns = ['Place','Count']
rdf2 = tdf.sort_values(by='Count',ascending = False)
rdf2.fillna(0,inplace=True)
#Plotting the data
if rdf2.shape[0]>0:
    st.bar_chart(rdf2,x='Place',y='Count')
else:
    st.write('No Data Found')   


