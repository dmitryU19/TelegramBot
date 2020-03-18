from vedis import Vedis
import config


def get_current_state(user_id):
    with Vedis(config.db_file) as db:
        try:
            return db[user_id].decode()
        except KeyError:
            return config.States.S_START.value


def set_state(user_id, value):
    with Vedis(config.db_file) as db:
        try:
            db[user_id] = value
            return True
        except:
            return False


def save_user_answer(user_id, step_id, value):
    with Vedis(config.db_file) as db:
        try:
            db['{0}_{1}'.format(user_id, step_id)] = value
            return True
        except:
            return False


def get_user_answer(user_id, step_id):
    with Vedis(config.db_file) as db:
        try:
            return db['{0}_{1}'.format(user_id, step_id)].decode()
        except KeyError:
            return 'no_answer'
