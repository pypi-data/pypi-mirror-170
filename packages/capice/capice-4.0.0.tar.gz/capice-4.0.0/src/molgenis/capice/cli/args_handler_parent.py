from abc import ABCMeta, abstractmethod

from molgenis.capice import __version__
from molgenis.capice.utilities import validate_list_length_one
from molgenis.capice.utilities.input_processor import InputProcessor
from molgenis.capice.validators.input_validator import InputValidator
from molgenis.capice.validators.version_validator import VersionValidator


class ArgsHandlerParent(metaclass=ABCMeta):
    """
    Parent class of all module specific argument parsers / handlers.
    """

    def __init__(self, parser):
        self.parser = parser
        self.input_validator = InputValidator()

    @property
    @abstractmethod
    def _extension(self):
        """
        Method to define what extension(s) are required for an input file for
        each module parser.
        """
        return ()

    @property
    @abstractmethod
    def _required_output_extensions(self):
        """
        Property to define what the output file extensions are required for each
        module parser.
        """
        return ""

    @property
    @abstractmethod
    def _empty_output_extension(self):
        """
        Property to define what extension an output file should get if no
        output file extension was given
        """
        return ""

    @abstractmethod
    def create(self):
        """
        Method to define what parser options should be available for the module.
        Use self.parser.add_argument() to add an argument to the subparser.
        """
        pass

    def handle(self):
        """
        Superclass handler to set the arguments set in create(). Also calls the
        parser to proceed with parsing the module specific arguments, validate
        them and run  the CAPICE code.
        """
        self.parser.set_defaults(func=self._handle_args)

    def _handle_args(self, args):
        """
        Superclass handle args to parse and validate the input and output
        arguments. Also parses the output filename.
        """
        version_validator = VersionValidator()
        try:
            version_validator.validate_capice_version(__version__)
        except ValueError as cm:
            self.parser.error(str(cm))
        input_path = self.validate_length_one(args.input, '-i/--input')
        try:
            self.input_validator.validate_input_path(input_path, extension=self._extension)
        except FileNotFoundError as cm:
            self.parser.error(str(cm))
        output_path = None
        if args.output is not None:
            output_path = self.validate_length_one(args.output, '-o/--output')
        try:
            processor = InputProcessor(
                input_path=input_path,
                output_path=output_path,
                force=args.force,
                default_extension=self._empty_output_extension
            )
        except FileExistsError as cm:
            self.parser.error(str(cm))
        output_filename = processor.get_output_filename()
        output_filename = self._handle_output_filename(output_filename)
        output_given = processor.get_output_given()
        output_path = processor.get_output_directory()
        try:
            self.input_validator.validate_output_path(output_path)
        except OSError as cm:
            self.parser.error(str(cm))
        self._handle_module_specific_args(input_path, output_path, output_filename, output_given,
                                          args)

    def validate_length_one(self, arg, arg_name):
        try:
            return validate_list_length_one(arg)
        except ValueError:
            self.parser.error(f'Invalid number of {arg_name} arguments.')

    @abstractmethod
    def _handle_module_specific_args(self, input_path, output_path, output_filename, output_given,
                                     args):
        """
        Method to be filled in by the module specific parsers. Should perform
        additional validation over args specific to the parser. Should then call
        the module to continue the module.
        """
        pass

    def _handle_output_filename(self, output_filename: str):
        """
        Method to validate that an output filename complies with the
        required output extension.
        """
        if '.' in output_filename and not output_filename.endswith(
                self._required_output_extensions):
            self.parser.error(
                f'Output file extension is incorrect. Expected output extension: '
                f'{self._required_output_extensions}'
            )
        else:
            return output_filename
