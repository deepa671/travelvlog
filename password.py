import zipfile
import getpass

def create_password_protected_zip(input_file, output_file, password):
    with zipfile.ZipFile(output_file, 'w') as zip_file:
        zip_file.setpassword(password.encode('utf-8'))
        zip_file.write(input_file)

def main():
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output ZIP file name: ")
    password = getpass.getpass("Enter the password: ")
    create_password_protected_zip(input_file, output_file, password)
    print("Password-protected ZIP file created successfully!")

if __name__ == "__main__":
    main()