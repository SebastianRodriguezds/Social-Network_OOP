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

    while True:
        choice = input("\nWould you like to check how many friends a member has? (y/n): ").lower()
        if choice == 'n':
            break
        elif choice == 'y':
            member_name = input("Enter the name: ")
            try:
                count = sn.get_friend_count(member_name)
                print(f"{member_name} has {count} friend(s).")
            except ValueError as e:
                print(e)
        else:
            print("Please enter 'y' or 'no'.")
    
    choice = input("\nWould you like to see members with least or no friends? (y/n): ").lower()
    if choice == 'y':
        least_friends, no_friends = sn.get_least_connected_members()

        if least_friends:
            print("\nMembers with the fewest friends: ")
            for name in least_friends:
                print(f"- {name}")
        else:
            print("\nNo members with few friends.")
        
        if no_friends:
            print("\nMembers with no friends at all: ")
            for name in no_friends:
                print(f"- {name}")
        else:
            print("\nAll members have at least one friend.")

    while True:
        choice = input("\nWould you like to see the relationships of a member? (y/n): ").lower()
        if choice == 'n':
            break
        elif choice == 'y':
            member_name = input("Enter the name: ")
            try:
                relationships = sn.get_relationship(member_name)
                if relationships:
                    print(f"{member_name} is connected with: {', '.join(relationships)}")
                else:
                    print(f"{member_name} has no friends.")
            except ValueError as e:
                print(e)
        else:
            print("Please enter 'y' or 'n'.")
    
    choice = input("\nWould you like to see indirect relationships (friends of friends)? (y/n): ").lower()
    if choice == 'y':
        indirect_friends = sn.social_indirect_relationships()
        print("\nIndirect Relationships: ")
        for member, indirect in indirect_friends.items():
            if indirect:
                print(f"{member} -> {', '.join(indirect)}")
            else:
                print(f"{member} -> No indirect friends")
        

if __name__ == "__main__":
    main()

