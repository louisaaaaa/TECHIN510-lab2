import streamlit as st
import pandas as pd 
import seaborn as sns

st.set_page_config(
    page_title="Data Visualization App", 
    page_icon="🖼", 
    layout="centered"
)
st.title("Data Analysis and Visualization App")
st.sidebar.success("Select a demo above.")

st.markdown("This is a sample data analysis and visualization app built using Streamlit. The data used in this app is the Iris Flowerdataset, which contains information about the flowers of the Iris species. The Iris dataset consists of 150 samples of iris flowers. There are three species of iris flowers in the dataset: setosa, versicolor, and virginica. For each sample, the dataset contains the following information: sepal length, sepal width, petal length, petal width, and the species of the flower.")
st.image('iris.jpg', caption='Iris Flower')
st.markdown("You can explore the data by sorting, filtering. You can also visualize the data using various plots such as histograms and pairplots.")   

st.header("Observations:")   
st.markdown("1. The dataset contains 150 samples of iris flowers.")
st.markdown("2. There are three species of iris flowers in the dataset: setosa, versicolor, and virginica.")
st.markdown("3. Iris virginica has the largest sepal length among the three species.")
st.markdown("4. Iris setosa has the smallest petal width among the three species.")   

st.markdown("Here is the Raw Data:")   

iris_df = pd.read_csv('IRIS.csv')

with st.expander("Raw Data"):
    st.write(iris_df)
# Species filter

st.markdown("You can fliter by species or by sepal length:")  
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
    
