def read_and_modify_file():
    # Ask the user for the input filename
    input_filename = input("my book: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Define the output filename
        output_filename = "modified_" + input_filename

        # Write the modified content to a new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"❌ Error: Unable to read the file '{input_filename}'.")

# Run the function
read_and_modify_file()
