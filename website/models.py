from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # ID 
#     teaname = db.Column(db.String(150))           # 차이름
#     country = db.Column(db.String(150))           # 원산지
#     type_of_tea = db.Column(db.String(150))       # 차 종류: 백차, 황차, 녹차, ...
#     tea_quantity = db.Column(db.Integer)          # 무게
#     tea_temprature = db.Column(db.Integer)        # 온도
#     tea_brew_time = db.Column(db.Integer)         # 시간

#     grade = db.Column(db.Integer)  # 평점

#     # 맛: ['풍부함', '기름짐', '훈연', '균형', '불쾌감', '후미', 
#     #      '수렴성', '매운맛', '신맛', '쓴맛', '짠맛', '단맛']
#     t1 = db.Column(db.Integer, nullable=True) 
#     t2 = db.Column(db.Integer)
#     t3 = db.Column(db.Integer)
#     t4 = db.Column(db.Integer)
#     t5 = db.Column(db.Integer)
#     t6 = db.Column(db.Integer)
#     t7 = db.Column(db.Integer)
#     t8 = db.Column(db.Integer)
#     t9 = db.Column(db.Integer)
#     t10 = db.Column(db.Integer)
#     t11 = db.Column(db.Integer)
#     t12 = db.Column(db.Integer)

#     # 향 : ['식물향', '바다형', '우유향', '꽃향', '토양향', '목재향', 
#     #       '과일향', '탄향', '동물향', '광물향', '단향', '매운향']
#     p1 = db.Column(db.Integer)
#     p2 = db.Column(db.Integer)
#     p3 = db.Column(db.Integer)
#     p4 = db.Column(db.Integer)
#     p5 = db.Column(db.Integer)
#     p6 = db.Column(db.Integer)
#     p7 = db.Column(db.Integer)
#     p8 = db.Column(db.Integer)
#     p9 = db.Column(db.Integer)
#     p10 = db.Column(db.Integer)
#     p11 = db.Column(db.Integer)
#     p12 = db.Column(db.Integer)

#     note = db.Column(db.String(10000))    # 총평
#     image = db.Column(db.String(150))     # 사진 

#     date = db.Column(db.DateTime(timezone=True), default=func.now()) # 기록날짜
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))           # 사용자 id


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    nickname = db.Column(db.String(150))
    notes = db.relationship('Note')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID 
    data = db.Column(db.String(150))           # 차이름
    date = db.Column(db.DateTime(timezone=True), default=func.now()) # 기록날짜
    image = db.Column(db.String(150))     # 사진 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 