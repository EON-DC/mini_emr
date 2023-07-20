from Back.db_connector import DBConnector
from Back.server import EMRServer

if __name__ == '__main__':
    db_conn = DBConnector(test_option=True)
    db_conn.create_tables()
    from data.insert_data_to_tables import *

    insert_KTAS_data(db_conn)
    insert_dummy_employee_data(db_conn, 30)
    insert_dummy_chat_room(db_conn, 30)
    insert_dummy_employee_chat_room_data(db_conn, 100, (1, 30), (1, 30))
    server = EMRServer(db_conn)
    server.start()