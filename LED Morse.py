import gpiozero
import time

red = gpiozero.LED(17)

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }


def main():
    msg = input('MESSAGE: ')

    for char in msg:
        a = CODE[char.upper()]
        for i in range(0, len(a)):
            if a[i+1] == '.':
                red.on()
                time.sleep(0.15)
                red.off()
                time.sleep(0.2)
            else:
                red.on()
                time.sleep(0.5)
                red.off()
                time.sleep(0.2)

        time.sleep(0.6)


if __name__ == "__main__":
    main()



