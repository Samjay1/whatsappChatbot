class Database:
    def __init__(self, mysql):
        self.mysql = mysql
        self.db = self.mysql.connection
        self.cursor = self.db.cursor()

    def check_user(self, student_id, phone):
        query = "SELECT * FROM goggle_form"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        # print(data)
        for user in data:
            if student_id == str(user.get('student_id')) and phone == str(user.get('phone')):
                token = self.get_token(student_id)
                return token

        print('user Unsuccessful..:', student_id)
        return False

    def get_token(self, student_id):
        query = "SELECT * FROM users_tb"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        print(data)
        for user in data:
            if student_id == str(user.get('student_id')):
                print(student_id, 'token', user.get('token'))
                dict = {'token': str(user.get('token')), 'fullname': str(user.get('full_name'))}
                return dict

        print('token Unsuccessful...:', student_id)
        return False


    def get_result(self):
        stephen = 0
        serwaa = 0
        naa = 0
        maygail = 0
        isaac = 0
        keziah = 0
        solomon = 0
        total = 0
        self.cursor.execute('SELECT * FROM users_tb')
        results = self.cursor.fetchall()
        for result in results:
            if result.get('status') == 1:
                total += 1

            if result.get('vice') == 'Stephen Obiri-Yeboah':
                stephen += 1
            elif result.get('vice') == 'Nana Ama Serwaa Osei':
                serwaa += 1

            if result.get('general') == 'Sharon Naa Atswei Mensah':
                naa += 1
            elif result.get('general') == 'Maygail Boatemaa Darteh':
                maygail += 1

            if result.get('organiser') == 'Isaac Etornam Akapko':
                isaac += 1
            elif result.get('organiser') == 'Keziah Naa Ode Mensah Ofori':
                keziah += 1

            if result.get('treasurer') == 'Solomon Aboagye':
                solomon += 1
        dict = {'total': total, 'stephen': stephen, 'serwaa': serwaa, 'naa': naa, 'maygail': maygail, 'isaac': isaac, 'keziah': keziah, 'solomon': solomon}

        return dict