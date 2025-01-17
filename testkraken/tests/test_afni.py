import os, pdb
import pytest

from ..testrunner import runner

Workflows_main_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                "../../workflows4regtests", "afni",)
workflows_list = [os.path.join(Workflows_main_dir, workf) for workf in next(os.walk(Workflows_main_dir))[1]]

@pytest.mark.parametrize("workflow_dir", workflows_list)
def test_afni_examples(workflow_dir):
    print(workflow_dir)
    try:
        runner(workflow_dir)
    except Exception as e:
        print(e)
        assert False
