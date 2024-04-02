import streamlit as st
import pandas as pd 
import seaborn as sns

st.set_page_config(
    page_title="Data Visualization App", 
    page_icon="🖼", 
    layout="centered"
)
st.title("Data Analysis and Visualization App")

st.markdown("This is a sample data visualization app built using Streamlit and AgGrid.")
st.markdown("The data used in this app is the famous Iris dataset, which contains information about the flowers of the Iris species.") 
st.markdown("You can explore the data by sorting, filtering.")   

iris_df = pd.read_csv('IRIS.csv')

# Species filter
species_filter = st.selectbox("Filter by Species", iris_df['species'].unique())

# Sepal Length slider
sepal_length_min, sepal_length_max = st.slider("Filter by Sepal Length Range", float(iris_df['sepal_length'].min()), float(iris_df['sepal_length'].max()), (float(iris_df['sepal_length'].min()), float(iris_df['sepal_length'].max())))

# Apply filters
filtered_df = iris_df[(iris_df['species'] == species_filter) & (iris_df['sepal_length'] >= sepal_length_min) & (iris_df['sepal_length'] <= sepal_length_max)]

# Display chart
st.subheader("Filtered Data")
st.write(filtered_df)

# Plot
st.header("Visualization")
plot_type = st.selectbox("Select Plot Type", ["Histogram", "Pairplot"])

if plot_type == "Histogram":
    feature = st.selectbox("Select a feature", iris_df.columns[:-1])
    fig = sns.histplot(filtered_df[feature], kde=True).get_figure()
    st.pyplot(fig)

elif plot_type == "Pairplot":
    fig = sns.pairplot(filtered_df, hue="species")
    st.pyplot(fig)
    
# Page 2: New Page
st.title("New Page")