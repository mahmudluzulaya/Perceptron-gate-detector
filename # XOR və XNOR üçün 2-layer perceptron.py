def perceptron(net_input, threshold):
    return 1 if net_input >= threshold else 0


# ---------------------------------------------------
# 1-layer perceptron logic gates (AND, OR, NAND, NOR)
# ---------------------------------------------------
def single_layer_gate(gate, x1, x2):
    if gate == "AND":
        w1, w2, t = 1, 1, 1.52
    
    elif gate == "OR":
        w1, w2, t = 1, 1, 0.5
    elif gate == "NAND":
        w1, w2, t = -1, -1, -1.5
    elif gate == "NOR":
        w1, w2, t = -1, -1, -0.5
    else:
        return None, None, None, None

    net = x1*w1 + x2*w2
    out = perceptron(net, t)

    return w1, w2, t, (net, out)


def truth_table_single(gate):
    print("\nTruth Table for", gate)
    print("x1 x2 | net_input | out")

    for x1 in [0, 1]:
        for x2 in [0, 1]:
            w1, w2, t, (net, out) = single_layer_gate(gate, x1, x2)
            print(f"{x1}  {x2}  |   {net:.1f}     |  {out}")


# ---------------------------------------------------
# XOR / XNOR 2-layer neural network
# ---------------------------------------------------
def two_layer_xor(x1, x2):

    # Hidden layer
    # Neuron 1 – OR
    h1 = perceptron(x1*1 + x2*1, 0.5)

    # Neuron 2 – NAND
    h2 = perceptron(x1*(-1) + x2*(-1), -1.5)

    # Output layer – AND
    out = perceptron(h1*1 + h2*1, 1.5)

    return h1, h2, out


def two_layer_xnor(x1, x2):
    xor_out = two_layer_xor(x1, x2)[2]
    return 1 - xor_out   # invert XOR output


def truth_table_xor():
    print("\nTruth Table for XOR (2-layer NN)")
    print("x1 x2 | h1 h2 | out")

    for x1 in [0, 1]:
        for x2 in [0, 1]:
            h1, h2, out = two_layer_xor(x1, x2)
            print(f"{x1}  {x2}  | {h1}  {h2} |  {out}")


def truth_table_xnor():
    print("\nTruth Table for XNOR (2-layer NN)")
    print("x1 x2 | out")

    for x1 in [0, 1]:
        for x2 in [0, 1]:
            out = two_layer_xnor(x1, x2)
            print(f"{x1}  {x2}  |  {out}")


# ---------------------------------------------------
# MENU
# ---------------------------------------------------
def main():
    while True:
        print("\n==== LOGIC GATE NEURAL NETWORK ====")
        print("1 – AND")
        print("2 – OR")
        print("3 – NAND")
        print("4 – NOR")
        print("5 – XOR (2-layer)")
        print("6 – XNOR (2-layer)")
        print("0 – Exit")

        choice = input("Choose gate: ")

        if choice == "0":
            break

        elif choice in ["1","2","3","4"]:
            gates = {"1":"AND","2":"OR","3":"NAND","4":"NOR"}
            gate = gates[choice]

            x1 = int(input("x1 (0/1): "))
            x2 = int(input("x2 (0/1): "))

            w1, w2, t, (net, out) = single_layer_gate(gate, x1, x2)

            print(f"\nGate: {gate}")
            print(f"w1={w1}, w2={w2}, threshold={t}")
            print(f"Net input = {net}")
            print(f"Output = {out}")

            truth_table_single(gate)

        elif choice == "5":   # XOR
            x1 = int(input("x1 (0/1): "))
            x2 = int(input("x2 (0/1): "))

            h1, h2, out = two_layer_xor(x1, x2)

            print("\nXOR (2-layer neural network)")
            print(f"Hidden layer: h1={h1}, h2={h2}")
            print(f"Output: {out}")

            truth_table_xor()

        elif choice == "6":   # XNOR
            x1 = int(input("x1 (0/1): "))
            x2 = int(input("x2 (0/1): "))

            out = two_layer_xnor(x1, x2)

            print("\nXNOR (2-layer neural network)")
            print(f"Output: {out}")

            truth_table_xnor()

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
