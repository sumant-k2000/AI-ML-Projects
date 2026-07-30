# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python** and **Scikit-learn**. The system recommends similar movies by analyzing movie metadata such as genres, keywords, cast, crew, and plot overview. It uses **Natural Language Processing (NLP)** techniques and **Cosine Similarity** to find movies with similar content.

---

## Features

- Content-based movie recommendation
- Data preprocessing and feature engineering
- Text vectorization using CountVectorizer
- Similarity calculation using Cosine Similarity
- Fast movie recommendations based on content
- Model serialization using Pickle

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Pickle
- Google Colab

---

## Dataset

This project uses the **TMDb 5000 Movies Dataset**.

**Dataset Link:**  
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

### Required Files

- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

Download these files and upload them to Google Colab before running the notebook.

---

## Installation

Install the required libraries using:

```bash
pip install pandas numpy scikit-learn nltk
```

---

## Machine Learning Workflow

1. Load the movie and credits datasets.
2. Merge both datasets.
3. Perform data cleaning and preprocessing.
4. Extract important features (genres, keywords, cast, crew, overview).
5. Create a combined **tags** feature.
6. Convert text into numerical vectors using CountVectorizer.
7. Compute movie similarity using Cosine Similarity.
8. Recommend the top similar movies based on the selected movie.

---

## Sample Recommendation

### Input

```text
Avatar
```

### Output

```text
Movies similar to 'Avatar'

Guardians of the Galaxy
John Carter
Star Trek
Aliens
Battle: Los Angeles
```

---

## Future Improvements

- Hybrid Recommendation System
- Collaborative Filtering
- Streamlit Web Application
- Movie Poster Integration using TMDb API
- Personalized Recommendations
- Cloud Deployment

---

## Author

**Sumant Kumar**

---

## License

This project is developed for educational and academic purposes.
