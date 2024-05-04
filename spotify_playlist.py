#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import webbrowser

def choose_language():
    print("Choose a language:")
    print("1) Marathi\n2) Hindi\n3) English")
    return input("Enter the number of Language: ")

def choose_mood():
    print("Choose a mood:")
    print("1) Happy\n2) Sad\n3) Dance\n4) Chill\n5) Energetic\n6) Workout")
    return input("Enter the number of mood: ")

def get_playlist_url(language, mood):
    playlist_urls = {
        ('Marathi', 'Happy'): 'https://open.spotify.com/playlist/3Wq5c7G7NFeVX1LanIDjIr?si=4655a6192261486d',  
        ('Marathi', 'Sad'): 'https://open.spotify.com/playlist/0IdMRuqhwaj8Hi8P9zrRyq?si=K9xsMGhcTJ6MNVN0PJ6FIw&pi=Je9Zrc5yTVOVZ',   
        ('Marathi', 'Dance'): 'https://open.spotify.com/playlist/2cAfXf0ZlKLA4cU6vXRyjj?si=QfMvrw57T_qTZHYu6ZRm6w', 
        ('Marathi', 'Chill'): 'https://open.spotify.com/playlist/5327TZHZn9B43497N5FEUP?si=HEHX_AYyROmuXUMXxsyksw',  
        ('Marathi', 'Energetic'): 'https://open.spotify.com/playlist/3EuyHdVlTnmxLt4PSv1SHN?si=K9u-KP4rQQuZrrEi8_KjWA',  
        ('Marathi', 'Workout'): 'https://open.spotify.com/playlist/7pm3q0ZcwVeQWuu4JrxPlG?si=HIOnB5acS560QVQPErKfZw&pi=I89AcgF9Qxup8',  
        ('Hindi', 'Happy'): 'https://open.spotify.com/playlist/2KZDu2B5IbYlU0RoNSKBst?si=hms6A0d8S9qL5LlWjdivjA',  
        ('Hindi', 'Sad'): 'https://open.spotify.com/playlist/6E1JKoG82E6d7WsxxpubmH?si=MWKO-r_9TmSr4LDZkNH1uw',   
        ('Hindi', 'Dance'): 'https://open.spotify.com/playlist/0LKjGx23SMvQMqo6lnSBTY?si=PpoZNL6ZQRGGV_MdSqBkJQ', 
        ('Hindi', 'Chill'): 'https://open.spotify.com/playlist/40rbOzktObUtGVwk8LCXwX?si=ruFJf4GrTJmEqGv6EyH6yA',  
        ('Hindi', 'Energetic'): 'https://open.spotify.com/playlist/1SIWL4jchAXAQAGaBaazwQ?si=NbHe0E1CRYSOM7Qzuuv53w&pi=89dtJ3z8SxyMP', 
        ('Hindi', 'Workout'): 'https://open.spotify.com/playlist/7HXzQN0twIcNbqBUiUyLt0?si=tzARa55GSdmyj6J_R78C3w',  
        ('English', 'Happy'): 'https://open.spotify.com/playlist/0m48b6IdBElxyVceUsJ3sz?si=vOjyuRO8TySje7AXY1tuSA&pi=y628IiLTT1O2k',  
        ('English', 'Sad'): 'https://open.spotify.com/playlist/3R6UPQo3ZZl9x1HRRRwVCw?si=QtCfmVx_SMmVwN3AoD2x-w',   
        ('English', 'Dance'): 'https://open.spotify.com/playlist/4ryRcoyOhxGkX0baQy35rg?si=5iMOPcZmQ6GU7ZGs_uySsw',  
        ('English', 'Chill'): 'https://open.spotify.com/playlist/7z89rUI1EYfpLhrU4UYY1x?si=C3PEwN_cT8yyGSURT18iRg',  
        ('English', 'Energetic'): 'https://open.spotify.com/playlist/1biksfEXJvkcirpFRshkyC?si=QqVrFwodRpiNAsPE7X7gQQ',  
        ('English', 'Workout'): 'https://open.spotify.com/playlist/4DqxINSrStYNJ3zE8ZFLCx?si=ZRPZirGaRAaq_IUJQxPZ8g',  
    }
    return playlist_urls.get((language, mood), 'Invalid language or mood selection')

def open_spotify_playlist(playlist_url):
    webbrowser.open(playlist_url)

def main():
    language_choice = choose_language()
    mood_choice = choose_mood()

    languages = {'1': 'Marathi', '2': 'Hindi', '3': 'English'} 
    moods = {'1': 'Happy', '2': 'Sad', '3': 'Dance', '4': 'Chill', '5': 'Energetic', '6': 'Workout'}
    selected_language = languages.get(language_choice, 'Invalid language selection')
    selected_mood = moods.get(mood_choice, 'Invalid mood selection')

    print(f"\nSelected language: {selected_language}")
    print(f"Selected mood: {selected_mood}")

    playlist_url = get_playlist_url(selected_language, selected_mood)
    if playlist_url != 'Invalid language or mood selection':
        open_spotify_playlist(playlist_url)
    else:
        print("Invalid language or mood selection. Please try again.")

if __name__ == "__main__":
    main()


# In[ ]:




