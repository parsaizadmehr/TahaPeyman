from django.db import models
from django.contrib.auth.models import User


class Individual(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=45, verbose_name='نام')
    surname = models.CharField(max_length=45, verbose_name='نام خانوادگی')
    gender = models.CharField(max_length=10, verbose_name='جنسیت')
    father_name = models.CharField(max_length=45, verbose_name='نام پدر')
    feasibility_phone = models.CharField(max_length=20, verbose_name='تلفن امکان سنجی')
    nationality = models.CharField(max_length=10, verbose_name='ملیت')
    id_number = models.CharField(max_length=30, verbose_name='شماره شناسه هویتی')
    birth_certificate_number = models.CharField(max_length=30, verbose_name='شماره شناسنامه')
    ownership_type = models.CharField(max_length=10, verbose_name='نوع مالکیت')
    line_owner_name = models.CharField(max_length=45, verbose_name='نام مالک خط')
    mobile_phone = models.CharField(max_length=20, verbose_name='تلفن همراه')
    email = models.EmailField(max_length=30, verbose_name='پست الکترونیک')
    postal_code = models.CharField(max_length=30, verbose_name='کد پستی')
    usage_type = models.CharField(max_length=20, verbose_name='نوع کاربری')
    educational_degree = models.CharField(max_length=45, verbose_name='مدرک تحصیلی')
    subscriber_type = models.CharField(max_length=20, verbose_name='نوع مشترک')
    customer_group = models.CharField(max_length=20, verbose_name='گروه مشتری')
    birth_date = models.DateField(verbose_name='تاریخ تولد')
    selection_date = models.DateField(verbose_name='انتخاب تاریخ')
    last_street = models.CharField(max_length=45, verbose_name='معبر آخر')
    plate_number = models.CharField(max_length=10, verbose_name='شماره پلاک')
    address = models.CharField(max_length=50, verbose_name='آدرس')

    class Meta:
        db_table = 'individual'
        verbose_name = 'فرد'
        verbose_name_plural = 'افراد'

    def __str__(self):
        return f'{self.name} {self.surname}'

class Legal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='کاربر')
    company_name = models.CharField(max_length=50, verbose_name='نام شرکت')
    representative_name = models.CharField(max_length=20, verbose_name='نام نماینده/مدیرعامل')
    representative_surname = models.CharField(max_length=40, verbose_name='نام خانوادگی نماینده/مدیرعامل')
    representative_nationality = models.CharField(max_length=15, verbose_name='ملیت نماینده/مدیرعامل')
    id_type = models.CharField(max_length=30, verbose_name='نوع شناسه هویتی')
    representative_birth_certificate_number = models.CharField(max_length=45, verbose_name='شماره شناسنامه نماینده')
    representative_id_number = models.CharField(max_length=45, verbose_name='شماره شناسه هویتی نماینده')
    feasibility_phone = models.CharField(max_length=20, verbose_name='تلفن امکان سنجی')
    ownership_type = models.CharField(max_length=10, verbose_name='نوع مالکیت')
    company_national_id = models.CharField(max_length=20, verbose_name='شناسه ملی شرکت')
    registration_number = models.CharField(max_length=20, verbose_name='شماره ثبت')
    economic_code = models.CharField(max_length=20, verbose_name='کد اقتصادی')
    company_type = models.CharField(max_length=10, verbose_name='نوع شرکت')
    mobile_phone = models.CharField(max_length=20, verbose_name='تلفن همراه')
    email = models.EmailField(max_length=45, verbose_name='پست الکترونیک')
    postal_code = models.CharField(max_length=30, verbose_name='کد پستی')
    usage_type = models.CharField(max_length=20, verbose_name='نوع کاربری')
    representative_educational_degree = models.CharField(max_length=45, verbose_name='مدرک تحصیلی نماینده/مدیرعامل')
    subscriber_type = models.CharField(max_length=20, verbose_name='نوع مشترک')
    customer_group = models.CharField(max_length=20, verbose_name='گروه مشتری')
    establishment_date = models.CharField(max_length=10, verbose_name='تاریخ تاسیس')
    representative_birth_date = models.CharField(max_length=10, verbose_name='تاریخ تولد نماینده/مدیرعامل')
    plate_number = models.CharField(max_length=5, verbose_name='شماره پلاک')

    class Meta:
        db_table = 'legal'
        verbose_name = 'مشتری حقوقی'
        verbose_name_plural = 'مشتریان حقوقی'

    def __str__(self):
        return self.company_name

