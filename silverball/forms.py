from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, DecimalField, HiddenField, TextField
from wtforms.validators import DataRequired

class CreateSeasonForm(FlaskForm):

    seasonLength = IntegerField('seasonLength')

    dropWeeks = IntegerField('dropWeeks')

    numRounds = IntegerField('numRounds')

    numGames = IntegerField('numGames')

    dues = DecimalField('dues')

    sid = HiddenField('sid')

    seeding = SelectField(
        'Seeding',
        choices=[('bapa', 'BAPA'), ('ifpa', 'IFPA')]
    )

    scoring = SelectField(
        'Scoring',
        choices=[('bapa', 'BAPA (8/6/4/2 - 8/5/2)'), 
                 ('ifpa', 'IFPA (7/5/3/1 - 7/4/1)')]
    )

    playorder = SelectField(
        'Play Order',
        choices=[('balanced', 'Balanced'), 
                 ('random', 'Random'), 
                 ('topseed', 'Top Seed'), 
                 ('previous', 'Previous')]
    )

    drawing = SelectField(
        'Machine Drawing',
        choices=[('effacatious', 'Effacatious'), 
                ('manual', 'Manual'), 
                ('random', 'Random'), 
                ('bank', 'Bank')]
    )

