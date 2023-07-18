from Back.db_connector import DBConnector
from Back.server import EMRServer

if __name__ == '__main__':
    db_conn = DBConnector(test_option=True)
    server = EMRServer(db_conn)
    server.start()