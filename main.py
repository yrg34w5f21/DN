# Import libraries
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

# Page Title
image_path = r'C:\\Users\\Acer\\Desktop\\BioInformatics\\dnacountwebapp\\dna-logo.jpg'

image = Image.open(image_path)
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide composition of a given DNA sequence!

***
""")

# Input Text Box
st.header('Enter DNA sequence')

# Example DNA sequence for initial input
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

# Display the text area for entering DNA sequence with a default example
sequence = st.text_area("Sequence input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]  # Skips the sequence name (first line)
sequence = ''.join(sequence)  # Concatenates list to string

# Add a horizontal line to separate input and output sections
st.write("""
***
""")

# Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

# DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Count)')

# 1. Print dictionary
st.subheader('1. Print dictionary')

# Define a function to count nucleotides and store in a dictionary
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C'))
    ])
    return d

# Apply the function to the input DNA sequence
X = DNA_nucleotide_count(sequence)

# Display the resulting dictionary
X

# 2. Print text
st.subheader('2. Print text')

# Display the count of each nucleotide in text format
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

# 3. Display DataFrame
st.subheader('3. Display DataFrame')

# Create a DataFrame from the dictionary for better visualization
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})

# Display the resulting DataFrame
st.write(df)

# 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')

# Create a bar chart using Altair and display it
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)
