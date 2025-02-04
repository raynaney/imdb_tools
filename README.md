# IMDB Tools

A suite of Python scripts for retrieving data from the IMDB homepage.

- `get_directors.py` contains functions for retrieving director names, either
  for an item identified by a given IMDB ID or a list of all directors that
  appear on the IMDB Top 250
- `get_imdb_id.py` contains functions for returning a list of titles and their
  associated IMDB IDs given a search query
- `get_top_250.py` contains a function for retrieving a list of titles on the
  IMDB Top 250
- `ratings_regression.py` contains functions for plotting all ratings for a
  series identified by an IMDB ID together for a linear regression analysis for
  each season
- `get_series_rating.py` contains functions for retrieving all episodes
  including ratings and vote counts for a series identified by a given IMDB ID

The script `show_ratings.sh` acts as a convenience script to perform a search
query and perform a regression analysis on the first result, like so:

    bash show_ratings.sh "true detective"

This will open an interactive plot window showing ratings for all three seasons
of the series *True Detective*, with a regression line for each season as well
as the series overall. Instead of passing a search string, the script also
accepts an IMDB ID directly.

To ensure all necessary dependencies are installed correctly, run the following
`pip` command:

    pip3 install -r requirements.txt
