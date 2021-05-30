import streamlit as st

import genanki


import random

def student():
    st.header('Mundo do Machado de Assis')

    if st.button('Esaú e Jacó'):
        my_model = genanki.Model(
            1091735104,
            'Simple Model with Media',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
                {'name': 'MyMedia'},                                  # ADD THIS
            ],
            templates=[
                {
                'name': 'Card 1',
                'qfmt': '{{Question}}<br>{{MyMedia}}',              # AND THIS
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
            ])

        my_note = genanki.Note(
        model=my_model,
        fields=['Capital of Argentina', 'Buenos Aires'])

        

        

    

    