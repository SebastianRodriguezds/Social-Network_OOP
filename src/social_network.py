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