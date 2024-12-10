from django.db import models


# Create your models here.
class Module(models.Model):
    #Define choices for difficulty level
    BEGINNER='Beginner'
    INTERMEDIATE='Intermediate'
    ADVANCED='Advanced'

    DIFFICULTY_CHOICES =[
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]

    #Define choices for phase
    PHASE_1 = 'Phase 1'
    PHASE_2 = 'Phase 2'
    PHASE_3 = 'Phase 3'
    PHASE_4 = 'Phase 4'
    PHASE_5 = 'Phase 5'
    PHASE_6 = 'Phase 6'
    PHASE_7 = 'Phase 7'


    PHASE_CHOICES = [
        (PHASE_1,'PHASE 1'),
        (PHASE_2,'PHASE 2'),
        (PHASE_3,'PHASE 3'),
        (PHASE_4,'PHASE 4'),
        (PHASE_5,'PHASE 5'),
        (PHASE_6,'PHASE 6'),
    ]

    title = models.CharField(max_length=255)
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)


    def __str__(self):
        return self.title


      