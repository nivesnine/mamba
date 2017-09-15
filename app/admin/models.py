from app import db

# Create the Models
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100))
    text = db.Column(db.Text())
    published = db.Column(db.Boolean(), default=0)

    @classmethod
    def all(cls):
        """
        Returns all researcher items from the database
        """
        return db.session.query(cls).all()

