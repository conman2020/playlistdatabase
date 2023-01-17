"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'playlists'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )
    description = db.Column(
        db.String(140),
        nullable=False,
    )
    playlistsongs = db.relationship(
        'Song',
        secondary="playlistsongs"
    )


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = 'songs'
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    title = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )
    artist = db.Column(
        db.String(140),
        nullable=False,
    )
    playlistssongs = db.relationship(
        'Song',
        secondary="playlistsongs"
    )





class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlistsongs'
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    playlist_id = db.Column(
        db.Integer,
        db.ForeignKey('playlists.id', ondelete='cascade')
    )

    song_id = db.Column(
        db.Integer,
        db.ForeignKey('songs.id', ondelete='cascade')
    )

    # ADD THE NECESSARY CODE HERE


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
