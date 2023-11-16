from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import JSON
import datetime

db = SQLAlchemy()

class Asset(db.Model):
    __tablename__ = 'Assets'

    AssetID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AssetType = db.Column(db.String(255), nullable=False)
    Name = db.Column(db.String(255), nullable=False)
    CreatedAt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    CreatedBy = db.Column(db.String(255))
    LastModified = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    AdditionalAttributes = db.Column(JSON)