def electron_distribution(number_of_electrons):
    shell = 0
    list_of_shells = []
    while number_of_electrons > 0:
        shell += 1
        # Defining the maximum electrons in a shell by given formula:
        e_in_shell = 2 * shell ** 2
        # Adding the electrons (if enough) to the shells:
        if e_in_shell <= number_of_electrons:
            list_of_shells.append(e_in_shell)
        # adding the left electrons in the last shell:
        else:
            list_of_shells.append(number_of_electrons)
        number_of_electrons -= e_in_shell
    return list_of_shells


electrons = int(input())
print(electron_distribution(electrons))
