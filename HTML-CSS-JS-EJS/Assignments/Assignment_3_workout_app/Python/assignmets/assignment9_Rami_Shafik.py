#Rami Shafik 100971729

######################################## filehandling.py #########################################

def main():

    with open("input_file.txt", "w") as input_file:
        input_file.write("Python is an interpreted, high-level, and general-purpose programming language.\n")

    inputfile = input("Enter input file: ")
    outputfile2 = input("Enter output file: ")

    try:
        inp_file = open(inputfile, "r")
        input_content = inp_file.read()
        print("\nContents of input file:")
        print(input_content)
        inp_file.close()
    except FileNotFoundError:
        print(f"The file {inputfile} does not exist.")
        return

    try:
        out_file = open(outputfile2, "r")
        out_file.close()
    except FileNotFoundError:
        print(f"The file {outputfile2} does not exist.")

    inp_file = open(inputfile, "r")
    out_file = open(outputfile2, "w")
    input_content = inp_file.readlines()
    line_count = len(input_content)
    character_count = sum(len(line) for line in input_content)

    for line in input_content:
        out_file.write(line)

    inp_file.close()
    out_file.close()

    print(f"\nNumber of lines copied: {line_count}")
    print(f"Number of characters copied: {character_count}")

    out_file = open(outputfile2, "a")
    out_file.write("It was created by Guido van Rossum and first released in 1991.\n")
    out_file.close()

    out_file = open(outputfile2, "r")
    updated_content = out_file.readlines()
    updated_line_count = len(updated_content)
    updated_character_count = sum(len(line) for line in updated_content)

    print(f"\nUpdated number of lines in output file: {updated_line_count}")
    print(f"Updated number of characters in output file: {updated_character_count}")
    print("\nContents of output file:")
    print("".join(updated_content))

main()