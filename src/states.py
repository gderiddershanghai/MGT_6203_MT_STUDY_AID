#====================TOKEN===================
class Token():
    def __init__(self, STATE="final"):
        self.STATE = STATE
        self.mpc_questions = None
        self.picture_questions = None
        self.islr_questions = None

    def turn_off(self):
        self.active = False
