from app.framework.models.role_base import RoleBase
from app import db

class Role(db.Model, RoleBase):
    __tablename__ = 'roles'

    user_roles = db.relationship('UserRoles', back_populates='role')