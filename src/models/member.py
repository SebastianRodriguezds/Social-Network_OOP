from user import User

class Memeber(User):
    def __init__(self, name):
        super().__init__(name)
        self.friends = set()

    def add_friend(self, friend_name):
        self.friends.add(friend_name)
    
    def __str__(self):
        return f"{self.name} -> {', '.join(sorted(self.friends)) if self.friends else ''}"