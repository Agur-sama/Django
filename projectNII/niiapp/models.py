from django.db import models

# class Employee(models.Model):
#     last_name = models.CharField(max_length=100, verbose_name='Фамилия')
#     first_name = models.CharField(max_length=100, verbose_name='Имя')
#     middle_name = models.CharField(max_length=100, blank=True, verbose_name='Отчество')
#     passport_series = models.CharField(max_length=10, verbose_name='Серия паспорта')
#     passport_number = models.CharField(max_length=20, verbose_name='Номер паспорта')
#     inn = models.CharField(max_length=12, verbose_name='ИНН')
#     birth_date = models.DateField(verbose_name='Дата рождения')
#     position = models.CharField(max_length=100, verbose_name='Должность')

#     def __str__(self):
#         return f"{self.last_name} {self.first_name}"

# class Project(models.Model):
#     title = models.CharField(max_length=200, verbose_name='Название проекта')
#     start_date = models.DateField(verbose_name='Дата начала')
#     end_date = models.DateField(verbose_name='Дата окончания')
#     budget = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Объем финансирования')

#     def __str__(self):
#         return self.title

# class Participation(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='participations')
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='participations')
#     role = models.CharField(max_length=100, verbose_name='Роль в проекте')

#     def __str__(self):
#         return f"{self.employee} в проекте {self.project} ({self.role})"


from django.utils.translation import gettext_lazy as _

class Employee(models.Model):
    last_name = models.CharField(max_length=100, verbose_name=_('Фамилия'))
    first_name = models.CharField(max_length=100, verbose_name=_('Имя'))
    middle_name = models.CharField(max_length=100, blank=True, verbose_name=_('Отчество'))
    passport_series = models.CharField(max_length=10, verbose_name=_('Серия паспорта'))
    passport_number = models.CharField(max_length=20, verbose_name=_('Номер паспорта'))
    inn = models.CharField(max_length=12, verbose_name=_('ИНН'))
    birth_date = models.DateField(verbose_name=_('Дата рождения'))
    position = models.CharField(max_length=100, verbose_name=_('Должность'))

    class Meta:
        verbose_name = _('Сотрудник')
        verbose_name_plural = _('Сотрудники')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Название проекта'))
    start_date = models.DateField(verbose_name=_('Дата начала'))
    end_date = models.DateField(verbose_name=_('Дата окончания'))
    budget = models.DecimalField(max_digits=15, decimal_places=2, verbose_name=_('Бюджет'))

    class Meta:
        verbose_name = _('Проект')
        verbose_name_plural = _('Проекты')

    def __str__(self):
        return self.title

class Participation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, 
                               verbose_name=_('Сотрудник'))
    project = models.ForeignKey(Project, on_delete=models.CASCADE, 
                              verbose_name=_('Проект'))
    role = models.CharField(max_length=100, verbose_name=_('Роль в проекте'))

    class Meta:
        verbose_name = _('Участие')
        verbose_name_plural = _('Участия в проектах')

    def __str__(self):
        return _("%(employee)s в проекте %(project)s") % {
            'employee': self.employee,
            'project': self.project
        }