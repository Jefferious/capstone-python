from model import db, User, Tic, connect_to_db

if __name__ == '__main__':
    from server import app
    connect_to_db(app)

def create_user(email, password):
     user = User(email=email, password=password)

     return user