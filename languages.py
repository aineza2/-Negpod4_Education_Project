# languages.py

# Define the list of languages supported by the app
supported_languages = ["Spanish", "French", "German", "Japanese", "Yoruba", "Hausa", "Igbo", "Kinyarwanda"]

# Define a dictionary to store language problem sets (replace this with actual data)
language_problem_sets = {
    "Spanish": {
        1: {"Hola": "Hello", "Gato": "Cat", "Casa": "House"},
        2: {"Perro": "Dog", "Sol": "Sun", "Libro": "Book"},
        3: {"Amigo": "Friend", "Jardín": "Garden", "Árbol": "Tree"},
        4: {"Tiempo": "Weather", "Trabajo": "Work", "Cocina": "Kitchen"},
        5: {"Playa": "Beach", "Bosque": "Forest", "Viaje": "Trip"},
        # Add more levels for Spanish
    },
    "French": {
        1: {"Bonjour": "Hello", "Chat": "Cat", "Maison": "House"},
        2: {"Chien": "Dog", "Soleil": "Sun", "Livre": "Book"},
        3: {"Ami": "Friend", "Jardin": "Garden", "Arbre": "Tree"},
        4: {"Temps": "Weather", "Travail": "Work", "Cuisine": "Kitchen"},
        5: {"Plage": "Beach", "Forêt": "Forest", "Voyage": "Trip"},
        # Add more levels for French
    },
    "German": {
        1: {"Guten Tag": "Good day", "Katze": "Cat", "Haus": "House"},
        2: {"Hund": "Dog", "Sonne": "Sun", "Buch": "Book"},
        3: {"Freund": "Friend", "Garten": "Garden", "Baum": "Tree"},
        4: {"Wetter": "Weather", "Arbeit": "Work", "Küche": "Kitchen"},
        5: {"Strand": "Beach", "Wald": "Forest", "Reise": "Trip"},
        # Add more levels for German
    },
    "Japanese": {
        1: {"こんにちは": "Hello", "ねこ": "Cat", "いえ": "House"},
        2: {"いぬ": "Dog", "たいよう": "Sun", "ほん": "Book"},
        3: {"ともだち": "Friend", "にわ": "Garden", "き": "Tree"},
        4: {"てんき": "Weather", "しごと": "Work", "だいどころ": "Kitchen"},
        5: {"うみ": "Beach", "もり": "Forest", "りょこう": "Trip"},
        # Add more levels for Japanese
    },
    "Yoruba": {
        1: {"Bawo ni": "How are you", "Eja": "Fish", "Ile": "Home"},
        2: {"Omi": "Water", "Igba": "Time", "Ina": "Fire"},
        3: {"Oruko": "Name", "Alẹ": "Land", "Ẹsẹ": "Food"},
        4: {"Ìrò ayé": "World", "Ilẹ̀": "Earth", "Ododo": "Flower"},
        5: {"Ounje": "Meal", "ẹjẹ": "Blood", "Oyin": "Honey"},
        # Add more levels for Yoruba
    },
    "Hausa": {
        1: {"Sannu": "Hello", "Kifi": "Monkey", "Gida": "House"},
        2: {"Kaza": "Chicken", "Rana": "Day", "Ƙofa": "Door"},
        3: {"Yara": "Child", "Tafiya": "Journey", "Kasuwa": "Market"},
        4: {"Gabas": "Sunrise", "Daki": "Bed", "Ilimi": "Knowledge"},
        5: {"Ƙasa": "Country", "Kwana": "Month", "Yanayi": "Heat"},
        # Add more levels for Hausa
    },
    "Igbo": {
        1: {"Kedu": "Hello", "Okuko": "Rooster", "Obi": "Heart"},
        2: {"Mmiri": "Water", "Egbe": "Sky", "Ilo": "Stomach"},
        3: {"Ora": "Seed", "Ije": "Journey", "Nri": "Rain"},
        4: {"Igu": "Fire", "Akwụkwọ": "Hand", "Ọgụ": "War"},
        5: {"Ọma": "Good", "Ikpọ": "Farm", "Ọkụ": "Tortoise"},
        # Add more levels for Igbo
    },
    "Kinyarwanda": {
        1: {'Igitondo' : 'Morning', 'Inkoko' : 'Chicken', 'Isake' : 'Rooster'},
        2: {'Injangwe' : 'Cat', 'Imbwa' : 'Dog', 'Umuntu' : 'Person'},
        3: {'Imbabazi' : 'Apologies', 'Ibiryo' : 'Food', 'Amazi' : 'Water'},
        4: {'Igihugu' : 'Country', 'Indabyo' : 'Flowers', 'Ifi' : 'Fish'},
        5: {'Imvura' : 'Rain', 'Umukobwa' : 'Girl', 'Umuhungu' : 'Boy'},
        6: {'Umugati' : 'Bread', 'Umuneke' : 'Banana', 'Imyenda' : 'Clothes'},
        
    },
    "Shona": {
        1: {"Mamuka sei": "Morning", "Huku": "Chicken", "Jongwe": "Rooster"},
        2: {"Mvura": "Water", "Denga": "Sky", "Dumbu": "Stomach"},
        3: {"Imba": "House", "Rwendo": "Journey", "Munhu": "Person"},
        4: {"Moto": "Fire", "Nyika": "Country", "Ruoko": "Hand"},
        5: {"Maruva": "Flowers", "Musikana": "Girl", "Mukomana": "Boy"},
        # Add more levels for Shona
    },
    "Ndebele": {
        1: {"Sakubona": "Hello", "Ngiyaphila": "I'm fine", "Ngidanile": "I'm sad"},
        2: {"Yebo": "Yes", "Hatshi": "No", "Mhlamunye": "Maybe"},
        3: {"Buya": "Come", "Hamba": "Go", "Inyamazana": "Animal"},
        4: {"Inja": "Dog", "Ibhiza": "Horse", "Inyama": "Meat"},
        5: {"Umumbhu": "Maize", "Ibizo": "Name", "Ubuhle": "Beauty"},
        # Add more levels for Ndebele
    },
    # Add problem sets for other languages
}
