from django.db import models

SocialMediaType = (
    ('facebook', 'facebook'),
    ('twitter', 'twitter'),
    ('instagram', 'instagram'),
    ('yelp', 'yelp'),
    ('linkedin', 'linkedin'),
    ('youtube', 'youtube'),
)

Price = (
    ('$', '$'),
    ('$$', '$$'),
    ('$$$', '$$$'),
    ('$$$$', '$$$$'),
)

Days = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)

Hours = (
    ('01:00', '01:00'),
    ('01:30', '01:30'),
    ('02:00', '02:00'),
    ('02:30', '02:30'),
    ('03:00', '03:00'),
    ('03:30', '03:30'),
    ('04:00', '04:00'),
    ('04:30', '04:30'),
    ('05:00', '05:00'),
    ('05:30', '05:30'),
    ('06:00', '06:00'),
    ('06:30', '06:30'),
    ('07:00', '07:00'),
    ('07:30', '07:30'),
    ('08:00', '08:00'),
    ('08:30', '08:30'),
    ('09:00', '09:00'),
    ('09:30', '09:30'),
    ('10:00', '10:00'),
    ('10:30', '10:30'),
    ('11:00', '11:00'),
    ('11:30', '11:30'),
    ('12:00', '12:00'),
    ('12:30', '12:30'),
    ('13:00', '13:00'),
    ('13:30', '13:30'),
    ('14:00', '14:00'),
    ('14:30', '14:30'),
    ('15:00', '15:00'),
    ('15:30', '15:30'),
    ('16:00', '16:00'),
    ('16:30', '16:30'),
    ('17:00', '17:00'),
    ('17:30', '17:30'),
    ('18:00', '18:00'),
    ('18:30', '18:30'),
    ('19:00', '19:00'),
    ('19:30', '19:30'),
    ('20:00', '20:00'),
    ('20:30', '20:30'),
    ('21:00', '21:00'),
    ('21:30', '21:30'),
    ('22:00', '22:00'),
    ('22:30', '22:30'),
    ('23:00', '23:00'),
    ('23:30', '23:30'),
    ('24:00', '24:00'),
    ('24:30', '24:30'),
)

State = (
    ('AL', 'AL'),
    ('AK', 'AK'),
    ('AZ', 'AZ'),
    ('AR', 'AR'),
    ('CA', 'CA'),
    ('CO', 'CO'),
    ('CT', 'CT'),
    ('DE', 'DE'),
    ('FL', 'FL'),
    ('GA', 'GA'),
    ('HI', 'HI'),
    ('ID', 'ID'),
    ('IL', 'IL'),
    ('IN', 'IN'),
    ('IA', 'IA'),
    ('KS', 'KS'),
    ('KY', 'KY'),
    ('LA', 'LA'),
    ('ME', 'ME'),
    ('MD', 'MD'),
    ('MA', 'MA'),
    ('MI', 'MI'),
    ('MN', 'MN'),
    ('MS', 'MS'),
    ('MO', 'MO'),
    ('MT', 'MT'),
    ('NE', 'NE'),
    ('NV', 'NV'),
    ('NH', 'NH'),
    ('NJ', 'NJ'),
    ('NM', 'NM'),
    ('NY', 'NY'),
    ('NC', 'NC'),
    ('ND', 'ND'),
    ('OH', 'OH'),
    ('OK', 'OK'),
    ('OR', 'OR'),
    ('PA', 'PA'),
    ('RI', 'RI'),
    ('SC', 'SC'),
    ('SD', 'SD'),
    ('TN', 'TN'),
    ('TX', 'TX'),
    ('UT', 'UT'),
    ('VT', 'VT'),
    ('VA', 'VA'),
    ('WA', 'WA'),
    ('WV', 'WV'),
    ('WI', 'WI'),
    ('WY', 'WY'),
)

BusinessType = (
    ('AccountingService', 'AccountingService'),
    ('AdultEntertainment', 'AdultEntertainment'),
    ('Apartment', 'Apartment'),
    ('AmusementPark', 'AmusementPark'),
    ('AnimalShelter', 'AnimalShelter'),
    ('ArchiveOrganization', 'ArchiveOrganization'),
    ('ArtGallery', 'ArtGallery'),
    ('Attorney', 'Attorney'),
    ('AutomotiveBusiness', 'AutomotiveBusiness'),
    ('AutoBodyShop', 'AutoBodyShop'),
    ('AutoDealer', 'AutoDealer'),
    ('AutoPartsStore', 'AutoPartsStore'),
    ('AutomatedTeller', 'AutomatedTeller'),
    ('AutoRental', 'AutoRental'),
    ('AutoRepair', 'AutoRepair'),
    ('AutoWash', 'AutoWash'),
    ('Bakery', 'Bakery'),
    ('BankOrCreditUnion', 'BankOrCreditUnion'),
    ('BarOrPub', 'BarOrPub'),
    ('BeautySalon', 'BeautySalon'),
    ('BedAndBreakfast', 'BedAndBreakfast'),
    ('Brewery', 'Brewery'),
    ('BowlingAlley', 'BowlingAlley'),
    ('CafeOrCoffeeShop', 'CafeOrCoffeeShop'),
    ('Campground', 'Campground'),
    ('Casino', 'Casino'),
    ('ChildCare', 'ChildCare'),
    ('ComedyClub', 'ComedyClub'),
    ('DaySpa', 'DaySpa'),
    ('Dentist', 'Dentist'),
    ('Dermatology', 'Dermatology'),
    ('Distillery', 'Distillery'),
    ('DryCleaningOrLaundry', 'DryCleaningOrLaundry'),
    ('EmergencyService', 'EmergencyService'),
    ('EmploymentAgency', 'EmploymentAgency'),
    ('EntertainmentBusiness', 'EntertainmentBusiness'),
    ('Electrician', 'Electrician'),
    ('FastFoodRestaurant', 'FastFoodRestaurant'),
    ('FireStation', 'FireStation'),
    ('FinancialService', 'FinancialService'),
    ('Florist', 'Florist'),
    ('FoodEstablishment', 'FoodEstablishment'),
    ('GasStation', 'GasStation'),
    ('GeneralContractor', 'GeneralContractor'),
    ('GolfCourse', 'GolfCourse'),
    ('GovernmentOffice', 'GovernmentOffice'),
    ('HairSalon', 'HairSalon'),
    ('HealthClub', 'HealthClub'),
    ('HealthAndBeautyBusiness', 'HealthAndBeautyBusiness'),
    ('Hospital', 'Hospital'),
    ('Hotel', 'Hotel'),
    ('HomeAndConstructionBusiness', 'HomeAndConstructionBusiness'),
    ('HousePainter', 'HousePainter'),
    ('HVACBusiness', 'HVACBusiness'),
    ('IceCreamShop', 'IceCreamShop'),
    ('InternetCafe', 'InternetCafe'),
    ('InsuranceAgency', 'InsuranceAgency'),
    ('LegalService', 'LegalService'),
    ('Library', 'Library'),
    ('Locksmith', 'Locksmith'),
    ('LodgingBusiness', 'LodgingBusiness'),
    ('MedicalBusiness', 'MedicalBusiness'),
    ('MedicalClinic', 'MedicalClinic'),
    ('Motel', 'Motel'),
    ('MotorcycleDealer', 'MotorcycleDealer'),
    ('MotorcycleRepair', 'MotorcycleRepair'),
    ('MovieTheater', 'MovieTheater'),
    ('MovingCompany', 'MovingCompany'),
    ('NailSalon', 'NailSalon'),
    ('NightClub', 'NightClub'),
    ('Pharmacy', 'Pharmacy'),
    ('Physician', 'Physician'),
    ('Plumber', 'Plumber'),
    ('ProfessionalService', 'ProfessionalService'),
    ('PoliceStation', 'PoliceStation'),
    ('PostOffice', 'PostOffice'),
    ('RadioStation', 'RadioStation'),
    ('Restaurant', 'Restaurant'),
    ('Resort', 'Resort'),
    ('RealEstateAgent', 'RealEstateAgent'),
    ('RoofingContractor', 'RoofingContractor'),
    ('SelfStorage', 'SelfStorage'),
    ('ShoppingCenter', 'ShoppingCenter'),
    ('SportsActivityLocation', 'SportsActivityLocation'),
    ('StadiumOrArena', 'StadiumOrArena'),
    ('Store', 'Store'),
    ('TattooParlor', 'TattooParlor'),
    ('TelevisionStation', 'TelevisionStation'),
    ('TouristInformationCenter', 'TouristInformationCenter'),
    ('TravelAgency', 'TravelAgency'),
    ('Winery', 'Winery'),
)

AssetType = (
    ('Services', 'Services'),
    ('Products', 'Products'),
)


class BusinessHours(models.Model):
    Day = models.CharField(choices=Days, max_length=50)
    Open = models.CharField(choices=Hours, max_length=50)
    Close = models.CharField(choices=Hours, max_length=50)
    BusinessId = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return self.Day

    class Meta():
        # ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Business Hour'
        verbose_name_plural = 'Business Hours'


class SocialMedia(models.Model):
    Link = models.URLField()
    LinkId = models.ForeignKey('Client', on_delete=models.CASCADE)
    Type = models.CharField(choices=SocialMediaType, max_length=150)

    def __str__(self):
        return self.Type

    class Meta():
        # ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Social Media Account'
        verbose_name_plural = 'Social Media Accounts'


class Client(models.Model):
    Type = models.CharField(choices=BusinessType, max_length=250)
    Name = models.CharField(max_length=300)
    Telephone = models.CharField(max_length=20)
    TelLink = models.CharField(max_length=20)
    Email = models.CharField(max_length=300)
    Website = models.URLField()
    SocialMedia = None
    Favicon = models.ImageField(upload_to='photos/client/%Y/')
    Logo = models.ImageField(upload_to='photos/client/%Y/')
    ServicesPhoto = models.ImageField(upload_to='photos/client/%Y/')
    Description = models.TextField()
    PriceRange = models.CharField(choices=Price, max_length=5)
    StreetAddress = models.CharField(max_length=400)
    City = models.CharField(max_length=350)
    State = models.CharField(choices=State, max_length=75)
    Zip = models.CharField(max_length=12)
    Latitude = models.CharField(max_length=100)
    Longitude = models.CharField(max_length=100)
    BusinessHours = None

    def __str__(self):
        return self.Name

    class Meta():
        # ordering = ('created',)
        get_latest_by = ('created',)
        verbose_name = 'Client Info'
        verbose_name_plural = 'Client Info'


class Asset(models.Model):
    Title = models.CharField(max_length=150)
    Description = models.CharField(max_length=250)
    Type = models.CharField(choices=AssetType, max_length=50)
    Published = models.BooleanField(default=False)

    def __str__(self):
        return self.Title

    class Meta():
        ordering = ('Type',)
        get_latest_by = ('Published',)
        verbose_name = 'Asset'
        verbose_name_plural = 'Assets'

    @property
    def get_items(self):
        return Item.objects.filter(Category=self.Category).filter(Published=True)


class Item(models.Model):
    Name = models.CharField(max_length=150)
    Description = models.TextField()
    Image = models.ImageField(upload_to='photos/assets/%Y/')
    Published = models.BooleanField(default=False)
    Category = models.ForeignKey('Asset', on_delete=models.CASCADE, related_name='Category')
    Price = models.CharField(max_length=25)

    def __str__(self):
        return self.Category.Type

    class Meta():
        ordering = ('Name',)
        get_latest_by = ('Published',)
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
