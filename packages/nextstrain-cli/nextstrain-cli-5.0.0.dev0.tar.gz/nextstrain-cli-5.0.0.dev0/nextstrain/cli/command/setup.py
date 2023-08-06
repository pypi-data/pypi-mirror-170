"""
Sets up a Nextstrain runtime for use with `nextstrain build`, `nextstrain
view`, etc.

Only the Conda runtime currently supports automated set up, but this command
may still be used with other runtimes to check an existing (manual) setup and
set the runtime as the default on success.

Exits with an error code if automated set up fails or if setup checks fail.
"""
from functools import partial
from shlex import quote as shquote
from textwrap import dedent

from .. import config, console
from ..util import colored, runner_name, runner_tests_ok, print_runner_tests
from ..types import Options
from ..runner import all_runners_by_name, configured_runner, default_runner # noqa: F401 (it's wrong; we use it in run())


def register_parser(subparser):
    parser = subparser.add_parser("setup", help = "Set up a runtime")

    parser.add_argument(
        "runner",
        help     = "The Nextstrain build environment (aka Nextstrain runtime) to set up. "
                   f"One of {{{', '.join(all_runners_by_name)}}}.",
        metavar  = "<runtime>",
        choices  = list(all_runners_by_name))

    parser.add_argument(
        "--dry-run",
        help   = "Don't actually set up anything, just show what would happen.",
        action = "store_true")

    parser.add_argument(
        "--force",
        help    = "Ignore existing setup, if any, and always start fresh.",
        action  = "store_true",
        default = False)

    parser.add_argument(
        "--set-default",
        help   = "Use the build environment (runtime) as the default if set up is successful.",
        action = "store_true")

    return parser


@console.auto_dry_run_indicator()
def run(opts: Options) -> int:
    global default_runner

    # opts.runner's "choices" above restricts it to valid keys; if it doesn't
    # that's a programming error and the user-facing exception for that will be
    # appropriate.
    runner = all_runners_by_name[opts.runner]

    heading = partial(colored, "bold")
    failure = partial(colored, "red")

    # Setup
    print(heading(f"Setting up {runner_name(runner)}…"))
    setup_ok = runner.setup(dry_run = opts.dry_run, force = opts.force)

    if setup_ok is None:
        print("Automated set up is not supported, but we'll check for a manual setup.")
    elif not setup_ok:
        print()
        print(failure("Set up failed!"))
        return 1

    # Test
    print()
    print(heading(f"Checking setup…"))

    if not opts.dry_run:
        tests = runner.test_setup()

        print_runner_tests(tests)

        if not runner_tests_ok(tests):
            print()
            print(failure("Checks failed!  Setup is unlikely to be fully functional."))
            return 1
    else:
        print("Skipping checks for dry run.")

    # Optionally set as default
    if opts.set_default:
        default_runner = runner
        print()
        print("Setting default environment to %s." % runner_name(default_runner))

        if not opts.dry_run:
            config.set("core", "runner", runner_name(default_runner))
            default_runner.set_default_config()

    # Warn if this isn't the default runner.
    if default_runner is not runner:
        print()
        if not configured_runner:
            print(f"Warning: No default environment is configured so {runner_name(default_runner)} will be used.")
        else:
            print(f"Note that your default environment is still {runner_name(default_runner)}.")
        print()
        print(dedent(f"""\
            You can use {runner_name(runner)} on an ad-hoc basis with commands like `nextstrain build`,
            `nextstrain view`, etc. by passing them the --{runner_name(runner)} option, e.g.:

                nextstrain build --{runner_name(runner)} …

            If you want to use {runner_name(runner)} by default instead, re-run this
            command with the --set-default option, e.g.:

                nextstrain setup --set-default {shquote(opts.runner)}\
            """))

    print()
    print("All good!  Set up of", runner_name(runner), "complete.")
    return 0
