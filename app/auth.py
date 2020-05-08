import pyrebase

# config = {
#     "apiKey": "AIzaSyCb9f7q_RbSezg5AhoHvy-BrLncvvoF5OY",
#     "authDomain": "shotur-794d7.firebaseapp.com",
#     "databaseURL": "https://shotur-794d7.firebaseio.com",
#     "projectId": "shotur-794d7",
#     "storageBucket": "shotur-794d7.appspot.com",
#     "messagingSenderId": "1017082040042",
#     "appId": "1:1017082040042:web:ed12f08bc36cdb97ae5193",
#     "measurementId": "G-RVKJD6GDRG"

# }

# firebase = pyrebase.initialize_app(config)

# auth = firebase.auth()


# email = input("Enter you email")
# password = input("Enter your password")

# user = auth.sign_in_with_email_and_password(email, password)
# user = auth.create_user_with_email_and_password(email, password)
def authenicate(email, password):
    try:
        config = {
            "apiKey": "AIzaSyCb9f7q_RbSezg5AhoHvy-BrLncvvoF5OY",
            "authDomain": "shotur-794d7.firebaseapp.com",
            "databaseURL": "https://shotur-794d7.firebaseio.com",
            "projectId": "shotur-794d7",
            "storageBucket": "shotur-794d7.appspot.com",
            "messagingSenderId": "1017082040042",
            "appId": "1:1017082040042:web:ed12f08bc36cdb97ae5193",
            "measurementId": "G-RVKJD6GDRG"

        }

        firebase = pyrebase.initialize_app(config)

        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email, password)
        return 1
    except:
        return 0


# print(authenicate(email, password))
# print(auth.get_account_info(user['idToken']))