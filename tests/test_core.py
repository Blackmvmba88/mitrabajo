import unittest
from blackmamba.core import Orchestrator, Policy, triage

class CoreTests(unittest.TestCase):
    def test_default_deny(self):
        with self.assertRaises(PermissionError):
            Orchestrator(Policy()).run("triage", {})

    def test_unknown_tool(self):
        with self.assertRaises(PermissionError):
            Orchestrator(Policy(frozenset({"shell"}))).run("shell", {})

    def test_allowed(self):
        self.assertEqual(Orchestrator(Policy(frozenset({"triage"}))).run("triage", {"failed_logins": 12})["priority"], "high")

    def test_thresholds(self):
        for n, expected in [(0,"low"),(2,"low"),(3,"medium"),(9,"medium"),(10,"high")]:
            with self.subTest(n=n):
                self.assertEqual(triage({"failed_logins":n})["priority"], expected)

    def test_invalid(self):
        for n in [-1, True, "12", 1.5, 1000001]:
            with self.subTest(n=n), self.assertRaises(ValueError):
                triage({"failed_logins":n})

if __name__ == "__main__":
    unittest.main()
