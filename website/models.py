from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # ID 
    teaname = db.Column(db.String(150), nullable=False)           # 차이름
    country = db.Column(db.String(150), nullable=True)           # 원산지
    type_of_tea = db.Column(db.String(150), nullable=False)       # 차 종류: 백차, 황차, 녹차, ...
    tea_quantity = db.Column(db.Integer, nullable=True)          # 무게
    tea_temprature = db.Column(db.Integer, nullable=True)        # 온도
    tea_brew_time = db.Column(db.Integer, nullable=True)         # 시간

    grade = db.Column(db.Integer, nullable=False)  # 평점

    # 맛: ['풍부함', '기름짐', '훈연', '균형', '불쾌감', '후미', 
    #      '수렴성', '매운맛', '신맛', '쓴맛', '짠맛', '단맛']
    dry_leaf_appearence = db.Column(db.String(5000), nullable=True)  # 마른 잎 외형
    brew_leaf_appearence = db.Column(db.String(5000), nullable=True) # 우린 잎 외형
    dry_leaf_perfume = db.Column(db.String(5000), nullable=True)     # 마른 잎 향
    brew_leaf_perfume = db.Column(db.String(5000), nullable=True)    # 우린 잎 향
    t1 = db.Column(db.Integer, nullable=True) 
    t2 = db.Column(db.Integer, nullable=True)
    t3 = db.Column(db.Integer, nullable=True)
    t4 = db.Column(db.Integer, nullable=True)
    t5 = db.Column(db.Integer, nullable=True)
    t6 = db.Column(db.Integer, nullable=True)
    t7 = db.Column(db.Integer, nullable=True)
    t8 = db.Column(db.Integer, nullable=True)
    t9 = db.Column(db.Integer, nullable=True)
    t10 = db.Column(db.Integer, nullable=True)
    t11 = db.Column(db.Integer, nullable=True)
    t12 = db.Column(db.Integer, nullable=True)

    # 향 : ['식물향', '바다형', '우유향', '꽃향', '토양향', '목재향', 
    #       '과일향', '탄향', '동물향', '광물향', '단향', '매운향']
    p1 = db.Column(db.Integer, nullable=True)
    p2 = db.Column(db.Integer, nullable=True)
    p3 = db.Column(db.Integer, nullable=True)
    p4 = db.Column(db.Integer, nullable=True)
    p5 = db.Column(db.Integer, nullable=True)
    p6 = db.Column(db.Integer, nullable=True)
    p7 = db.Column(db.Integer, nullable=True)
    p8 = db.Column(db.Integer, nullable=True)
    p9 = db.Column(db.Integer, nullable=True)
    p10 = db.Column(db.Integer, nullable=True)
    p11 = db.Column(db.Integer, nullable=True)
    p12 = db.Column(db.Integer, nullable=True)

    leaf_color = db.Column(db.String(100), nullable=True) # 수색
    transparency = db.Column(db.Integer, nullable=True)   # 투명도
    finish = db.Column(db.Integer, nullable=True)   # 피니쉬

    note = db.Column(db.String(10000), nullable=True)   # 총평
    image = db.Column(db.String(150), nullable=True)    # 사진 

    date = db.Column(db.DateTime(timezone=True), default=func.now()) # 기록날짜
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))        # 사용자 id


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    nickname = db.Column(db.String(150))
    notes = db.relationship('Note')

# class Note(db.Model):
#     id = db.Column(db.Integer, primary_key=True)  # ID 
#     data = db.Column(db.String(150))           # 차이름
#     date = db.Column(db.DateTime(timezone=True), default=func.now()) # 기록날짜
#     image = db.Column(db.String(150))     # 사진 
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 