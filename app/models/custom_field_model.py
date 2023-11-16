from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import JSON
import datetime

db = SQLAlchemy()

class CustomField(db.Model):
    __tablename__ = 'CustomFields'

    CustomFieldID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    AssetID = db.Column(db.Integer, db.ForeignKey('Assets.AssetID'))
    FieldName = db.Column(db.String(255), nullable=False)
    FieldValue = db.Column(JSON)