"""class Time:
    def __init__(self):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        self.__period = ""

    #def get_hours(self):
    #    return self.__hours
    
    def get_minutes(self):
        return self.__minutes

    def get_seconds(self):
        return self.__seconds

    #def set_hours(self, val):
    #    if val < 0:
    #        self.__hours = 0
    #    elif val > 23:
    #        self.__hours = 23
    #    else:
    #        self.__hours = val

    def set_minutes(self, val):
        if val < 0:
            self.__minutes = 0
        elif val > 59:
            self.__minutes = 59
        else:
            self.__minutes = val

    def set_seconds(self, val):
        if val < 0:
            self.__seconds = 0
        elif val > 59:
            self.__seconds = 59
        else:
            self.__seconds = val

    @property
    def hours_simple(self):
        return self.__hours

    @hours_simple.setter
    def hours_simple(self, hour):
        if hour > 12:
            self.__hours = hour - 12
        elif hour < 0:
            self.__hours = 0
        else:
            self.__hours = hour

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self, hour):
        if hour >= 12:
            self.__period = "PM"
        else:
            self.__period = "AM"


    #hours = property(get_hours, set_hours)
    minutes = property(get_minutes, set_minutes)
    seconds = property(get_seconds, set_seconds)
    hour = (hours_simple)


def main():
    time = Time()
    time.hour = int(input("Enter an hour: "))
    time.minutes = int(input("Enter a minute: "))
    time.seconds = int(input("Enter a second: "))

    #time.set_hours(hours)
    #time.set_minutes(minutes)
    #time.set_seconds(seconds)

    print(f'hours: {time.hour}')
    print(f'minutes: {time.minutes}')
    print(f'seconds: {time.seconds}')
    print(time.period)


if __name__ == '__main__':
    main()
    """

class Time:
    def __init__(self):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        self.__period = ''

    # def get_hours(self):
    #     return self.__hours
    #
    # def set_hours(self, hours):
    #     if hours > 23:
    #         self.__hours = 23
    #     elif hours < 0:
    #         self.__hours = 0
    #     else:
    #         self.__hours = hours

    def get_minutes(self):
        return self.__minutes

    def set_minutes(self, minutes):
        if minutes > 59:
            self.__minutes = 59
        elif minutes < 0:
            self.__minutes = 0
        else:
            self.__minutes = minutes

    def get_seconds(self):
        return self.__seconds

    def set_seconds(self, seconds):
        if seconds > 59:
            self.__seconds = 59
        elif seconds < 0:
            self.__seconds = 0
        else:
            self.__seconds = seconds

    @property
    def hours_simple(self):
        return self.__hours

    @hours_simple.setter
    def hours_simple(self, hour):
        if hour > 12:
            self.__hours = hour - 12
        elif self.__hours < 0:
            self.__hours = 0
        else:
            self.__hours = hour

    @property
    def period(self):
        return self.__period

    @period.setter
    def period(self):
        if self.__hours > 12:
            self.__period = 'PM'
        else:
            self.__period = 'AM'

    # hours = property(get_hours, set_hours)
    minutes = property(get_minutes, set_minutes)
    seconds = property(get_seconds, set_seconds)
    hour = hours_simple
    format_time = period


def main():
    time = Time()
    time.hour = int(input("Enter an hour: "))
    time.minutes = int(input("Enter an minutes: "))
    time.seconds = int(input("Enter an seconds: "))
    time.hour
    time.period
    # print(f'hours: {time.hours}')
    print(f'hour "simple": {time.hour}')
    print(f'hour period: {time.period}')
    print(f'minutes: {time.minutes}')
    print(f'seconds: {time.seconds}')


if __name__ == '__main__':
    main()