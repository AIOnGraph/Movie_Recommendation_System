# Movie Recommendation System using IMDb Dataset

This repository contains code for a movie recommendation system built using the IMDb dataset. The recommendation system utilizes Count Vectorization and Cosine Similarity to suggest movies based on directors, movie titles, cast, and genres.

## Tools Used
- Python
- scikit-learn
- Streamlit

## Dataset
The dataset used in this project is the IMDb dataset, which contains information about movies, including details such as movie titles, directors, cast, genres, ratings, and more. The dataset is publicly available and can be obtained from the IMDb website or other sources.

## Files
- `main.py`: This file contains the code for the Streamlit web application, where users can input a movie,director,Actors,Genre and receive recommendations.
- `requirements.txt`: This file lists all the Python dependencies required to run the application.
- `movie_list1.joblib`: Joblib file containing preprocessed movie data.
- `similarity1.joblib`: Joblib file containing cosine similarity scores.

## Setup and Installation
1. Clone the repository to your local machine. 
2. Install the required Python dependencies by running `pip install -r requirements.txt`.
3. Run the Streamlit application using the command `streamlit run main.py`.
4. Access the application in your web browser.

## Usage
1. Type a movie name.
2. Click on the "Show Recommendations" button to view recommended movies based on the selected movie.

## Contributing
Contributions to this project are welcome! Feel free to open an issue or submit a pull request with any improvements or suggestions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
