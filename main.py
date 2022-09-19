temp = 0

def on_button_pressed_a():
    basic.show_number(temp)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    global temp
    temp = input.temperature()
    basic.show_number(temp)
    if temp == 10:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # . # .
                        # . # . #
        """)
    if temp == 20:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
        """)
    if temp == 30:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        # # # # #
                        . # # # .
        """)
    if temp == 40:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # # # .
                        # . . . #
        """)
basic.forever(on_forever)
