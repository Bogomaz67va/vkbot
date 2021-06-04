from vk_api.keyboard import VkKeyboard, VkKeyboardColor

COLOR_PRIMARY = VkKeyboardColor.PRIMARY
COLOR_NEGATIVE = VkKeyboardColor.NEGATIVE
COLOR_POSITIVE = VkKeyboardColor.POSITIVE


def button_bot(text: str, text_2=None, text_3=None):
    if text_2 is None:
        button = VkKeyboard(one_time=False, inline=True)
        button.add_button(text, COLOR_PRIMARY)
        return button.get_keyboard()
    elif text_2 and text_3 is None:
        button = VkKeyboard(one_time=False, inline=True)
        button.add_button(text, COLOR_PRIMARY)
        button.add_line()
        button.add_button(text_2, COLOR_NEGATIVE)
        return button.get_keyboard()
    else:
        button = VkKeyboard(one_time=False, inline=True)
        button.add_button(text, COLOR_PRIMARY)
        button.add_line()
        button.add_button(text_2, COLOR_POSITIVE)
        button.add_line()
        button.add_button(text_3, COLOR_NEGATIVE)
        return button.get_keyboard()


def button_bot_age(text_1: str, text_2: str, text_3: str, text_4: str, text_5: str):
    button = VkKeyboard(one_time=False, inline=True)
    button.add_button(text_1, COLOR_PRIMARY)
    button.add_button(text_2, COLOR_POSITIVE)
    button.add_line()
    button.add_button(text_3, COLOR_NEGATIVE)
    button.add_button(text_4, COLOR_PRIMARY)
    button.add_line()
    button.add_button(text_5, COLOR_POSITIVE)
    return button.get_keyboard()


def button_bot_status(text_1: str, text_2: str, text_3: str, text_4: str):
    button = VkKeyboard(one_time=False, inline=True)
    button.add_button(text_1, COLOR_PRIMARY)
    button.add_line()
    button.add_button(text_2, COLOR_NEGATIVE)
    button.add_line()
    button.add_button(text_3, COLOR_POSITIVE)
    button.add_line()
    button.add_button(text_4, COLOR_PRIMARY)
    return button.get_keyboard()
