class Television:

    MIN_VOLUME: int = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 0
    MAX_CHANNEL = 10

    def __init__(self):
        self.__status = False
        self.__channel = 0
        self.__volume = 0
        self.__muted = False
        self.__favoriteChannel = 1
        self.__favoriteVolume = 5

    def power(self):
        self.__status = not self.__status

    def channel_up(self):
        if self.__status:
            self.__channel += 1
            if self.__channel > self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status:
            self.__channel -= 1
            if self.__channel < self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL

    def channel(self, channel):
        if self.__status:
            if channel >= self.MIN_CHANNEL and channel <= self.MAX_CHANNEL:
                self.__channel = channel
    def mute(self):
        if self.__status:
            self.__muted = not self.__muted

    def volume(self, volume):
        if self.__status:
            if volume >= self.MIN_VOLUME and volume <= self.MAX_VOLUME:
                self.__volume = volume
    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.mute()
            self.__volume += 1
            if self.__volume > self.MAX_VOLUME:
                self.__volume = self.MAX_VOLUME

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.mute()
            self.__volume -= 1
            if self.__volume < self.MIN_VOLUME:
                self.__volume = self.MIN_VOLUME

    def favorite(self):
        if self.__status:
            self.__channel = self.__favoriteChannel
            self.__volume = self.__favoriteVolume
    def favorite_set(self):
        if self.__status:
            self.__favoriteChannel = self.__channel
            self.__favoriteVolume = self.__volume

    def __str__(self):
        if self.__muted:
            return f"TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"TV status: Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
