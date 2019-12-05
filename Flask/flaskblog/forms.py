from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms import StringField,SubmitField,BooleanField,PasswordField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators = [DataRequired(),Length(min=2,max=40)])
    email = StringField('E-mail',validators = [DataRequired(),Email()] )
    password = PasswordField('Password',validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators = [DataRequired(),EqualTo('password')])

    submit = SubmitField('SignUp')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user :
            raise ValidationError('This username is already taken.Please try another.')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user :
            raise ValidationError('This email is already taken.Please try another.')

class LoginForm(FlaskForm):
    
    email = StringField('E-mail',validators = [DataRequired(),Email()] )
    password = PasswordField('Password',validators = [DataRequired()])
    remember = BooleanField('Remember me ')

    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',validators = [DataRequired(),Length(min=2,max=40)])
    email = StringField('E-mail',validators = [DataRequired(),Email()] )
    picture = FileField('Update Profile Picture',validators = [FileAllowed(['jpg','png'])])
    
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user :
                raise ValidationError('This username is already taken.Please try another.')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user :
                raise ValidationError('This email is already taken.Please try another.')

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    content = TextAreaField('Content',validators = [DataRequired()])
    submit = SubmitField('Post')
