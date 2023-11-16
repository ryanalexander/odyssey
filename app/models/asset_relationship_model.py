from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import JSON
import datetime

db = SQLAlchemy()

class AssetRelationship(db.Model):
    __tablename__ = 'AssetRelationships'

    RelationshipID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ParentAssetID = db.Column(db.Integer, db.ForeignKey('Assets.AssetID'))
    ChildAssetID = db.Column(db.Integer, db.ForeignKey('Assets.AssetID'))
    RelationshipType = db.Column(db.String(255), nullable=False)