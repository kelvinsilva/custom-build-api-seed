#kelvin silva
#cs 18 armen donigian

import os
from flask import Flask, url_for, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data.sqlite')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

db = SQLAlchemy(app)


class ValidationError(ValueError):
    pass


class politicsPost(db.Model):
    __tablename__ = 'politics'
    id = db.Column(db.Integer, primary_key=True)
    party = db.Column(db.String(64), index=True)
    createdUtc = db.Column(db.Float, index=True)
    score = db.Column(db.Integer, index=True)
    domain = db.Column(db.String(512), index=True)
    title = db.Column(db.String(512), index=True)
    author = db.Column(db.String(128), index=True)
    ups = db.Column(db.Integer, index=True)
    downs = db.Column(db.Integer, index=True)
    numComments = db.Column(db.Integer, index=True)
    permaLinks = db.Column(db.String(512), index=False)
    thumbNail = db.Column(db.String(512), index=False)
    urlImg = db.Column(db.String(512), index=False)
    

    def get_url(self):
        return url_for('get_politics', id=self.id, _external=True)

    def export_data(self):
        return {
            
            'self_url': self.get_url(),
            'party' : self.party,
            'createdUtc' : self.createdUtc,
            'score' : self.score,
            'domain' : self.domain,
            'title' : self.title,
            'author' : self.author,
            'ups' : self.ups,
            'downs' : self.downs,
            'numComments' : self.numComments,
            'permaLinks' : self.permaLinks,
            'thumbNail' : self.thumbNail,
            'urlImg' : self.urlImg
            
        }

    def import_data(self, data):
        try:
            self.party = data['party']
            self.createdUtc = data['createdUtc']
            self.score = data['score']
            self.domain = data['domain']
            self.title = data['title']
            self.author = data['author']
            self.ups = data['ups']
            self.downs = data['downs']
            self.numComments = data['numComments']
            self.permaLinks = data['permaLinks']
            self.thumbNail = data['thumbNail']
            self.urlImg = data['urlImg']
            
        except KeyError as e:
            raise ValidationError('Invalid politics post: missing ' + e.args[0])
        return self


@app.route('/politics/', methods=['GET'])
def get_politics():
    return jsonify({'politics': [polit.get_url() for polit in
                                  politicsPost.query.all()]})

@app.route('/politics/<int:id>', methods=['GET'])
def get_politicsAt(id):
    return jsonify(politicsPost.query.get_or_404(id).export_data())

@app.route('/politics/', methods=['POST'])
def new_politics():
    polit = politicsPost()
    polit.import_data(request.json)
    db.session.add(polit)
    db.session.commit()
    return jsonify({}), 201, {'Location': polit.get_url()}

@app.route('/politics/<int:id>', methods=['PUT'])
def edit_politics(id):
    politics = politicsPost.query.get_or_404(id)
    politics.import_data(request.json)
    db.session.add(politics)
    db.session.commit()
    return jsonify({})


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)