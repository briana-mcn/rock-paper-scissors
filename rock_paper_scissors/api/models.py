from sqlalchemy import (
    Column,
    create_engine,
    Enum,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, scoped_session, sessionmaker

ModelBase = declarative_base()
engine = create_engine('sqlite://', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
ModelBase.query = db_session.query_property()


class Game(ModelBase):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    player_1_id = Column(Integer, ForeignKey('user.id'))
    player_2_id = Column(Integer, ForeignKey('user.id'))
    rounds_limit = Column(Integer)
    winner_id = Column(Integer, ForeignKey('user.id'), nullable=True)

    player_1 = relationship('User', foreign_keys=[player_1_id])
    player_2 = relationship('User', foreign_keys=[player_2_id])
    winner = relationship('User', foreign_keys=[winner_id])

    rounds = relationship('Round', foreign_keys='[Round.game_id]')

    @property
    def current_round(self):
        for round in self.rounds:
            if round.winning_choice is None:
                return round.id
        return

    @property
    def rounds_remaining(self):
        rounds_complete = 0

        for round in self.rounds:
            if round.winning_choice is not None:
                rounds_complete += 1

        return self.rounds_limit - rounds_complete


class Round(ModelBase):
    __tablename__ = 'round'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'))
    winning_choice_id = Column(Integer, ForeignKey('choice.id'), nullable=True)

    winning_choice = relationship('Choice', foreign_keys=[winning_choice_id])
    choices = relationship('Choice', foreign_keys='[Choice.round_id]')


class User(ModelBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    games_won = relationship('Game', foreign_keys='[Game.winner_id]')
    choices = relationship('Choice', foreign_keys='[Choice.player_id]')

    @property
    def rounds_won(self):
        query = Round.query.join(
            Choice,
            Round.winning_choice_id == Choice.id
        ).filter(
            Choice.player_id == self.id
        )

        rounds = query.all()

        return rounds


class Choice(ModelBase):
    __tablename__ = 'choice'

    id = Column(Integer, primary_key=True)
    round_id = Column(Integer, ForeignKey('round.id'))
    player_id = Column(Integer, ForeignKey('user.id'))
    move = Column('moves', Enum('Paper', 'Rock', 'Scissors'))
