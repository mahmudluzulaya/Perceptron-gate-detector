def neuron_output(inputs, weights, threshold):
    net_input = sum(x * w for x, w in zip(inputs, weights))
    output = 1 if net_input >= threshold else 0
    return net_input, output


def print_truth_table(weights, threshold):
    w1, w2 = weights

    print("\n=== Truth Table ===")
    print("x1  x2 |  w1   w2 | threshold | net_input | output")
    print("----------------------------------------------------")

    for x1 in [0, 1]:
        for x2 in [0, 1]:
            net_input, output = neuron_output([x1, x2], weights, threshold)
            print(f"{x1}   {x2} | {w1:4} {w2:4} | {threshold:9} | {net_input:9.1f} | {output:6}")


def main():
    print("=== Neural Network Logic Gate Calculator ===")
    print("Available gates: AND, OR, NAND, NOR, XOR, XNOR")

    gate = input("Choose a gate: ").strip().upper()

    # Auto-assign correct perceptron weights for linearly separable gates
    if gate == "AND":
        weights = [1, 1]
    elif gate == "OR":
        weights = [1, 1]
    elif gate == "NAND":
        weights = [-1, -1]
    elif gate == "NOR":
        weights = [-1, -1]
    elif gate in ("XOR", "XNOR"):
        print("\nXOR və XNOR qapıları tək qatlı perceptronla həyata keçirilə bilmir.")
        print("Bu proqram bir qatlı perceptron üçün nəzərdə tutulub, ona görə XOR/XNOR üçün weight təyin etmir.")
        return
    else:
        print("Invalid gate!")
        return

    print(f"\nSelected Gate: {gate}")
    print(f"Automatically selected weights: {weights}")

    # YOU choose threshold
    threshold = float(input("Enter your threshold value: "))

    # Print full truth table
    print_truth_table(weights, threshold)


if __name__ == "__main__":
    main()