def electron_distribution(total_electrons):
    shells = []
    shell_number = 1

    while total_electrons > 0:
        max_electrons_in_shell = 2 * shell_number ** 2
        if total_electrons >= max_electrons_in_shell:
            shells.append(max_electrons_in_shell)
            total_electrons -= max_electrons_in_shell
        else:
            shells.append(total_electrons)
            total_electrons = 0
        shell_number += 1

    return shells

if __name__ == "__main__":
    electrons = int(input())
    result = electron_distribution(electrons)
    print(result)
