import os
import urllib3
import behave
from datetime import datetime
from jinja2 import Template
from Tables_and_Dictionaries import BehaveSupport

urllib3.disable_warnings()


def service_under_test(feature):
    path_list = os.path.split(feature.location.dirname())
    return path_list[-1]


def before_all(context):
    def __run(self, context):
        args = []
        kwargs = {}
        for arg in self.arguments:
            if arg.name is not None:
                kwargs[arg.name] = Template(arg.value).render(context=context) \
                    if isinstance(arg.value, str) \
                    else arg.value
            else:
                args.append(arg.value)

        with context.use_with_user_mode():
            self.func(context, *args, **kwargs)

    setattr(behave.matchers.Match, 'run', __run)


def before_feature(context, feature):
    print(feature.name)
    context.session = datetime.now().strftime('%d%B_%H_%M.%S')

    # make folder (Service under test) name be accessible feature wide
    context.test_application = service_under_test(feature)
    os.environ['TEST_APPLICATION'] = context.test_application
    # Set context.env based on OS env
    context.ENVIRONMENT = getattr(context, 'ENVIRONMENT', None) or os.getenv('ENVIRONMENT', 'qa')
    # Set context.env based on feature tag
    env_from_tag = [tag.split("environment=")[1] for tag in feature.tags if "environment=" in tag]
    if env_from_tag:
        context.ENVIRONMENT = env_from_tag[0]
    print(f"Executing tests in '{context.ENVIRONMENT}' environment")

    if "skip" in feature.tags:
        feature.skip("Marked with @skip")
        return


def before_scenario(context, scenario):
    """Some tags explanation:

    stay     - with browser reusing to stay on the same page after scenario
    home     - with browser reusing to close all the tabs but first after scenario
    home_out - with browser reusing to drop session after scenario
    """
    print(scenario.name)

    if any([t in scenario.tags for t in ('no_background', 'stay', 'home', 'home_out',)]):
        scenario.background = None
    if hasattr(context, "browser"):
        if any([t in scenario.tags for t in ('home', 'home_out')]) and len(context.browser.window_handles) > 1:
            close_all_tabs_but_first(context)

    if "run_background_once" in context.feature.tags:
        if hasattr(context, "background_executed"):
            scenario.background = None
        else:
            context.background_executed = True
            BehaveSupport.context_variable_to_custom_layer(context, "background_executed", True)

    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return
    # handle tags like @env:qa, to only execute in the specified env
    allowed_envs = [tag.split(':')[1].lower() for tag in scenario.effective_tags if "env:" in tag]
    if allowed_envs and context.ENVIRONMENT.lower() not in allowed_envs:
        scenario.skip(f"Scenario marked for execution only in {allowed_envs} environments;"
                      f" current env: {context.ENVIRONMENT}")
        return


def before_step(context, step):
    print(Template(step.name).render(context=context))

    # render step.text and step.table with jinja2 template engine
    if step.text:
        step.text = Template(step.text).render(context=context)

    if step.table:
        for row in step.table.rows:
            for i, cell in enumerate(row.cells):
                row.cells[i] = Template(cell).render(context=context) if isinstance(cell, str) else cell


def after_step(context, step):
    print(Template(step.name).render(context=context), '\t', step.status)
    bug_links = [t for t in context.scenario.effective_tags if t.startswith('bug')]
    if step.status == 'failed' and bug_links:
        refs = ' '.join([b.lstrip('bug_') for b in bug_links])
        reason = step.error_message
        step.error_message = f"{refs}:\n\n{reason}"


def after_scenario(context, scenario):
    print(scenario.name, '\t', scenario.status)

def after_feature(context, feature):
    print(feature.name, '\t', feature.status)


def close_all_tabs_but_first(context):
    while len(context.browser.window_handles) > 1:
        context.browser.close()
        context.browser.switch_to.window(context.browser.window_handles[-1])