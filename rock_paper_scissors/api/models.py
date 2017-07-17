from sqlalchemy import Column, Integer, String
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


ModelBase = declarative_base()


class Game(ModelBase):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    player_1_id = Column(Integer, ForeignKey('user.id'))
    player_2_id = Column(Integer, ForeignKey('user.id'))
    round_id = Column(Integer, ForeignKey('round.id'), nullable=False)
    rounds_limit = Column(Integer)
    winner_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    player_1 = relationship('User', foreign_keys=[player_1_id])
    player_2 = relationship('User', foreign_keys=[player_2_id])
    winner = relationship('User', foreign_keys=[winner_id])

    rounds_remaining = relationship('Round', foreign_keys='Round.id')
    current_round = relationship('Round', foreign_keys='Round.id')


class Round(ModelBase):
    __tablename__ = 'round'

    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'))
    winner_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    game = relationship('Game')
    user = relationship('User')
    player_1_choice = relationship('Choice', foreign_keys=[player_1_choice_id])
    player_2_choice = relationship('Choice', foreign_keys=[player_2_choice_id])


class User(ModelBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)
    choices_id = Column(Integer, ForeignKey('choice.player_id'))

    games = relationship('Game', foriegn_keys=['Game.player_1_id', 'Game.player_2_id'])
    choices = relationship('Choice')


class Choice(ModelBase):
    __tablename__ = 'choice'

    id = Column(Integer, primary_key=True)
    rounds_id = Column(Integer, ForeignKey('rounds.id'))
    player_id = Column(Integer, ForeignKey('user.id'))
    move = Column('moves', Enum('Paper', 'Rock', 'Scissors'))

    user = relationship('User')
    round = relationship('Round')
