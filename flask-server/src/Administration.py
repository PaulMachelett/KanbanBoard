# from src.bo.KanbanCard import KanbanCard
# from src.db.KanbanCardMapper import KanbanCardMapper
from src.bo.Person import Person
from src.db.PersonMapper import PersonMapper
from src.bo.Project import Project
from src.db.ProjectMapper import ProjectMapper
from src.bo.Phase import Phase
from src.db.PhaseMapper import PhaseMapper
from src.bo.KanbanCard import KanbanCard
from src.db.KanbanCardMapper import KanbanCardMapper
from src.bo.Comment import Comment
from src.db.CommentMapper import CommentMapper
from src.db.ProjectParticipationMapper import ProjectParticipationMapper
from src.bo.ProjectParticipation import ProjectParticipation


class Administration(object):

    def __init__(self):
        pass

    # ---------- Person ----------

    def create_person(self, p):
        person = Person()
        person.set_nickname(p.get_nickname())
        person.set_firstname(p.get_firstname())
        person.set_lastname(p.get_lastname())
        person.set_googleid(p.get_googleid())
        person.set_email(p.get_email())

        with PersonMapper() as mapper:
            return mapper.insert(person)

    def delete_person(self, id):
        with PersonMapper() as mapper:
            return mapper.delete(id)

    def edit_person(self, person):
        with PersonMapper() as mapper:
            return mapper.update(person)

    def get_person_by_googleid(self, id):
        with PersonMapper() as mapper:
            return mapper.find_by_googleid(id)

    def get_person_by_email(self, email):
        with PersonMapper() as mapper:
            return mapper.find_by_email(email)

    # ---------- ProjectParticipation ----------

    def get_all_person_by_projectid(self, id):
        with ProjectParticipationMapper() as mapper:
            return mapper.find_all_person_by_project_id(id)

    def get_all_project_by_personid(self, id):
        with ProjectParticipationMapper() as mapper:
            return mapper.find_all_project_by_person_id(id)

    def remove_person_from_project(self, projectparticipation):
        with ProjectParticipationMapper() as mapper:
            return mapper.delete_projectparticipation(projectparticipation)

    # ---------- Project ----------

    def create_project(self, p):
        project = Project()
        project.set_start_date(p.get_start_date())
        project.set_end_date(p.get_end_date())
        project.set_name(p.get_name())

        with ProjectMapper() as mapper:
            return mapper.insert(project)

    def delete_project(self, id):
        with ProjectMapper() as mapper:
            mapper.delete(id)

    def edit_project(self, project):
        with ProjectMapper() as mapper:
            return mapper.update(project)

    def get_hierachy_by_project_id(self, projectid):

        with ProjectParticipationMapper() as mapper:
            project_list = []
            projects = mapper.find_all_project_by_person_id(projectid)

            for project in projects:
                project_dict = {}
                project_dict.update(Project.to_dict(project))

                with PhaseMapper() as mapper:
                    phases = mapper.find_all_by_projectid(project.get_id())
                    phase_list = []

                    for phase in phases:
                        phase_dict = {}
                        phase_dict.update(Phase.to_dict(phase))

                        with KanbanCardMapper() as mapper:
                            cards = mapper.find_all_by_phaseid(phase.get_id())
                            card_list = []

                            for card in cards:
                                card_dict = {}
                                card_dict.update(KanbanCard.to_dict(card))

                                with CommentMapper() as mapper:
                                    comments = mapper.find_all_by_cardid(card.get_id())
                                    comment_list = []

                                    for comment in comments:
                                        comment_dict = {}
                                        comment_dict.update(Comment.to_dict(comment))
                                        comment_list.append(comment_dict)

                                    card_dict.update({'comments': comment_list})
                                card_list.append(card_dict)
                            phase_dict.update({'kanbancards': card_list})
                        phase_list.append(phase_dict)
                    project_dict.update({'phases': phase_list})
                project_list.append(project_dict)

            return project_list



    # ---------- Phase ----------

    def create_phase(self, p):
        phase = Phase()
        phase.set_name(p.get_name())
        phase.set_projectid(p.get_projectid())

        with PhaseMapper() as mapper:
            return mapper.insert(phase)

    def delete_phase(self, phase):
        with PhaseMapper() as mapper:
            mapper.delete(phase)

    def edit_phase(self, phase):
        with PhaseMapper() as mapper:
            mapper.update(phase)

    def get_all_phase_by_projectid(self, id):
        with PhaseMapper() as mapper:
            return mapper.find_all_by_projectid(id)

    # ---------- Kanbancard ----------

    def create_kanbancard(self, card):
        kanbancard = KanbanCard()
        kanbancard.set_title(card.get_title())
        kanbancard.set_content(card.get_content())
        kanbancard.set_phaseid(card.get_phaseid())
        kanbancard.set_start_date(card.get_start_date())
        kanbancard.set_end_date(card.get_end_date())
        kanbancard.set_creator(card.get_creator())
        kanbancard.set_assigned_person(card.get_assigned_person())

        with KanbanCardMapper() as mapper:
            return mapper.insert(kanbancard)

    def edit_kanbancard(self, card):
        with KanbanCardMapper() as mapper:
            return mapper.update(card)

    def delete_kanbancard(self, id):
        with KanbanCardMapper() as mapper:
            return mapper.delete(id)

    def get_all_kanbancard_by_creator(self, id):
        with KanbanCardMapper() as mapper:
            return mapper.find_all_by_creator(id)

    def get_all_kanbancard_by_phaseid(self, id):
        with KanbanCardMapper() as mapper:
            return mapper.find_all_by_phaseid(id)

    def find_all_kanbancard_by_assigned_person(self, id):
        with KanbanCardMapper() as mapper:
            return mapper.find_all_by_assigned_person(id)

    def get_all_kanbancard_by_assigned_person(self, id):
        with KanbanCardMapper as mapper:
            return mapper.find_all_by_assigned_person(id)

    # ---------- Comment ----------

    def get_all_comment_by_cardid(self, id):
        with CommentMapper() as mapper:
            return mapper.find_all_by_cardid(id)

    def create_comment(self, comment):
        c = Comment()
        c.set_creator(comment.get_creator())
        c.set_content(comment.get_content())
        c.set_cardid(comment.get_cardid())
        c.set_creation_date(comment.get_creation_date())

        with CommentMapper() as mapper:
            return mapper.insert(c)

    def delete_comment(self, commentid):
        with CommentMapper() as mapper:
            mapper.delete(commentid)

    def edit_comment(self, comment):
        with CommentMapper() as mapper:
            mapper.update(comment)

    def get_all_comment_by_creator(self, creator):
        with CommentMapper() as mapper:
            mapper.find_by_creator(creator)

    # ---------- Statistik ----------





if (__name__ == "__main__"):
   adm = Administration()
   list = adm.get_hierachy_by_project_id(3)
   for l in list:
       print(l)





