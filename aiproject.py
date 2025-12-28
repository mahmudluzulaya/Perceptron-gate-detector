def neuron_output(inputs, weights, threshold):
    net_input = sum(x * w for x, w in zip(inputs, weights))
    output = 1 if net_input >= threshold else 0
    return net_input, output


def detect_gate(outputs):
    """
    outputs: [o00, o01, o10, o11]
    order: (0,0), (0,1), (1,0), (1,1)
    """

    patterns = {
        "AND":   [0, 0, 0, 1],
        "OR":    [0, 1, 1, 1],
        "NAND":  [1, 1, 1, 0],
        "NOR":   [1, 0, 0, 0],
        "XOR":   [0, 1, 1, 0],
        "XNOR":  [1, 0, 0, 1],
    }

    for gate_name, pattern in patterns.items():
        if outputs == pattern:
            return gate_name
    return None  # none of the standard gates


def main():
    print("=== Perceptron Gate Detector ===")
    print("You will enter w1, w2 and threshold.")
    print("Program will compute the truth table and try to guess the gate.\n")

    # Get weights and threshold from user
    w1 = float(input("w1 = "))
    w2 = float(input("w2 = "))
    threshold = float(input("threshold = "))

    weights = [w1, w2]

    print("\n=== Truth Table ===")
    print("x1  x2  |  w1   w2  | threshold | net_input | output")
    print("----------------------------------------------------")

    # outputs in order: (0,0), (0,1), (1,0), (1,1)
    outputs = []

    for x1 in [0, 1]:
        for x2 in [0, 1]:
            net_input, out = neuron_output([x1, x2], weights, threshold)
            outputs.append(out)
            print(f"{x1:2}  {x2:2}  | {w1:4} {w2:4} | {threshold:9} | {net_input:9.2f} | {out:6}")

    gate_name = detect_gate(outputs)

    print("\n=== Result ===")
    print(f"Outputs pattern (00,01,10,11) = {outputs}")

    if gate_name:
        print(f"This perceptron behaves like: {gate_name} gate")
    else:
        print("This does NOT match AND/OR/NAND/NOR/XOR/XNOR exactly (custom perceptron).")


if __name__ == "__main__":
    main()

