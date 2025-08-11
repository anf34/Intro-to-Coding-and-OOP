class Song:
	def __init__(self, artist, album, name, dat):
		self.validate_input(artist, album, name, dat)
		self.artist = artist
		self.album = album
		self.name = name
		self.dat = dat

	def validate_input(self, artist, album, name, dat):
		self.validate_artist(artist)
		self.validate_album(album)
		self.validate_name(name)
		self.validate_dat(dat)

	def get_artist(self):
		return self.artist

	def get_album(self):
		return self.album

	def get_name(self):
		return self.name

	def get_dat(self):
		return self.dat

	def set_artist(self, artist):
		self.validate_artist(artist)
		self.artist = artist

	def set_album(self, album):
		self.validate_album(album)
		self.album = album

	def set_name(self, name):
		self.validate_name(name)
		self.name = name

	def set_dat(self, dat):
		self.validate_dat(dat)
		self.dat = dat

	def validate_artist(self, artist):
		if not (artist and isinstance(artist, str)):
			raise TypeError('Artist must be of type str and non empty.')

	def validate_album(self, album):
		if not (album and isinstance(album, str)):
			raise TypeError('Album must be of type str and non empty.')

	def validate_name(self, name):
		if not (name and isinstance(name, str)):
			raise TypeError('Name must be of type str and non empty.')

	def validate_dat(self, dat):
		if not (dat and isinstance(dat, str)):
			raise TypeError('Dat must be of type str and non empty.')

	def dummy(self):
		pass

	def dummy2(self):
		pass

