# Import all necessary libraries may need...
import os
import subprocess

# I am looking wether i am owning the current directory or not :P
current_directory = os.getcwd()

# What are these all stuffs in my directory? :D
files = os.listdir(current_directory)

# But i am looking for only .inp files. Honestly :P
inp_files = [file for file in files if file.endswith(".inp")]

# Let see how much muscles power my laptop have to hold the breath.
while True:
    try:
        num_cpus = int(input("Enter the number of CPUs for all jobs (1-4): "))
        if 1 <= num_cpus <= 4:
            break
        else:
            print("Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Start workout bro !
for inp_file in inp_files:
    # Create a .bat file
    bat_file_path = os.path.join(current_directory, f"{inp_file}.bat")

    # Put the weight bars...
    with open(bat_file_path, "w") as bat_file:
        bat_file.write(f"Abaqus J={inp_file} cpus={num_cpus} int")

    print(f".bat file '{inp_file}.bat' created.")

    # Let see what can i do :D
    command = f'cmd /c "{bat_file_path}"'
    subprocess.run(command, shell=True)

    print(f"Job submitted for '{inp_file}'.")

print("Well played! You've just unleashed the magical might! How's it going with that CPU sorcery? :P ")
