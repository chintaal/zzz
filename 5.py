def hill_climbing(func, start, step=0.01, iterations=1000):
    current = start
    current_val = func(current)

    for _ in range(iterations):
        up = current + step
        down = current - step

        if func(up) > current_val:
            current = up
            current_val = func(up)
        elif func(down) > current_val:
            current = down
            current_val = func(down)
        else:
            break

    return current, current_val

function_str = input("Enter function of x: ")
function = lambda x: eval(function_str)

start = float(input("Enter starting value: "))
x_opt, val = hill_climbing(function, start)

print("Optimal x:", x_opt)
print("Maximum value:", val)
