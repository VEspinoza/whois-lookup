import socket

def whois(domain: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.iana.org", 43))
    s.send(f"{domain}\r\n".encode())
    response = s.recv(4096).decode()
    s.close()
    return response

def main():
    url_choice = input("Who is lookup! Press 1 to input domain or press 2 to enter file name: ")
    if url_choice == "1":
        url = input("Please enter a URL: ").strip()
        print(whois(url))

    elif url_choice == "2":
        fname = input("Please enter file name: ")
        try:
            fhand = open(fname)
        except:
            print("Could not open file ", fname)
            exit()

        fout = open('whois_output.txt', 'a')
        for domain in fhand:
            fout.write(whois(domain.strip()))
            fout.write("_________________________________________\n")

        fout.close()
        print("Whois_output file created.")

    else:
        print("Invalid entry, please try again.")
        main()


if __name__ == "__main__":
    main()
