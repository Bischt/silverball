from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DecimalField, HiddenField, TextField, BooleanField
from wtforms.validators import DataRequired, NumberRange, Required, Optional, AnyOf


class ConfigurationForm(FlaskForm):
    leaguename = StringField('League Name', validators=[Optional()])

    welcometext = TextField('Welcome Text', validators=[Optional()])


class AddPostForm(FlaskForm):
    title = StringField('Post Title', validators=[Required(message="Post title cannot be blank")])

    content = TextField('Post Content', validators=[Required(message="Post content cannot be blank")])


class AddPlayerForm(FlaskForm):
    nick = StringField('Initials', validators=[Optional()])

    name = StringField('Name', validators=[Required(message="Must enter player name")])

    email = StringField('Email', validators=[Optional()])

    phone = StringField('Phone', validators=[Optional()])

    location = StringField('Location', validators=[Optional()])

    ifpanumber = IntegerField('IFPA Number', validators=[Optional()])

    pinside = StringField('Pinside', validators=[Optional()])

    notes = TextField('Notes', validators=[Optional()])

    status = SelectField(
        'Dues Paid?',
        choices=[('0', 'Not Paid'), ('1', 'Paid')],
        validators=[AnyOf(values=['0', '1'], message="Must select whether or not dues have been paid")]
    )

    active = SelectField(
        'Active?',
        choices=[('1', 'Yes'), ('0', 'No')],
        validators=[AnyOf(values=['0', '1'], message="Must select whether or not player is active")]
    )


class AddLocationForm(FlaskForm):
    name = StringField('Name', validators=[Required(message="Must enter location name")])

    address = StringField('Address', validators=[Optional()])

    addressprivate = SelectField(
        'Hide Address',
        choices=[('false', 'No'), ('true', 'Yes')],
        validators=[AnyOf(values=['false', 'true'], message="Must select to hide or display address")]
    )

    notes = TextField('Notes', validators=[Optional()])

    loctype = SelectField(
        'Location Type',
        choices=[('0', 'Public Location'), ('1', 'Private Residence')],
        validators=[AnyOf(values=['0', '1'], message="Must select a location type")]
    )

    active = SelectField(
        'Active',
        choices=[('true', 'Yes'), ('false', 'No')],
        validators=[AnyOf(values=['false', 'true'], message="Must select active or not")]
    )


class CreateSeasonForm(FlaskForm):
    seasonLength = IntegerField('Season Length',
                                validators=[NumberRange(
                                    min=1,
                                    message="Must enter a non zero season length")
                                ])

    dropWeeks = IntegerField('Weeks To Drop',
                             validators=[NumberRange(
                                 min=0,
                                 message="Must enter the number of weeks to drop")
                             ])

    numRounds = IntegerField('Number of Rounds',
                             validators=[NumberRange(
                                 min=1,
                                 message="Must enter the number of rounds to play")
                             ])

    numGames = IntegerField('Games Per Round',
                            validators=[NumberRange(
                                min=1,
                                message="Must enter the number of games played per round")
                            ])

    dues = DecimalField('Dues',
                        validators=[NumberRange(
                            min=0,
                            message="Must enter the amount of league dues to be collected")
                        ])

    sid = HiddenField('sid', validators=[Optional()])

    seeding = SelectField(
        'Seeding',
        choices=[('bapa', 'BAPA'), ('ifpa', 'IFPA')],
        validators=[AnyOf(values=['bapa', 'ifpa'], message="Must select a seeding option")]
    )

    scoring = SelectField(
        'Scoring',
        choices=[('bapa', 'BAPA (8/6/4/2 - 8/5/2)'),
                 ('ifpa', 'IFPA (7/5/3/1 - 7/4/1)')],
        validators=[AnyOf(values=['bapa', 'ifpa'], message="Must select a scoring option")]
    )

    playorder = SelectField(
        'Play Order',
        choices=[('balanced', 'Balanced'),
                 ('random', 'Random'),
                 ('topseed', 'Top Seed'),
                 ('previous', 'Previous')],
        validators=[AnyOf(values=['balanced',
                                  'random',
                                  'topseed',
                                  'previous'],
                          message="Must select the play order")]
    )

    drawing = SelectField(
        'Machine Drawing',
        choices=[('effacatious', 'Effacatious'),
                 ('manual', 'Manual'),
                 ('random', 'Random'),
                 ('bank', 'Bank')],
        validators=[AnyOf(values=['effacatious',
                                  'manual',
                                  'random',
                                  'bank'],
                          message="Must select machine drawing")]
    )
