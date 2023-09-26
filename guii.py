import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
def find_most_similar():
    user_input = entry.get().strip().lower()
    most_similar_data = None
    max_similarity = 0.0
    for term in terms:
        similarity = cosine_similarity(vectorizer.transform([user_input]), vectorizer.transform([term]))[0][0]
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_data = term
    if most_similar_data:
        result_label.config(text=f"The most similar data to '{user_input}' is '{most_similar_data}' with a similarity score of {max_similarity:.2f}", foreground="green")
    else:
        result_label.config(text=f"No similar data found for '{user_input}'", foreground="red")

excel_file_path = 'Normalaization of terms 21 Sep 2023.xlsx'
df = pd.read_excel(excel_file_path)
terms = df['Terms'].tolist()
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(terms)
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)
root = tk.Tk()
root.title("Similarity Finder")
root.geometry("400x300")  
root.configure(bg="#f0f0f0")
label = tk.Label(root, text="Enter a term:", bg="#f0f0f0", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack()
button = tk.Button(root, text="Find Similar Data", command=find_most_similar, font=("Arial", 12), bg="#008CBA", fg="white")
button.pack(pady=15)
result_label = tk.Label(root, text="", wraplength=380, bg="#f0f0f0", font=("Arial", 12))
result_label.pack()
root.mainloop()
