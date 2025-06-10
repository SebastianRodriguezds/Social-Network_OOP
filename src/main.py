from social_network import SocialNetwork

def main():
    sn = SocialNetwork()

    while True:
        filename = input("Insert the name of the file (or 'n' to exit): ")
        if filename.lower() == 'n':
            print("Exiting the programme.")
            return
        
        try:
            sn.load_from_file(f"data/{filename}")
            break
        except Exception as e:
            print(f"Error: {e}")
        
    choice = input("Would you like to display the loaded social network (y/n): ").lower()
    if choice == 'y':
        print("\nRed socila:")
        sn.display_network()

if __name__ == "__main__":
    main()

