from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    easiness = Column(Float, default=2.5)
    interval = Column(Integer, default=0)
    repetitions = Column(Integer, default=0)
    due = Column(DateTime, default=datetime.utcnow)

class SRS:
    def __init__(self, db_path="sqlite:///srs.db"):
        self.engine = create_engine(db_path, echo=False, future=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_card(self, question, answer):
        s = self.Session()
        c = Card(question=question, answer=answer, due=datetime.utcnow())
        s.add(c); s.commit(); s.close()
        return c

    def get_due_cards(self, limit=20):
        s = self.Session()
        now = datetime.utcnow()
        cards = s.query(Card).filter(Card.due <= now).limit(limit).all()
        s.close()
        return cards

    def record_review(self, card_id: int, quality: int):
        s = self.Session()
        card = s.get(Card, card_id)
        if card is None:
            s.close()
            raise ValueError("Card not found")
        if quality < 3:
            card.repetitions = 0
            card.interval = 1
        else:
            card.repetitions += 1
            if card.repetitions == 1:
                card.interval = 1
            elif card.repetitions == 2:
                card.interval = 6
            else:
                card.interval = int(card.interval * card.easiness)
        card.easiness = max(1.3, card.easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02)))
        card.due = datetime.utcnow() + timedelta(days=card.interval)
        s.commit()
        s.close()
        return card
