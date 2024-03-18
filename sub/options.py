import getopt

class TooManyArgsError(Exception):
    pass

class Option:
    def __init__(self, short, long, action, has_parameter=False):
        self.short = short
        self.long = long
        self.action = action
        self.has_parameter = has_parameter
    
    def short_formatted(self):
        return f"{self.short}:" if self.has_parameter else self.short

    def long_formatted(self):
        return f"{self.long}=" if self.has_parameter else self.long

class Options:
    def __init__(self, options):
        self.__options = options
        self.__shorts = ''.join(list(opt.short_formatted() for opt in options))
        self.__longs = list(opt.long_formatted() for opt in options)

    def __find_option(self, arg):
        for option in self.__options:
            if (arg == f"-{option.short}" or arg == f"--{option.long}"):
                return option
        # TODO error handling

    def get_option(self, argv):
        try:
            args, rest = getopt.getopt(
                argv[1:],
                self.__shorts,
                self.__longs
            )

            if (len(args) != 1):
                raise TooManyArgsError()
            
            return self.__find_option(args[0][0]), args[0][1]
        except TooManyArgsError:
            print("Too many Args")
        except getopt.error as err:
            print(str(err))
