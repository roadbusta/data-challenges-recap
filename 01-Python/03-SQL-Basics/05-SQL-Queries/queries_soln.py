# pylint: disable=C0103, missing-docstring

def detailed_movies(db):
    '''return the list of movies with their genres and director name'''
    # $CHALLENGIFY_BEGIN
    query = """
        SELECT
            movies.title,
            movies.genres,
            directors.name
        FROM movies
        JOIN directors ON movies.director_id = directors.id
    """
    db.execute(query)
    movies = db.fetchall()
    return movies
    # $CHALLENGIFY_END


def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    # $CHALLENGIFY_BEGIN
    query = """
        SELECT movies.title
        FROM directors
        JOIN movies ON directors.id = movies.director_id
        WHERE (movies.start_year - directors.death_year) > 0
        ORDER BY movies.title
    """
    db.execute(query)
    movies = db.fetchall()
    return [movie[0] for movie in movies]
    # $CHALLENGIFY_END


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    # $CHALLENGIFY_BEGIN
    query = """
        SELECT
            genres,
            COUNT(*),
            ROUND(AVG(minutes), 2)
        FROM movies
        WHERE genres = ?
    """
    db.execute(query, (genre_name,))
    stat = db.fetchone()
    print(stat)
    return {
        "genre": stat[0],
        "number_of_movies": stat[1],
        "avg_length": stat[2]
    }
    # $CHALLENGIFY_END


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    # $CHALLENGIFY_BEGIN
    query = """
        SELECT
            directors.name,
            COUNT(*) movie_count
        FROM movies
        JOIN directors ON movies.director_id = directors.id
        WHERE movies.genres = ?
        GROUP BY directors.name
        ORDER BY movie_count DESC, directors.name
        LIMIT 5
    """
    db.execute(query, (genre_name,))
    directors = db.fetchall()
    return directors
    # $CHALLENGIFY_END


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    # $CHALLENGIFY_BEGIN
    query = """
        SELECT
            (minutes / 30 + 1)*30 time_range,
            COUNT(*)
        FROM movies
        WHERE minutes IS NOT NULL
        GROUP BY time_range
    """
    return db.execute(query).fetchall()
    # $CHALLENGIFY_END


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    # $CHALLENGIFY_BEGIN
    query = """
        SELECT
            directors.name,
            movies.start_year - directors.birth_year age
        FROM directors
        JOIN movies ON directors.id = movies.director_id
        GROUP BY directors.name
        HAVING age IS NOT NULL
        ORDER BY age
        LIMIT 5
    """
    db.execute(query)
    directors = db.fetchall()
    return directors
    # $CHALLENGIFY_END
