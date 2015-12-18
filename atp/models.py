from atp import db


class BaseModel(object):
    id = db.Column(db.Integer, primary_key=True)

    @property
    def url(self):
        return "{name}/{id}".format(self.__tablename__, self.id)


class User(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(128))


class Player(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    skype_login = db.Column(db.String(128))
    user_cans = db.relationship('GameDateUserCan', backref='player_date',
                                lazy='dynamic')


class Game(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    game_time = db.Column(db.Time)
    dates = db.relationship('GameDate', backref='game', lazy='dynamic')
    selected_date = 1
    place = db.Column(db.String(128))
    description = db.Column(db.Text)


class GameDate(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    game_date = db.Column(db.Date)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    user_cans = db.relationship('GameDateUserCan', backref='game_date',
                                lazy='dynamic')


class GameDateUserCan(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    game_date_id = db.Column(db.Integer, db.ForeignKey('game_date.id'))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
