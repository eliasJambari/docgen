from gui import my_constants as cst


# Change state of validation (fields : user, password + buttons : save, validate)
def set_validation_state(ui_preferences, state):

    if state == cst.NOT_VALIDATED:
        template_valid(ui_preferences, True, True, False, True, "Please validate login information before saving", "red")
    elif state == cst.VALIDATING:
        template_valid(ui_preferences, False, False, False, False, "Validating login information...", "yellow")
    elif state == cst.VALIDATED:
        template_valid(ui_preferences, False, False, True, False, "Login information validated", "green")
    elif state == cst.INCORRECT_LOGIN:
        template_valid(ui_preferences, True, True, False, True, "Incorrect login information. Please try again", "red")


def template_valid(ui_preferences, user, password, save, validate, label, color):
    ui_preferences.add_txt.setEnabled(user)
    ui_preferences.pass_txt.setEnabled(password)
    ui_preferences.save_btn.setEnabled(save)
    ui_preferences.validate_btn.setEnabled(validate)
    ui_preferences.valid_lbl.setText(label)
    ui_preferences.valid_lbl.setStyleSheet("color: " + color)