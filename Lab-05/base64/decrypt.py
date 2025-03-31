import base64
def main():
    try:
        with open("data.txt", "r") as file:
            encoded_String = file.read().strip()
            
            decoded_bytes=base64.b64decode(encoded_String)
            decoded_String=decoded_bytes.decode("utf-8")
            
            print("Chuoi sau khi giai ma:", decoded_String)
    except Exception as e:
        print("Loi:", e)
        
if __name__ == "__main__":
    main()