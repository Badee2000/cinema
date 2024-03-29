### How to start the project:

1. - `poetry init`. (optional)
   - `poetry shell`.
   - `poetry install --no-root`.

- Make sure postgreSQL is running.

2. - run `psql -h localhost -U postgres` in the _cmd_ to start the database.
   - `CREATE USER admin WITH PASSWORD '1234qwer1234';` (I used `.env` file but to make it easier and ready to launch faster without creating the file _for testing only_).
   - `CREATE DATABASE cinema OWNER admin ENCODING 'UTF8';`

- migrate to database. (`py manage.py makemigrations` then `py manage.py migrate`).
- Start the project with `py manage.py runserver`.

To start the async task:
Type in seperate terminals (after typing poetry shell to make sure everything is in the venv) these commands:
1- `redis-server`
2- `celery -A cinema beat -l info`
3- `celery -A cinema worker -l info -P gevent`

Posting movies using the request.http (You need to download the REST Client extension from vscode or any related extension).

### Answers:

1. **Desing and implement:**
   1.1 **Content-Based Filtering Recommendation Algorithms:**

   - This algorithms is used for recommending items to a user based on user's preferences. Which means it recommends items similar to what the user has liked in the past depending on item's features.
   - For example: In our database we extract the movie features that we rate from movie metadata, and suggests movies that are similar to what we (watcher before for example) or (same protagonists or rank for example).
   - This algorithm builds a profile for the user and keep the user's history to do recommendations.
   - Best algorithm to use from my search is **Cosine similarity** as a best measure.
   - I once used the KNN algorithm for an anime recommendation system.

     1.2 **Collaborative Filtering Recommendation Algorithms:**

   - This algorithm recommends items based on user interactions and similarities between users or items. So It has two types user-based and item-based.
   - **User-based**: compares users based on their historical interactions with items. If two users have rated similar movies highly, it suggests new movies to one user based on the other's preferences.
   - **Item-based** recommends items that are similar to those a user has interacted with in the past. It focuses on the relationships between items themselves, rather than user-item interactions. (That is the difference between it and the content-based one).
   - Designing requires building the following:
     - `User-Item Matrices` which is a matrix.
     - `User-Based` or `Item-Based` Filtering.
   - **Matrix Factorization** is the most recommended algorithm.

     1.3 **What databases:**

   - I would use a relational database because it is well structured and I prefer postgresSQL because:
     - Better query speed & concurrency.
     - Suited for complex querying.
     - ACID Compliance (Atomicity, Consistency, Isolation, Durability) ensures data integrity.
   - After many searches, some engineers prefer using NoSQL databases for its `Flexible Storage` and can handle large amount of data.

2. - **Use indexes**: Create indexes on frequently requested columns to speed up search queries in `Postgres`. Use indexes and constraints to optimize graph traversal in `Neo4j`. Use the indexing capability for match searches in `Qdrant`.

   - **Split data**: Split the data into smaller chunks based on certain criteria such as user ID or time stamp to distribute the load evenly across database nodes This can improve query performance by increasing the amount of data to be processed which will reduce the.

   - **Use caching**: Use caching techniques such as `Redis` to store frequently accessed data to lighten the load on the database server.

   - **Optimize queries**: Make sure all queries are typed properly and use proper indexing to avoid unnecessary scans of the database.

3. **Celery** is a task queue implementation for web applications used to asynchronously execute work outside the HTTP request-response cycle using workers. In celery logic we have message broker which used to exchange messages(requests or responses) between celery and workers, which could be RabbitMQ or Redis (I used redis in the project).

- To ensure reliability and fault tolerance, celery provides several solutions:

      - **Retries**: If a task failed, you can configure Celery to retry the task after a certain period.

      - **Concurrency**: Celery allows you to control the number of concurrent tasks each worker can process.

      - **Result Backends**: To save task results and make sure they are not lost if a worker crashes for example, we configure a result backend. This could be a SQL database or a cache system like Redis.

      - **Acknowledgments and Task Persistence**: If a worker crashes while processing a task, the task will be returned to the queue so another worker can pick it up.
