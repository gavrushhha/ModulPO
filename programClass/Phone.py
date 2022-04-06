class Phone:
    @staticmethod
    def country(phone):
        return phone[1:-14]

    @staticmethod
    def check_Format(phone):
        Flag_1, Flag_2, Flag_3 = False
        if phone[0] == "+":
            Flag_1 = True
        if phone[-3] == "-" and phone[-6] == "-":
            Flag_2 = True
        if phone[-10] == ")" and phone[-14] == "(":
            Flaf_3 = True