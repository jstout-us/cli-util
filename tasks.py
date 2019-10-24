import os

from invoke import Collection
from invoke import task
from invoke import exceptions

from js_invoke.scm import SCM


ns = Collection(SCM)
