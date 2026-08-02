class CliError(Exception):
    pass

class LeetCodeError(CliError):
    pass

class ObjectNotFoundError(LeetCodeError):
    pass

class UnknownCommandError(CliError):
    pass

class PackageError(CliError):
    pass

class PackageAlreadyExistsError(PackageError):
    pass
