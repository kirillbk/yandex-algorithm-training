# C. Надпись на табло

# удалить повторяющиеся строки и пустые строки сверху/снизу
def compress(screen: list[str]) -> list[str]:
    new_screen = [screen[0]]

    for i in range(1, len(screen)):
        if screen[i] != new_screen[-1]:
            new_screen.append(screen[i])
    if len(new_screen) > 1 and new_screen[0].count(".") == len(new_screen[0]):
        new_screen.pop(0)
    if len(new_screen) > 1 and new_screen[-1].count(".") == len(new_screen[-1]):
        new_screen.pop()

    return new_screen


n = int(input())
screen = [input() for _ in range(n)]

screen = compress(screen)
# повернуть против часовой стрелки
screen = ["".join(l) for l in zip(*screen)]
screen = compress(screen)
# повернуть по часовой стрелке
screen = ["".join(l) for l in zip(*screen)]

if screen == ["#"]:
    print("I")
elif screen == ["###", "#.#", "###"]:
    print("O")
elif screen == ["##", "#.", "##"]:
    print("C")
elif screen == ["#.", "##"]:
    print("L")
elif screen == ["#.#", "###", "#.#"]:
    print("H")
elif screen == ["###", "#.#", "###", "#.."]:
    print("P")
else:
    print("X")
