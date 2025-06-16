import os
from models.member import Member

class SocialNetwork:
    def __init__(self):
        self.members = {}
    
    def load_from_file(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError("The file does not exist.")
    
        with open(file_path, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        
        try:
            expected_members = int(lines[0])
        except ValueError:
            raise ValueError("The first line of the file must be a integer.")
        
        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 1:
                member, friend = parts[0], None
            elif len(parts) == 2:
                member, friend = parts
            else:
                raise ValueError(f"Invalid format in line: {line}")
            
            if member not in self.members:
                self.members[member] = Member(member)
            if friend:
                if friend not in self.members:
                    self.members[friend] = Member(friend)
                self.members[member].add_friend(friend)
                self.members[friend].add_friend(member)

        if len(self.members) != expected_members:
            raise ValueError("The number of members does not match the number specified.")
    
    def display_network(self):
        for member in sorted(self.members.values(), key=lambda x: x.name):
            print(member)

    def get_common_friends_matrix(self):
        member_names = list(self.members.keys())
        matrix = {}

        for name1 in member_names:
            row = []
            friends1 = self.members[name1].friends
            for name2 in member_names:
                if name1 == name2:
                    row.append(0)
                else:
                    friends2 = self.members[name2].friends
                    common = friends1.intersection(friends2)
                    row.append(len(common))
            matrix[name1] = row
        return matrix
    
    def recommend_friend(self, member__name, common_friends):
        if member__name not in self.members:
            return None
        
        member_list = list(self.members.keys())
        row = common_friends[member__name]
        max_common = -1
        recommended  = None

        for i, count in enumerate(row):
            candidate = member_list[i]
            if (
                candidate != member__name and 
                candidate not in self.members[member__name].friends and
                count > max_common
            ):
                max_common = count
                recommended = candidate

        return recommended if max_common > 0 else None