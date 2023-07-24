import psycopg2
from psycopg2 import IntegrityError


class PostgresPipeline:
    def __init__(self):
        # Connection Details
        hostname = "db"
        username = "news"
        password = "news"  # your password
        database = "news_db"

        # Create/Connect to database
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database
        )

        # Create cursor, used to execute commands
        self.cur = self.connection.cursor()

        self.ids_seen = set()

        self.cur.execute("SELECT url FROM news")

        # Fetch all existing urls
        self.ids_seen = set([row[0] for row in self.cur.fetchall()])

        # Create quotes table if none exists
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS news (
                parent_url VARCHAR(255),
                url VARCHAR(255) PRIMARY KEY,
                title VARCHAR(255),
                subtitle VARCHAR(255),
                author VARCHAR(255),
                date VARCHAR(255),
                text TEXT
            )
            """
        )

    def process_item(self, item, spider):

        # Check if item has already been scraped
        if item["url"] in self.ids_seen:
            return item

        # Define insert statement
        try:
            self.cur.execute(
                """
                INSERT INTO news (parent_url, url, title, subtitle, author, date, text)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING
                """,
                (
                    item["parent_url"],
                    item["url"],
                    item["title"],
                    item["subtitle"],
                    item["author"],
                    item["date"],
                    item["text"],
                ),
            )
            # Execute insert of data into database
            self.connection.commit()
        except IntegrityError:
            # Ignore duplicate entry, rollback the transaction
            self.connection.rollback()
        except Exception as e:
            self.connection.rollback()  # Rollback the transaction
            raise e

        return item

    def close_spider(self, spider):
        # Close cursor & connection to database
        self.cur.close()
        self.connection.close()
