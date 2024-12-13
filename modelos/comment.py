class Comment:
    def __init__(self, comment_id, post_id, name, email, body):
        self.comment_id = comment_id
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body

    def __str__(self):
        return f"Comment(ID: {self.comment_id}, Name: {self.name}, Email: {self.email})"

    @staticmethod
    def from_json(data):
        return Comment(
            comment_id=data["id"],
            post_id=data["postId"],
            name=data["name"],
            email=data["email"],
            body=data["body"]
        )