from flask import Flask, request
import requests
from flask_mysqldb import MySQL
from twilio.twiml.messaging_response import MessagingResponse
from database import Database

app = Flask(__name__)
app.secret_key = "my_secret_key"
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'electiondb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def home():
    return "Chat bot - Hello folks"


@app.route('/bot', methods=['POST'])
def bot():
    new_message = request.values.get('Body', '').lower()
    from_number = request.values.get('From')
    to = request.values.get('To')
    print(from_number[13:], to[9:])
    resp = MessagingResponse()
    my_message = resp.message()

    responded = False
    if new_message != '':
        print((new_message, from_number[13:]))
        try:
            dict = Database(mysql).check_user(new_message, from_number[13:])
            message = '\t*Congratulation*' \
                      '\n Student ID: ' + new_message + \
                      '\n Full Name: ' + dict.get('fullname') + \
                      '\n *Token*: ' + dict.get('token') + \
                      '\nAlternate link1: https://97045c77e4b4.ngrok.io' \
                      '\nAlternate link2: https://079a9818031f.ngrok.io' \
                      '\n Type /help if you need help'
            my_message.body(message)
            responded = True
        except:
            print("error")

    if 'cat' in new_message:
        my_message.media('https://cataas.com/cat')
        responded = True
    if 'help' in new_message:
        message = '\t*Welcome to NFS Help Page*' \
                  '\n Type your student ID (eg. 10234588) for *TOKEN*' \
                  '\nContact us: 0240187877/ 0572751631' \
                  '\n/results - for election results' \
                  '\n/status - for your vote status'
        my_message.body(message)
        responded = True
    if 'result' in new_message:
        dict = Database(mysql).get_result()
        message = '\t*NFSS ELECTION RESULTS*' \
                  '\n\n PRESIDENT: ' + "__Dora Owusua Ofori (Appointed)__" + \
                  '\n\n VICE PRESIDENT: ' + "__Nana Ama Serwaa (56.1%)__" + \
                  '\n\n G. SECRETARY: ' + "__Sharon Naa Atswei Mensah (50.41%)__" + \
                  '\n\n ORGANISER ' + "__Isaac Etornam Akakpo (52.03%)__" + \
                  '\n\n TREASURER ' + "__Solomon Aboagye (86.99%)__" + \
                  '\n\n\n\n Developer: Samjay (0547785025)'
        my_message.body(message)
        responded = True

    if not responded:
        # my_message.body('no data')
        print('Invalid message')
    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
