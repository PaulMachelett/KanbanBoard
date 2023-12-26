from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from src.Administration import Administration
from src.bo.Person import Person
from src.bo.BusinessObject import BusinessObject as bo
from src.bo.Project import Project
from src.bo.Phase import Phase
from src.bo.KanbanCard import KanbanCard
from src.bo.Comment import Comment
from src.bo.ProjectParticipation import ProjectParticipation


app = Flask(__name__)
api = Api(app, version='1.0')
CORS(app, resources=r'/kbb/*')

kbb = api.namespace('kbb', description='Funktionen der Kanbanboard Anwendung')

bo = api.model('BusinessObject', {
    'id': fields.Integer(attribute='_id', description='Der Unique Identifier eines Business Object')
})

kanbancard = api.inherit('Kanbancard', bo, {
    'id': fields.Integer(attribute='_id', description='Kanbancard Id'),
    'title': fields.String(attribute='_title', description='Title of the Kanbancard'),
    'content': fields.String(attribute='_content', description='Content of the Kanbancard'),
    'phaseid': fields.Integer(attribute='_phaseid', description='Phase ID of the Kanbancard'),
    'start_date': fields.DateTime(attribute='_start_date', description='Start date of the Kanbancard'),
    'end_date': fields.DateTime(attribute='_end_date', description='End date of the Kanbancard'),
    'creator': fields.String(attribute='_creator', description='Creator of the Kanbancard'),
    'assigned_person': fields.Integer(attribute='_assigned_person', description='Assigned person of the Kanbancard')
})


person = api.inherit('Person', bo, {
    'id': fields.Integer(attribute='_id', description='Person Id'),
    'nickname': fields.String(attribute='_nickname', description='Nickname'),
    'firstname': fields.String(attribute='_firstname', description='Firstname'),
    'lastname': fields.String(attribute='_lastname', description='Lastname'),
    'googleid': fields.String(attribute='_googleid', description='Googleid'),
    'email': fields.String(attribute='_email', description='Email')
})

project = api.inherit('Project', bo, {
    'id': fields.Integer(attribute='_id', description='Project Id'),
    'start_date': fields.String(attribute='_start_date', description='Start Date'),
    'end_date': fields.String(attribute='_end_date', description='End Date'),
    'name': fields.String(attribute='_name', description='Name')
})

phase = api.inherit('Phase', bo, {
    'id': fields.Integer(attribute='_id', description='Phase Id'),
    'name': fields.String(attribute='_name', description='Phase Name'),
    'projectid': fields.Integer(attribute='_projectid', description='ProjectId')
})

comment = api.inherit('Comment', bo, {
    'id': fields.Integer(attribute='_id', description='Comment ID'),
    'creator': fields.Integer(attribute='_creator', description='Comment creator'),
    'content': fields.String(attribute='_content', description='Comment content'),
    'cardid': fields.Integer(attribute='_cardid', description='CardID of the comment'),
    'creation_date': fields.DateTime(attribute='_creation_date', description='Comment creation date')
})

projectparticipation = api.inherit('ProjectParticipation', bo, {
    'id': fields.Integer(attribute='_id', description='Projectparticipation Id'),
    'projectid': fields.Integer(attribute='_projectid', description='Project Id'),
    'personid': fields.Integer(attribute='_personid', description='Person Id'),
})


@kbb.route("/kanbancard/phase/<int:phaseid>")
@kbb.param('phaseid', 'PhaseId der Kanbancard')
class KanbanCardListOperations(Resource):

    @api.marshal_list_with(kanbancard)
    def get(self, phaseid):
        adm = Administration()
        list_kanbancard = adm.get_all_kanbancard_by_phaseid(phaseid)
        return list_kanbancard


@kbb.route("/kanbancard")
class KanbanCardOperations(Resource):

    @api.marshal_with(kanbancard)
    @api.expect(kanbancard)
    def put(self):
        k = KanbanCard.from_dict(api.payload)

        if k is not None:
            adm = Administration()
            adm.edit_kanbancard(k)
            return '', 200
        else:
            return '', 500

    @api.marshal_with(kanbancard)
    @api.expect(kanbancard)
    def post(self):
        k = KanbanCard.from_dict(api.payload)

        if k is not None:
            adm = Administration()
            adm.create_kanbancard(k)
            return '', 200
        else:
            return '', 500


@kbb.route('/kanbancard/<int:id>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('id', 'Die id der Kanbancard')
class KanbancardDeleteOperations(Resource):

    def delete(self, id):
        adm = Administration()
        return adm.delete_kanbancard(id)


@kbb.route('/person')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class PersonOperations(Resource):

    @api.marshal_with(person)
    @api.expect(person)
    def put(self):
        p = Person.from_dict(api.payload)

        if p is not None:
            adm = Administration()
            adm.edit_person(p)
            return '', 200
        else:
            return '', 500

    @api.marshal_with(person)
    @api.expect(person)
    def post(self):
        p = Person.from_dict(api.payload)

        if p is not None:
            adm = Administration()
            adm.create_person(p)
            return '', 200
        else:
            return '', 500


@kbb.route('/person/<int:googleid>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('googleid', 'Die googleid der Person')
class PersonGetByGoogleIdOperations(Resource):

    @api.marshal_with(person)
    def get(self, googleid):
        adm = Administration()
        p = adm.get_person_by_googleid(googleid)
        return p


@kbb.route('/person/<string:email>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('email', 'Die email der Person')
class PersonGetByMailOperations(Resource):

    @api.marshal_with(person)
    def get(self, email):
        adm = Administration()
        p = adm.get_person_by_email(email)
        return p


@kbb.route('/person/delete/<int:id>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('id', 'Die id der Person')
class PersonDeleteOperations(Resource):

    @api.marshal_with(person)
    def delete(self, id):
        adm = Administration()
        adm.delete_person(id)
        return id


@kbb.route('/projectparticipation/projects/<int:personid>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('personid', 'Die id der Person')
class ProjectParticipationGetAllProjectByPersonIdOperations(Resource):

    @api.marshal_list_with(project)
    def get(self, personid):
        adm = Administration()
        return adm.get_all_project_by_personid(personid)


@kbb.route('/projectparticipation/persons/<int:projectid>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('projectid', 'Die id des Projekts')
class ProjectParticipationGetAllPersonByProjectIdOperations(Resource):

    @api.marshal_list_with(person)
    def get(self, projectid):
        adm = Administration()
        return adm.get_all_person_by_projectid(projectid)


@kbb.route('/projectparticipation/remove')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ProjectParticipationRemoveOperations(Resource):

    @api.marshal_with(projectparticipation)
    @api.expect(projectparticipation)
    def put(self):
        p = ProjectParticipation.from_dict(api.payload)
        adm = Administration()
        return adm.remove_person_from_project(p)


@kbb.route('/project')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class ProjectOperations(Resource):

    @api.expect(project)
    def post(self):
        p = Project.from_dict(api.payload)

        if p is not None:
            adm = Administration()
            adm.create_project(p)
            return '', 200
        else:
            return '', 500

    @api.expect(project)
    def put(self):
        p = Project.from_dict(api.payload)

        if p is not None:
            adm = Administration()
            adm.edit_project(p)
            return '', 200
        else:
            return '', 500


@kbb.route('/project/<int:projectid>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('projectid', 'Die id des Projects')
class ProjectDeleteOperations(Resource):

    def delete(self, projectid):
        adm = Administration()
        return adm.delete_project(projectid)


@kbb.route('/phase')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class PhaseOperations(Resource):

    @api.expect(phase)
    def post(self):
        p = Phase.from_dict(api.payload)

        if p is not None:
            adm = Administration()
            adm.create_phase(p)
            return '', 200
        else:
            return '', 500

    @api.expect(phase)
    def put(self):
        p = Phase.from_dict(api.payload)

        if p is not None:
            adm = Administration()
            adm.edit_phase(p)
            return '', 200
        else:
            return '', 500


@kbb.route('/phase/project/<int:projectid>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('projectid', 'Die id des Projekts')
class PhaseProjectIdOperations(Resource):

    @api.marshal_list_with(phase)
    def get(self, projectid):
        adm = Administration()
        return adm.get_all_phase_by_projectid(projectid)


@kbb.route('/phase/<int:phaseid>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('phaseid', 'Die id der Phase')
class PhaseDeleteOperations(Resource):

    def delete(self, phaseid):
        adm = Administration()
        return adm.delete_phase(phaseid)


@kbb.route('/comment')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
class CommentOperations(Resource):

    @api.expect(comment)
    def post(self):
        c = Comment.from_dict(api.payload)

        if c is not None:
            adm = Administration()
            adm.create_comment(c)
            return '', 200
        else:
            return '', 500

    @api.expect(comment)
    def put(self):
        c = Comment.from_dict(api.payload)

        if c is not None:
            adm = Administration()
            adm.edit_comment(c)
            return '', 200
        else:
            return '', 500


@kbb.route('/comment/card/<int:cardid>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('carid', 'Die ID des Comments')
class CommentCardIDOperations(Resource):

    @api.marshal_list_with(comment)
    def get(self, cardid):
            adm = Administration()
            return adm.get_all_comment_by_cardid(cardid)


@kbb.route('/comment/<int:commentid>')
@kbb.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@kbb.param('commentid', 'Die ID des Kommentars')
class CommentDeleteOperations(Resource):

    def delete(self, commentid):
     adm = Administration()
     return adm.delete_comment(commentid)


if __name__ == '__main__':
    app.run(debug=True)
