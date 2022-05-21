import time
import turtle
cnt = 0


def hilbert(level, angle, step):
    global cnt
    cnt += 1

    # Input Parameters are numeric
    # Return Value: None
    if level == 0:
        return

    turtle.right(angle)
    hilbert(level - 1, -angle, step)

    turtle.forward(step)
    turtle.left(angle)
    hilbert(level - 1, angle, step)

    turtle.forward(step)
    hilbert(level - 1, angle, step)

    turtle.left(angle)
    turtle.forward(step)
    hilbert(level - 1, -angle, step)
    turtle.right(angle)



def main():
    turtle.tracer(0, None)
    level = int(input())
    size = 200
    turtle.penup()
    turtle.goto(-size / 2.0, size / 2.0)
    turtle.pendown()
    turtle.update()

    # For positioning turtle
    prev_t = time.time()
    hilbert(level, 90, size / (2 ** level - 1))
    cur_t = time.time() - prev_t
    print(f"Глубина рекурсии: {cnt}\n{cur_t}")
    turtle.done()


if __name__ == '__main__':
    main()
