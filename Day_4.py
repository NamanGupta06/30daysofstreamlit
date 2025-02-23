# Import python packages
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from snowflake.snowpark.context import get_active_session

st.header("st.write()")

#example 1
st.write('Hello, *World!* :sunglasses:')

#example 2
st.write(1234)

#example 3
df = pd.DataFrame({
    'first_column': [1,2,3,4],
    'second_column': ['naman',1,'muskaan', 2]
})
st.write(df)

#example 4
st.write('Below is a Dataframe',df,'After is a DataFrame')

#example 5
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
#A Pandas DataFrame (df2) is created with 200 rows and 3 columns (a, b, c).
#The values are randomly generated from a normal distribution (np.random.randn(200, 3)).
#The column names are 'a', 'b', and 'c'.
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
#alt.Chart(df2): Creates an Altair Chart using the DataFrame df2.
#.mark_circle(): Specifies that the chart should use circle markers (scatter plot).
#.encode(...): Defines how the data will be mapped to visual properties:
#x='a': Column 'a' is mapped to the x-axis.
#y='b': Column 'b' is mapped to the y-axis.
#size='c': Column 'c' determines the size of each circle (larger values = bigger circles).
#color='c': Column 'c' also determines the color of each circle.
#tooltip=['a', 'b', 'c']: Displays column values (a, b, c) when hovering over a point.

st.markdown("*Streamlit* is **really** ***cool***.")


# In addition to st.write, you can explore the other ways of displaying text:

# st.markdown
# st.header
# st.subheader
# st.caption
# st.text
# st.latex
# st.code
