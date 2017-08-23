from beprof.profile import Profile


class DepthProfile(Profile):

    def range(self, level):
        return self.width(level)

    def FWHM(self):
        return self.width(0.5)

    def distal_falloff(self):
        return self.x_at_y(0.1, True) - self.x_at_y(0.9, True)

    def normalize(self, allow_cast=True):
        """
        Scale and translate y to be in range(0,1)
        Normalize before calling other methods
        """
        self.y -= self.y.min()

        if allow_cast:
            self.y = self.y / self.y.max()
        else:
            self.y /= self.y.max()

