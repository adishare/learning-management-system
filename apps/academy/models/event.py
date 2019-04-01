from django_undeletable.models import BaseModel
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Event(BaseModel):

  TYPE_CHOICE = (
    ('L', "Lat"),
    ('N', "Non-Lat"),
  )

  STATUS_CHOICE = (
    ('O', "On Going"),
    ('S', "Soon"),
    ('F', "Finish"),
  )

  CLASSIC_CHOICE = (
    ('C', "Classical"),
    ('O', "Online"),
  )

  event = models.CharField(max_length=50, verbose_name=_("Event"))
  learning_plan = models.ForeignKey("academy.LearningPlan", 
                    on_delete=models.CASCADE,
									  verbose_name=_("Learning Plan"))
  curriculum_title = models.ForeignKey("competency.Curriculum",
										 on_delete=models.CASCADE,
										 verbose_name=_("Curriculum"))
  location = models.ForeignKey("location.Location",
								 on_delete=models.CASCADE,
								 verbose_name=_("Location"))
  academy = models.ForeignKey("academy.Academy",
								on_delete=models.CASCADE,
								verbose_name=_("Academy"))
  start = models.DateField(verbose_name=_("Start"))
  type = models.CharField(max_length=2,
							choices=TYPE_CHOICE,
							verbose_name=_("Type"))
  classic_type =  models.CharField(max_length=2,
									 choices=CLASSIC_CHOICE)
  state =  models.CharField(max_length=3,
							  choices=STATUS_CHOICE,
							  default="S",
							  verbose_name=_("State"))
	
  def __str__(self):
    return self.event
	
  def set_on_going(self, user):
    from libs.log_utils import create_object_log
    if self.state == "S":
      self.state = "O"
      self.save()
      create_object_log(self, user, 'edit', message=_("Event on going now"))
			
  def set_finish(self, user):
    from libs.log_utils import create_object_log
    if self.state == "O":
      self.state = "F"
      self.save()
      create_object_log(self, user, 'edit', message=_("Event finish"))