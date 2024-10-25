from BitstringGenerator import *

def main():
    bitstrings = []
    while True:
        print("\nMain Menu:")
        print("1. Generate bitstring")
        print("2. Filter bitstring")
        print("3. Exit program")

        choice = input("Choose an option: ")

        if choice == "1":
            # Generate bitstring
            try:
                length = int(input("Enter the length of Bitstring: "))
                if length < 1:
                    print("Length should be a positive integer.")
                    continue
                bitstrings = generate_bitstrings(length)
                display_bitstrings(bitstrings, length)
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

        elif choice == "2":
            if not bitstrings:
                print("No bitstrings generated yet. Please generate bitstrings first.")
                continue

            while True:
                print("\nFilter Menu:")
                print("1. Filter by start")
                print("2. Filter by end")
                print("3. Filter by subset")
                print("4. Back to main menu")

                filter_choice = input("Choose an option: ")

                if filter_choice == "1":
                    # Filter by start
                    prefix = input("Enter the prefix to filter out: ")
                    bitstrings = filter_start_bitstrings(bitstrings, prefix)
                    display_bitstrings(bitstrings, length)

                elif filter_choice == "2":
                    # Filter by end
                    suffix = input("Enter the suffix to filter out: ")
                    bitstrings = filter_end_bitstrings(bitstrings, suffix)
                    display_bitstrings(bitstrings, length)

                elif filter_choice == "3":
                    # Filter by subset
                    subset = input("Enter the subset to filter out: ")
                    bitstrings = filter_subsets(bitstrings, subset)
                    display_bitstrings(bitstrings, length)

                elif filter_choice == "4":
                    # Back to main menu
                    break

                else:
                    print("Invalid choice. Please select from the options.")

        elif choice == "3":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please select from the options.")

if __name__ == "__main__":
    main()
