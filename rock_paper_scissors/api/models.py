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
    round_id = Column(Integer, ForeignKey('round.id'))
    rounds_choice = Column(Integer)
    rounds_decrement = Column(Integer)
    current_round = Column(Integer)
    winner_id = Column(Integer, ForeignKey('user.id'))

    player_1 = relationship('User', foreign_key=[player_1_id])
    player_2 = relationship('User', foreign_key=[player_2_id])
    winner = relationship('User', foreign_key=[winner_id])


class Round(ModelBase):
    __tablename__ = 'round'

    id = Column(Integer, primary_key=True)
    player_1_choice_id = Column(Integer, ForeignKey('choice.id'))
    player_2_choice_id = Column(Integer, ForeignKey('choice.id'))
    winner_id = Column(Integer, ForeignKey('user.id'))
    game_id = Column(Integer, ForeignKey('game.id'))

    game = relationship('Game')
    user = relationship('User')
    player_1_choice = relationship('Choice', foreign_keys=[player_1_choice_id])
    player_2_choice = relationship('Choice', foreign_keys=[player_2_choice_id])


class User(ModelBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)
    choices = Column(String, ForeignKey('choice.move'))

    game = relationship('Game', back_populates='user')
    choice = relationship('Choice', back_populates='user')
    round = relationship('Round', back_populate='user')


class Choice(ModelBase):
    __tablename__ = 'choice'

    id = Column(Integer, primary_key=True)
    rounds_id = Column(Integer, ForeignKey('rounds.id'))
    player = Column(Integer, ForeignKey('user.id'))
    move = Column('moves', Enum('Paper', 'Rock', 'Scissors'))

    user = relationship('User', back_populates='choice')
    round = relationship('Round', back_populate='choice')