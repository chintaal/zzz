print("="*50)
print("Hill Climbing Optimization")
print("="*50)
print("\nExamples of functions to try:")
print("  1. -(x**2) + 4*x        [Parabola with max at x=2]")
print("  2. -abs(x-5)            [Peak at x=5]")
print("  3. -(x-3)**2 + 10       [Max at x=3]")

def hill_climbing(func, start, step=0.01, iterations=1000):
    current = start
    current_val = func(current)
    steps_taken = 0
    
    print(f"\n→ Starting hill climbing from x={start:.4f}")
    print(f"  Initial value: f({start:.4f}) = {current_val:.4f}")

    for i in range(iterations):
        up = current + step
        down = current - step

        if func(up) > current_val:
            current = up
            current_val = func(up)
            steps_taken += 1
        elif func(down) > current_val:
            current = down
            current_val = func(down)
            steps_taken += 1
        else:
            print(f"✓ Converged after {steps_taken} steps (iteration {i+1})")
            break
        
        if (i+1) % 200 == 0:
            print(f"  Step {i+1}: x={current:.4f}, f(x)={current_val:.4f}")

    return current, current_val

function_str = input("\nEnter function of x: ")
function = lambda x: eval(function_str)

start = float(input("Enter starting value: "))
step = float(input("Enter step size (default 0.01): ") or 0.01)

x_opt, val = hill_climbing(function, start, step)

print(f"\n📊 Results:")
print(f"  Optimal x: {x_opt:.6f}")
print(f"  Maximum value: {val:.6f}")
