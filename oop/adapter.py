"""
    Adapter design pattern
"""
import abc


class MySQL:

    def connect_to_DB(self, uri):
        print('Many steps to connect to DB')

    def run_query(self, query):
        print("my SQL specific query")


class MongoDB:

    def create_connection(self, uri):
        print('Many steps to connect to Mongo DB')

    def query_DB(self, query):
        print("Mongo specific query")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class DBAdapter(abc.ABC):

    @abc.abstractmethod
    def connnect(self, path, username, password):
        pass

    @abc.abstractmethod
    def query(self, text):
        """
        Provide the name of the object you need
        rerun the results as a list
        """
        pass

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class MySQLAdapter(DBAdapter):

    def __init__(self):
        # Composite = this class owns a class instance
        self.database = MySQL()

    def connnect(self, path, username, password):
        print("Connecting to mysql")
        uri = "{}:/{}/{}".format(path, username, password)
        self.database.connect_to_DB(uri)

    def query(self, text):
        print("Running my sql query")
        self.database.run_query(text)


class MongoAdapter(DBAdapter):

    def __init__(self):
        # Composite = this class owns a class instance
        self.database = MongoDB()

    def connnect(self, path, username, password):
        print("Connecting to MongDB")
        uri = "{}:/{}_::{}".format(path, username, password)
        self.database.create_connection(uri)

    def query(self, text):
        print("Running my MongoDB query")
        self.database.query_DB(text)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

db = MySQLAdapter()
db = MongoAdapter()

db.connnect('some/path', 'user', '***')
db.query('AMBER')









