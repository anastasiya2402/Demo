from Demonstration.Base import BaseUIEnvironment
from datetime import datetime


def before_feature(context, feature):
    # Parent inheritance
    BaseUIEnvironment.before_feature(context, feature)

    context.url = 'http://myut.utoledo.edu/'

    # store session id
    context.session = datetime.now().strftime('%d%B_%H_%M.%S')


def after_feature(context, feature):
    # Parent inheritance
    BaseUIEnvironment.after_feature(context, feature)


def before_scenario(context, scenario):
    BaseUIEnvironment.before_scenario(context, scenario)


def after_scenario(context, scenario):
    BaseUIEnvironment.after_scenario(context, scenario)


