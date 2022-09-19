let temp = 0
input.onButtonPressed(Button.A, function () {
    basic.showNumber(temp)
})
basic.forever(function () {
    temp = input.temperature()
    basic.showNumber(temp)
    if (temp == 10) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            # . # . #
            `)
    }
    if (temp == 20) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
    }
    if (temp == 30) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # # # # #
            . # # # .
            `)
    }
    if (temp == 40) {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            . # # # .
            # . . . #
            `)
    }
})
