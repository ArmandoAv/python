# Python has its exception handling like other programming languages

"""
    Python has exception handling with the following commands
        try
        exception
    The following command is not necessary, you should only use it 
    when you need the program to do something even with the exception.
    finally
"""

file = "../data/text.txt"

try:
    # Open the file in reading mode
    with open(file, "r") as file:
        # Leemos el contenido del archivo
        contained = file.read()
        
        # Convert file content to a number
        number = int(contained)
        
        # Do an arithmetic operation with the number obtained
        result = number / 2
        
        print("The final result is:", result)

# Exception for file not found
except FileNotFoundError:
    print(f"The file {file} doesn't exist. Could you verify?")

# Exception for contain 
except ValueError:
    print("Cannot convert file content to integer.")

# Manejamos cualquier otra excepción que pueda ocurrir
except Exception as e:
    print("An unexpected error occurred:", e)

# El bloque finally se ejecutará siempre, independientemente de si se producen excepciones o no.
finally:
    print("This part must always be executed")
