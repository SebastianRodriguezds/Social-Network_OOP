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
        print("\nSocial Network:")
        sn.display_network()

    common_friends = sn.get_common_friends_matrix()

    print("\nFriend recommendations:")
    for name in sn.members:
        suggestion = sn.recommend_friend(name, common_friends)
        if suggestion:
            print(f"Recommended friend for {name} is {suggestion}")
        else:
            print(f"Recommended friend for {name} is none")

if __name__ == "__main__":
    main()

