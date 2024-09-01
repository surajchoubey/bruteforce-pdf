import sys
import itertools
from PyPDF2 import PdfReader

def try_password(pdf_path, pan_last4):
    alphanumeric_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for emp_id in itertools.product(alphanumeric_chars, repeat=4):
        emp_id_str = ''.join(emp_id)
        # Try both lowercase and uppercase for the last 'd' character
        for last_char in ['d', 'D']:
            password = f"{emp_id_str}{pan_last4[:-1]}{last_char}"
            print(password)
            try:
                with open(pdf_path, 'rb') as file:
                    reader = PdfReader(file)
                    # Try to decrypt the PDF
                    print(f"Trying password: {password}")
                    if reader.decrypt(password):
                        print(f"Password found: {password}")
                        return password
            except Exception as e:
                print(f"Error with password {password}: {str(e)}")
    print("Password not found in the given range.")
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    pan_last4 = "468"  # Last 3 digits of your PAN without the final 'd' character

    try_password(pdf_path, pan_last4)
