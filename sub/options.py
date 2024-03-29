import getopt

class IncorrectUsageError(Exception):
    pass

class Option:
    def __init__(self, short, long, action, help_message, parameter=None):
        self.short = short
        self.long = long
        self.action = action
        self.help_message = help_message
        self.parameter = parameter

    def has_parameter(self):
        return self.parameter != None
    
    def short_formatted(self):
        return f"{self.short}:" if self.has_parameter() else self.short

    def long_formatted(self):
        return f"{self.long}=" if self.has_parameter() else self.long

    def to_string(self):
        return "\t%s  %s %s\n\t\t%s" % (
                f"-{self.short}",
                f"--{self.long}",
                f"[{self.parameter.upper()}]" if self.has_parameter() else "",
                self.help_message
            )

class Options:
    def __init__(self, options):
        self.__options = options
        self.__shorts = ''.join(list(opt.short_formatted() for opt in options))
        self.__longs = list(opt.long_formatted() for opt in options)

    def __find_option(self, arg):
        for option in self.__options:
            if (arg == f"-{option.short}" or arg == f"--{option.long}"):
                return option
        # TODO error handling for when no option found

    def get_option(self, argv):
        try:
            args, _ = getopt.getopt(
                argv[1:],
                self.__shorts,
                self.__longs
            )
        except getopt.error:
            raise IncorrectUsageError

        if (len(args) != 1):
            raise IncorrectUsageError()

        # TODO seems handled by getopt.error - check may be redundant
        chosen_option = self.__find_option(args[0][0])
        if (chosen_option.has_parameter() and len(args[0]) == 1):
            raise IncorrectUsageError()
        
        return chosen_option, args[0][1]
