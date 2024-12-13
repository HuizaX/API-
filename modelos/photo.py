class Photo:
    def __init__(self, photo_id, album_id, title, url, thumbnail_url):
        self.photo_id = photo_id
        self.album_id = album_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    def __str__(self):
        return f"Photo(ID: {self.photo_id}, Title: {self.title}, URL: {self.url})"

    @staticmethod
    def from_json(data):
        return Photo(
            photo_id=data["id"],
            album_id=data["albumId"],
            title=data["title"],
            url=data["url"],
            thumbnail_url=data["thumbnailUrl"]
        )