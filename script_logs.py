import re

def check_pass_status(file_path, phrases):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        num_lines = len(lines)
        found_phrases = {}

        for i in range(num_lines - 15):
            log_lines = lines[i:i+16]
            for phrase in phrases:
                for j, line in enumerate(log_lines):
                    if re.search(re.escape(phrase), line):
                        found_phrases[phrase] = i + j + 1  # Adjust line number relative to the full file

        if set(found_phrases.keys()) == set(phrases):
            print("Passed")
            print("\nLine numbers where phrases were found:")
            for phrase, line_number in found_phrases.items():
                print(f"- {phrase}: Line {line_number}")
            return

        print("Not Passed")
    except FileNotFoundError:
        print(f"{file_path} file not found.")

# Prompt user for file path and phrases
file_path = input("Enter the file path you want to check: ")

phrases = ["kali-raspberry-pi-zero-2-w sshd[660]: Server listening on :: port 22.",
           "Accepted password for dougl from 10.42.0.71 port 45991 ssh2",
           "pam_unix(sshd:session): session opened for user dougl(uid=1000) by dougl(uid=0)"]


check_pass_status(file_path, phrases)