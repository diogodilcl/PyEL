import inspect
import re


class PreEL:
    def __init__(self, expression: str):
        self.expression = expression

    def __call__(self, original_func):
        decorator_self = self

        def decorated_function(*args, **kwargs):
            values = ExpressionLanguage.get_values_properties(original_func, *args, **kwargs)
            ExpressionLanguage.execute_expression(values, decorator_self.expression)
            return original_func(*args, **kwargs)

        return decorated_function


class PosEL:
    def __init__(self, expression: str):
        self.expression = expression

    def __call__(self, original_func):
        decorator_self = self

        def decorated_function(*args, **kwargs):
            return_value = original_func(*args, **kwargs)
            values = ExpressionLanguage.get_values_properties(original_func, *args, **kwargs)
            ExpressionLanguage.execute_expression(values, decorator_self.expression)
            return return_value

        return decorated_function


class ExpressionLanguage:

    @staticmethod
    def execute_expression(values, expression):
        expression = _process_args(values, expression)
        imports, to_execute = _generate_import(expression)

        exec(imports)
        eval(to_execute)

    @staticmethod
    def get_values_properties(original_func, *args, **kwargs):
        arguments = inspect.signature(original_func).parameters.keys()
        values = dict()
        for idx, val in enumerate(arguments):
            if kwargs.__contains__(val):
                values[val] = kwargs[val]
            else:
                values[val] = args[idx]
        return values


def _process_args(values, expression):
    matchs = list(re.finditer(r'(\#+\w+)', expression))
    for x in matchs:
        expression = expression.replace(x.group(1), '"{}"'.format(values[x.group(1)[1:]]))
    return expression


def _generate_import(value: str):
    paths = [str(match.group())[:-1] for match in list(re.finditer(r'(\w+\.)+', value))]
    methods = [match.group() for match in list(re.finditer(r'(\w+)(?=\()', value))]
    zip_list = zip(paths, methods)

    imports = ''.join(['from {} import {}; '.format(current[0], current[1]) for current in zip_list])

    to_execute = re.sub(r'(\w+\.)+', '', value)

    return imports, to_execute
