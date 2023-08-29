

    @staticmethod
    def create_window():
        return QMainWindow()
    @staticmethod
    def owner_signup():
        return

    @staticmethod
    def owner_signin():
        return

    @staticmethod
    def self_info_manage():
        return

    @staticmethod
    def post_message():
        return

    @staticmethod
    def admin_info_manage():
        return

    @staticmethod
    def property_fee_manage():
        return

    @staticmethod
    def message_manage():
        return

    @staticmethod
    def create_signup():
        if globals.ui_lists['signup'] is None:
            globals.ui_lists['signup'] = ui = signupUI.Ui_MainWindow()
        else:
            ui = manager.ui_lists['signup']
        if manager.window_lists['signup'] is None:
            manager.window_lists['signup'] = window = manager.create_window()
        else:
            window = manager.window_lists['signup']
        ui.setupUi(window)
        ui.cancel.clicked.connect(window.close)
        ui.submit.clicked.connect(manager.submit)
        return window


    @staticmethod
    def create_app():
        if manager.app is None:
            manager.app = QApplication(sys.argv)
        return manager.app


    @staticmethod
    def display_window(window):
        window.show()

    @staticmethod
    def wait_app_end():
        if manager.app is None:
            return
        sys.exit(manager.app.exec())


    @staticmethod
    def get_signup_date():
        ui = manager.ui_lists['signup']

        datas = dict()
        datas['house_id'] = ui.house_id.text()
        datas['name'] = ui.name.text()
        datas['password'] = ui.password.text()

        # In yyyy-mm-dd
        date = ui.start_date.date()
        datas['start_time'] = "{}-{}-{}".format(str(date.year()), str(date.month()), str(date.day()))

        datas['gender'] = ui.gender.currentText()
        datas['profession'] = ui.profession.currentText()
        datas['area'] = ui.area.text()
        datas['population'] = ui.population.value()
        datas['phone'] = ui.phone.text()

        print(datas)
        return datas

    # return -1 if data not formatted
    @staticmethod
    def parse_signup_data(datas):
        try:
            data = datas['house_id']
            for ch in data:
                if ch < '0' or ch > '9':
                    raise ValueError()

            data = datas['phone']
            for ch in data:
                if ch < '0' or ch > '9':
                    raise ValueError()

            data = float(datas['area'])
            datas['area'] = data

            if len(datas['house_id']) == 0 or len(datas['password']) == 0 \
                    or len(datas['name']) == 0:
                raise ValueError()

            return 0

        except ValueError:
            print("Through Value Error")
            main_window = manager.window_lists['signup']
            main_window.error_window = manager.create_window()
            error_ui = error.Ui_Form()
            error_ui.setupUi(main_window.error_window)
            main_window.error_window.show()
            error_ui.ensure.clicked.connect(main_window.error_window.close)
            return -1

    @staticmethod
    def send_signup_data(datas):
        return
    @staticmethod
    def submit():
        datas = manager.get_signup_date()
        flag = manager.parse_signup_data(datas)
        if flag == -1:
            return
        manager.send_signup_data(datas)
