# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Time, text
from sqlalchemy.dialects.mysql.base import LONGBLOB
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Advertisement(Base):
    __tablename__ = 'advertisement'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    is_default = Column(Integer)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))


class Alert(Base):
    __tablename__ = 'alert'

    id = Column(Integer, primary_key=True)
    phno = Column(Integer)
    isactive = Column(Integer)


class BillInfo(Base):
    __tablename__ = 'bill_info'

    id = Column(Integer, primary_key=True)
    is_default = Column(Integer)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))


class CustomerInfo(Base):
    __tablename__ = 'customer_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone_no = Column(String(50))
    email_id = Column(String(50))
    address = Column(String(100))
    personal_desc = Column(String(200))
    description = Column(String(100))
    image = Column(String(100))
    is_default = Column(Integer)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))


class DeviceInfo(Base):
    __tablename__ = 'device_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    device_add_info = Column(String(50))
    current_profile_id = Column(Integer, index=True)
    current_user_id = Column(Integer, index=True)
    location = Column(String(100))
    status = Column(String(20))
    is_default = Column(Integer)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))
    device_id = Column(String(50), nullable=False, unique=True)
    version = Column(String(20))
    device_phone_number = Column(Integer)
    os_info = Column(String(50))
    model_info = Column(String(50))
    login_user_load = Column(Integer)
    current_user_name = Column(String(50))
    current_user_pwd = Column(String(50))
    is_lock_active = Column(Integer)
    locking_key = Column(String(50), server_default=text("'123'"))
    createuser = Column(Integer)
    is_user_advanced = Column(Integer)
    current_survey_id = Column(Integer)


class Organisation(Base):
    __tablename__ = 'organisation'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    address1 = Column(String(50))
    address2 = Column(String(50))
    address3 = Column(String(50))
    logo_name = Column(String(50))
    logo = Column(LONGBLOB)
    logo1_name = Column(String(50))
    logo2 = Column(LONGBLOB)
    location1 = Column(String(50))
    location2 = Column(String(50))
    company_key = Column(String(50), nullable=False)
    is_default = Column(Integer)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))


class Permission(Base):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True)
    permission_name = Column(String(7), nullable=False)
    description = Column(String(200))
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))


class ProfileSurvey(Base):
    __tablename__ = 'profile_survey'

    id = Column(Integer, primary_key=True)
    survey_name = Column(String(50), nullable=False)
    profile_id = Column(ForeignKey(u'user_profile.id'), index=True)
    description = Column(String(100))
    schedule_from = Column(Time)
    schedule_to = Column(Time)
    valid_upto = Column(DateTime)
    schedule_days = Column(String(7))
    schedule_isactive = Column(Integer)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))
    thank_you_id = Column(ForeignKey(u'thank_you.id'), index=True)
    permission_id = Column(ForeignKey(u'permission.id'), index=True, server_default=text("'1'"))

    permission = relationship(u'Permission')
    profile = relationship(u'UserProfile')
    thank_you = relationship(u'ThankYou')


class SurveyAnswer(Base):
    __tablename__ = 'survey_answers'

    id = Column(Integer, primary_key=True)
    answer_name = Column(String(50))
    value = Column(Integer)
    image = Column(LONGBLOB)
    description = Column(String(100))
    survey_question_id = Column(ForeignKey(u'survey_questions.id'), index=True)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))
    alert_id = Column(ForeignKey(u'alert.id'), index=True)
    image_id = Column(Integer)
    permission_id = Column(ForeignKey(u'permission.id'), index=True, server_default=text("'1'"))
    half_rating = Column(Integer)

    alert = relationship(u'Alert')
    permission = relationship(u'Permission')
    survey_question = relationship(u'SurveyQuestion')


class SurveyDetail(Base):
    __tablename__ = 'survey_details'

    id = Column(Integer, primary_key=True)
    survey_answer_id = Column(ForeignKey(u'survey_answers.id'), index=True)
    survey_question_id = Column(ForeignKey(u'survey_questions.id'), nullable=False, index=True)
    profile_survey_id = Column(ForeignKey(u'profile_survey.id'), nullable=False, index=True)
    user_profile_id = Column(ForeignKey(u'user_profile.id'), nullable=False, index=True)
    user_id = Column(ForeignKey(u'users.id'), nullable=False, index=True)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))
    customer_info_id = Column(ForeignKey(u'customer_info.id'), index=True)
    bill_info_id = Column(ForeignKey(u'bill_info.id'), index=True)
    device_info_id = Column(ForeignKey(u'device_info.id'), index=True)
    voice_desc = Column(LONGBLOB)
    answer_value = Column(Float)
    is_advanced_user = Column(Integer)

    bill_info = relationship(u'BillInfo')
    customer_info = relationship(u'CustomerInfo')
    device_info = relationship(u'DeviceInfo')
    profile_survey = relationship(u'ProfileSurvey')
    survey_answer = relationship(u'SurveyAnswer')
    survey_question = relationship(u'SurveyQuestion')
    user = relationship(u'User')
    user_profile = relationship(u'UserProfile')


class SurveyQuestion(Base):
    __tablename__ = 'survey_questions'

    id = Column(Integer, primary_key=True)
    question_name = Column(String(50), nullable=False)
    profile_survey_id = Column(ForeignKey(u'profile_survey.id'), index=True)
    question = Column(String(200), nullable=False)
    description = Column(String(500))
    isvisible = Column(Integer)
    valid_upto = Column(DateTime)
    survey_type_id = Column(ForeignKey(u'survey_type.id'), index=True)
    question_order = Column(Integer)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))
    advertisement_id = Column(ForeignKey(u'advertisement.id'), index=True)
    permission_id = Column(ForeignKey(u'permission.id'), index=True, server_default=text("'1'"))

    advertisement = relationship(u'Advertisement')
    permission = relationship(u'Permission')
    profile_survey = relationship(u'ProfileSurvey')
    survey_type = relationship(u'SurveyType')


class SurveyType(Base):
    __tablename__ = 'survey_type'

    id = Column(Integer, primary_key=True)
    type_name = Column(String(50), nullable=False)
    description = Column(String(100))
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))


class ThankYou(Base):
    __tablename__ = 'thank_you'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    image = Column(LONGBLOB)
    is_default = Column(Integer)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))


class UserAdvanced(Base):
    __tablename__ = 'user_advanced'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email_id = Column(String(50))
    pwd = Column(String(50))
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))
    user_id = Column(ForeignKey(u'users.id'), index=True)
    survey_perform_only = Column(Integer)
    current_profile_id = Column(Integer)
    current_survey_id = Column(Integer)

    user = relationship(u'User')


class UserProfile(Base):
    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)
    profile_name = Column(String(50), nullable=False)
    permission_id = Column(ForeignKey(u'permission.id'), nullable=False, index=True, server_default=text("'1'"))
    valid_upto = Column(DateTime)
    valid_upto_isactive = Column(Integer)
    user_id = Column(ForeignKey(u'users.id'), index=True)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))
    multiple_survey = Column(Integer)

    permission = relationship(u'Permission')
    user = relationship(u'User')


class UserSetting(Base):
    __tablename__ = 'user_settings'

    id = Column(Integer, primary_key=True)
    layout_heading = Column(String(50))
    layout_colour = Column(String(10))
    bg_colour = Column(String(10))
    questions_left_isactive = Column(Integer)
    lock_is_active = Column(Integer)
    locking_key = Column(String(20))
    thankyou_timeout = Column(Integer)
    name_is_active = Column(Integer)
    email_is_active = Column(Integer)
    phno_is_active = Column(Integer)
    address_is_active = Column(Integer)
    personaldesc_is_active = Column(Integer)
    customerinfo_is_active = Column(Integer)
    user_id = Column(ForeignKey(u'users.id'), index=True)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))

    user = relationship(u'User')


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    pwd = Column(String(50))
    valid_upto = Column(DateTime)
    valid_upto_isactive = Column(Integer)
    created_by = Column(String(50))
    created_date = Column(DateTime)
    modified_by = Column(String(50))
    last_modified_date = Column(DateTime)
    is_active = Column(Integer, server_default=text("'1'"))
    description = Column(String(100))
    last_name = Column(String(50))
    email_id = Column(String(100), nullable=False)
    ph_no = Column(String(50))
    address_1 = Column(String(300))
    address_2 = Column(String(100))
    address_3 = Column(String(100))
    department = Column(String(50))
    designation = Column(String(50))
    employee_id = Column(String(50))
    gender = Column(String(20))
