from sqlalchemy import (
    Column,
    Enum,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


ModelBase = declarative_base()


class Game(ModelBase):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    player_1_id = Column(Integer, ForeignKey('user.id'))
    player_2_id = Column(Integer, ForeignKey('user.id'))
    rounds_limit = Column(Integer)
    winner_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    player_1 = relationship('User', foreign_keys=[player_1_id])
    player_2 = relationship('User', foreign_keys=[player_2_id])
    winner = relationship('User', foreign_keys=[winner_id])

    rounds = relationship('Round', foreign_keys='[Round.game_id]')
    current_round = relationship('Round', foreign_keys='Round.id')

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

    winning_choice = relationship('Choice', foreign_keys='Round.winning_choice_id')
    choices = relationship('Choice', foreign_keys='[Choice.round_id]')


class User(ModelBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    games_won = relationship('Game', foreign_keys=['Game.winner_id'])
    rounds_won = relationship('Game', foreign_keys=['Round.winner_id'])
    choices = relationship('Choice', foreign_keys=['Choice.player_id'])


class Choice(ModelBase):
    __tablename__ = 'choice'

    id = Column(Integer, primary_key=True)
    round_id = Column(Integer, ForeignKey('round.id'))
    player_id = Column(Integer, ForeignKey('user.id'))
    move = Column('moves', Enum('Paper', 'Rock', 'Scissors'))
