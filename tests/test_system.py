from orchestration.orchestrator import run
def test_gate(): assert run({'human_approval':False})['review']['approved'] is False
