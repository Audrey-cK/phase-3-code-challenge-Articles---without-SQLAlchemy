class Band:
    all=[]
    def __init__(self, name, hometown):
        if isinstance(hometown, str) and len(hometown):
            self._hometown = hometown
        else:
            raise ValueError("Hometown must be a string")
        self.name = name
        Band.all.append(self) 
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a string.")

    @property
    def hometown(self):
        return self._hometown


    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.band == self]

    def venues(self):
        venues = list(set(concert.venue for concert in self.concerts()))
        return venues if venues else None

    def play_in_venue(self, venue, date):
        if not isinstance(venue, Venue):
            raise ValueError("venue must be of type Venue")
        return Concert(date, self, venue)

    def all_introductions(self):
        return [
            concert.introduction() for concert in self.concerts() if concert.introduction()
        ]


class Concert:
    all_concerts = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all_concerts.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a string.")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, band):
        if not isinstance(band, Band):
            raise TypeError("band must be of type Band")
        self._band = band

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("venue must be an instance of Venue.")

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all=[]
    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a string.")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a string.")

    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.venue == self]

    def bands(self):
        return list({concert.band for concert in self.concerts()})
    
    def concert_on(self, date):
        for concert in self.concerts():
            if concert.date == date:
                return concert
        return None