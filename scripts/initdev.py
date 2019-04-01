import sh
import glob
import os
import datetime
from django.conf import settings
from django.core.management import call_command
from django.contrib.auth import get_user_model
from human_resource.models.division import Division
from human_resource.models.employee import Employee
from human_resource.models.employee_grade import EmployeeGrade
from human_resource.models.position import Position
from human_resource.models.workplace import Workplace
from human_resource.models.participant import Participant
from competency.models.competency import Competency
from competency.models.competency_requirement import CompetencyRequirement
from competency.models.curriculum import Curriculum
from competency.models.proficiency import Proficiency
from competency.models.employee_competency import EmployeeCompetency
from location.models.city import City
from location.models.building import Building    
from location.models.room import Room
from location.models.location import Location
from location.models.company import Company
from academy.models.academy import Academy
from academy.models.partner import Partner
from academy.models.learning_plan import LearningPlan
from academy.models.learning_activity import LearningActivity
from academy.models.strategic_plan import StrategicPlan, StrategicPlanField
from academy.models.content_creator import ContentCreator
from academy.models.event import Event
from academy.models.event_plan import EventPlan
from academy.models.participant_event import ParticipantEvent
from account.models import Role
from corporate.models.learning_focus import LearningFocus
from content.models.article import ArticleCategory, Article
from content.models.quiz import QuizQuestion, ParticipantAnswer
from feedback.models.feedback import Testimonial
from feedback.models.feedback import Questionnaire
from feedback.models.feedback import QuestionnaireAnswer
from feedback.models.feedback import TestimonialAnswer
from feedback.models.feedback import TestimonialCategory
from feedback.models.feedback import QuestionnaireCategory
from forum.models.forum import Forum
from forum.models.thread import Thread, ThreadTag, Comment
from attachment.models.attachment import Attachment
from notification.models.notification import Notification


User = get_user_model()


def run():
    company_code = "1000"
    company_name = "Telkom Indonesia"
    db_name = settings.DATABASES['default']['NAME']
    if "postgres" in settings.DATABASES['default']['ENGINE']:
        import psycopg2
        try:
            psycopg2.connect("dbname=%s" % db_name)
            print("Deleting DB ...", end="")
            sh.dropdb(db_name)
            print("Done")
        except psycopg2.OperationalError:
            pass
    else:
        if os.path.isfile(db_name):
            os.unlink(db_name)
    print("Done")
    print("Creating DB ...", end="")
    if "postgres" in settings.DATABASES['default']['ENGINE']:
        sh.createdb(db_name)
    print("Done")
    call_command("migrate")
    
    print("Create Company")
    company = Company.objects.create(
        code=company_code,
        company_name=company_name,
        type= "P",
    )
    print("Create Role")
    role_student = Role.objects.create(company=company,
                                       name="Student",
                                       code='student',
                                       landing_url_name="landing-student-index")
    content_creator = Role.objects.create(company=company,
                                          name="Content Creator",
                                          code='content_creator',
                                          landing_url_name="landing-content-creator-index") 
    strategic_plan = Role.objects.create(company=company,
                                          name="Plan Manager",
                                          code='strategic_plan',
                                         landing_url_name="landing-strategic-plan-index")
    curriculum = Role.objects.create(company=company,
                                          name="Curriculum",
                                          code='curriculum',
                                          landing_url_name="landing-curriculum-index")
    event_manager = Role.objects.create(company=company,
                                          name="Event Manager",
                                          code='event_manager',
                                          landing_url_name="landing-event-manager-index")
    expert = Role.objects.create(company=company,
                                          name="Expert",
                                          code='expert',
                                          landing_url_name="landing-expert-index") 
    mentor = Role.objects.create(company=company,
                                          name="Mentor",
                                          code='mentor',
                                          landing_url_name="landing-mentor-index"
                                          )
    
    print("Create superuser")
    admin = User.objects.create_superuser(username="admin",
                                          password="admin",
                                          email="admin@admin.com",
                                          full_name="Admin Syalala")
    print("Create Student Dummy")
    
    student = User.objects.create_superuser(username="student",
                                    password="student",
                                    email="student@student.com",
                                    full_name="Andre Taulany")

    admin.role.add(role_student)
    admin.role.add(content_creator)
    admin.role.add(strategic_plan)
    admin.role.add(curriculum)
    admin.role.add(event_manager)
    admin.role.add(expert)
    admin.role.add(mentor)

    student.role.add(role_student)


    print("Create Sample Data ..")

    

    division = Division.objects.create(
        company = company,
        code = "10001",
        name = 'Information Technology'
    )

    grade = EmployeeGrade.objects.create(
        company = company,
        title = "Expert",
        description = "Expert in anything."
    )

    position = Position.objects.create(
        company = company,
        code = "IT-ENG",
        title = 'Software Engineer'
    )

    Workplace.objects.create(
        company = company,
        division = division,
        code = "CORP-G",
        name = "Telkom Corporate University",
    )
    
    parent_competency = Competency.objects.create(
        company = company,
        title = 'Data Science'
    )

    competency = Competency.objects.create(
        company = company,
        parent = parent_competency,
        title = "Python Programming Language"
    )

    proficiency = Proficiency.objects.create(
        company = company,
        level = "4"
    )

    city = City.objects.create(
        company = company,
        code = "BDG",
        name = "Bandung"
    )

    location = Location.objects.create(
        company = company,
        city = city,
        address = "Jl. Suka-Suka",
        code = "1221",
        name = "Corporate University"
    )

    building = Building.objects.create(
        company = company,
        city = city,
        location = location,
        address = "Jl. Suka - Suka",
        code = "1331",
        name = "Gedung G"
    )

    Room.objects.create(
        company = company,
        city = city,
        building = building,
        code = "222",
        name = "Room D"
    )
    
    academy = Academy.objects.create(
        company = company,
        code = "CORP",
        name = 'Corporate Academy'
    )
    
    academy.division.add(division)

    Partner.objects.create(
        company = company,
        code = "P0001",
        name = "ARM SOlusi",
        type = "V"
    )
    
    employee = Employee.objects.create(
        user = admin,
        company = company,
        location = location,
        division = division,
        position = position,
        ic_number = "7336813518",
        name = "Nikola Tesla",
        email = "nikola@tesla.com",
        address = "Bandung",
        phone = "08888899999",
        grade = grade
    )

    competency_requirement = CompetencyRequirement.objects.create(
        company = company,
        competency = competency,
        proficiency = proficiency,
        position = position
    )

    employee_competency = EmployeeCompetency.objects.create(
        company = company,
        competency = competency,
        employee = employee,
        proficiency = proficiency
    )

    LearningFocus.objects.create(
        unit_business = 'DSC',
        academy = academy,
        year = 2017,
        org_competence = 'Competency Terkait',
        objective = 'Ini Objective',
        staff = 'Staff',
        supervisor = 'Analize new service',
        manager = 'Review The Posibility',
        senior_manager = 'Evaluate Program',
        top_management = 'Disseminate initiative'
    )

    article_caregory = ArticleCategory.objects.create(name="Programming")
    ArticleCategory.objects.create(name="Economy")
    

    articledua = Article(
        title = 'How cat Jumping',
        author = admin,
        competency = competency,
        proficiency = proficiency,
        body = 'Most domestic cats can typically jump up to 6 times their own height. This means a healthy, agile one foot tall cat can be expected to jump up to six feet! ... Thanks to a flexible spine and strong leg ',
    )
    articledua.save()

    article = Article(
        title = 'Uses of Python in Real World',
        author = admin,
        competency = competency,
        proficiency = proficiency,
        body = 'Python is interpreted object-oriented language. It is also referred to as a high-level programming language. It is designed by Guido Van Rossum. It was initially released in the year ',
    )
    article.save()
    article.category.add(article_caregory)



    quiz_question = QuizQuestion.objects.create(
        title = 'Basic Knowledge',
        question = 'What is document format for python file',
        option_a = '.py',
        option_b = '.js', 
        option_c = '.ppt', 
        option_d = '.pdf', 
        correct_option = 'A' ,
    )
    quiz_question.competency.add(competency)
    quiz_question.proficiency.add(proficiency)

    quiz_question2 = QuizQuestion.objects.create(
        title = 'Random',
        question = 'is cat killable?',
        option_a = 'maybe',
        option_b = 'yes', 
        option_c = 'absolutely', 
        option_d = 'nope', 
        correct_option = 'D' ,
    )
    quiz_question2.competency.add(competency)
    quiz_question2.proficiency.add(proficiency)


    strategic_plan = StrategicPlan.objects.create(
        strategic_initiative = 'Digital Mindset',
    )
  
    learning_plan = LearningPlan.objects.create(
        title = 'Web Developer Training',
        location = location,
        date = '1990-01-01',
        budget = 10000000,
        competency_issue = strategic_plan,
        participant = '30',
        batch = '1'
    )

    learning_act_1 = LearningActivity.objects.create(
        code = '001',
        title = 'Reading',
        description = 'Reading is the complex cognitive process of decoding symbols to derive meaning. It is a form of language processing. Success in this process is measured as',
        cycle = '1',
        link = 'www.telkomcorpu.com',
    )
    learning_act_1.articles.add(article)
    learning_act_1.articles.add(articledua)

    learning_act_2 = LearningActivity.objects.create(
        code = '002',
        title = 'E-Learning',
        description = 'utilizing electronic technologies to access educational curriculum outside of a traditional classroom',
        cycle = '2',
        link = 'www.elearning.com',
    )
    
    learning_act_3 = LearningActivity.objects.create(
        code = '003',
        title = 'Class Meeting',
        description = 'where the only shareholders in attendance that can vote are those that hold a particular class of shares',
        cycle = '3',
        link = 'www.telkomcorpu.com',
    )
    learning_act_3.quiz.add(quiz_question)
    learning_act_3.quiz.add(quiz_question2)
    
    learning_act_4 = LearningActivity.objects.create(
        code = '004',
        title = 'Assignment',
        description ='a task given to students by their teachers to be completed out of the class time',
        cycle = '4',
        link = 'www.telkomcorpu.com',
    )
    
    learning_act_5 = LearningActivity.objects.create(
        code = '005',
        title = 'Forum Disscussion',
        description = 'Join Forum to share',
        cycle = '5',
        link = 'www.telkomcorpu.com',
    )
    
    
    learning_act_6 = LearningActivity.objects.create(
        code = '006',
        title = 'Wrinte an Artikel',
        description = 'Be productive',
        cycle = '6',
        link = 'www.telkomcorpu.com',
    )

    curriculum = Curriculum.objects.create(
        company = company,
        title = 'Python for data Science',
        competency_goal = competency,
        issue = strategic_plan,
        capacity = 50,
        claim = 'N'
    )

    curriculum.learning_activity.add(learning_act_1)
    curriculum.learning_activity.add(learning_act_2)
    curriculum.learning_activity.add(learning_act_3)
    curriculum.learning_activity.add(learning_act_4)
    curriculum.learning_activity.add(learning_act_5)
    curriculum.learning_activity.add(learning_act_6)
    
    ContentCreator.objects.create(
        event = 'Bangmat DL Prime',
        academy = academy,
        start = datetime.date.today(),
        end = datetime.date.today(),
        type = 'Non-Lat',
        learning_activity = 'Bangmat DL Prime',
        resource = 'OK',
        status = 'On Going',
        class_type = 'ILC'
    )
    participant = Participant.objects.create(
        nik = "1106257",
        name = "Tegar",
        age = "24",
        address = "Jl. Lembang",
       telephone_number = "08939292929",
    )
    event = Event.objects.create(
        event = 'Bangmat DL Prime',
        learning_plan = learning_plan,
        curriculum_title = curriculum,
        location = location,
        academy = academy,
        start = datetime.date.today(),
        type = 'Non-Lat',
        classic_type = 'ILC',

    )
    EventPlan.objects.create(
        learning_plan = learning_plan,
        curriculum_title = curriculum,
        mentor_request = 'Sent',
        vendor_request = 'Sent',
        start = datetime.date.today(),
        end = datetime.date.today(),
    )
    testimony_category = TestimonialCategory.objects.create(name="Course")
    testimony_category = TestimonialCategory.objects.create(name="Facility")
    testimony_category = TestimonialCategory.objects.create(name="Management")

    questionnaire_category = QuestionnaireCategory.objects.create(name="Behavior")
    questionnaire_category = QuestionnaireCategory.objects.create(name="Performance")

    testimonial = Testimonial.objects.create(
        name = 'Bangmat DL Prime',
        event = event,
        category = testimony_category,
        question = "Bagaimana cara mengajar disana?"
    )

    questionnaire = Questionnaire.objects.create(
        code = 'Q1',
        event = event,
        category = questionnaire_category,
        question = "Apakah perilaku peserta menjadi lebih sopan?",
    )

    QuestionnaireAnswer.objects.create(
        question = questionnaire,
        answer = "Peserta menjadi sangat sopan pada setiap orang."
    )

    TestimonialAnswer.objects.create(
        question = testimonial,
        answer = "Sangat mudah dipahami."
    )

    ParticipantEvent.objects.create(
        participant_name = participant,
        event_name = event,
        state = False,
    )

    StrategicPlanField.objects.create(
        name="Strategic Initiative",
        required=True        
    )
    StrategicPlanField.objects.create(
        name="Bussines Issue",
        required=True        
    )
    StrategicPlanField.objects.create(
        name="Performance Issue",
        required=True        
    )
    StrategicPlanField.objects.create(
        name="Competency Issue",
        required=True        
    )

    forum = Forum.objects.create(
        name = 'Python Community',
        description = 'Forum diskusi seputar python',        
    )
    forum.members.add(admin)
    forum.competency.add(competency)
    forum.proficiency.add(proficiency)
    
    learning_act_5.forum.add(forum)

    thread_tag = ThreadTag.objects.create(
        name = 'Framework'
    )

    thread = Thread.objects.create(
        title = 'Django Framework - Python web dev',
        author = admin,
        body = 'Django is a Python-based free and open-source web framework, which follows the model-view-template architectural pattern. ',
        forum = forum
    )
    thread.tag.add(thread_tag)

    Comment.objects.create(
        author = admin,
        thread = thread,
        body = 'Gimana cara install django di iphone X ?'
    )

    Notification.objects.create(
        title = 'Your first Notification!',
        type = 'system',
        message = 'Welcome to the LMS CORPU APPS, hope you enjoy this.',
        sender = admin,
        receiver = admin,
        read = False,
        url = 'localhost/landing'
    )
