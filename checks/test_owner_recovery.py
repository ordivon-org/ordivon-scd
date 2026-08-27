from __future__ import annotations

import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SCDOwnerRecoveryTests(unittest.TestCase):
    def test_current_authority_pointer_matches_publication_bytes(self) -> None:
        current = json.loads((ROOT / "authority" / "CURRENT.json").read_text(encoding="utf-8"))
        publication = ROOT / current["publication"]
        actual = "sha256:" + hashlib.sha256(publication.read_bytes()).hexdigest()
        self.assertEqual(actual, current["currentAuthorityVersionRef"])

    def test_recovered_research_manifest_is_byte_exact(self) -> None:
        manifest = json.loads(
            (ROOT / "RECOVERED-RESEARCH-ARTIFACTS-20260827.json").read_text(encoding="utf-8")
        )
        self.assertFalse(manifest["semanticStandingChange"])
        self.assertEqual(manifest["sourceRepository"], "ordivon-computing")
        self.assertGreaterEqual(len(manifest["artifacts"]), 14)
        for item in manifest["artifacts"]:
            path = ROOT / item["path"]
            self.assertTrue(path.is_file(), item["path"])
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            self.assertEqual(digest, item["sha256"], item["path"])
            self.assertRegex(item["sourceComputingRevision"], r"^[0-9a-f]{40}$")

    def test_authority_named_current_instruments_are_owner_native_recoverable(self) -> None:
        current = json.loads((ROOT / "authority" / "CURRENT.json").read_text(encoding="utf-8"))
        publication = json.loads((ROOT / current["publication"]).read_text(encoding="utf-8"))
        corpus = json.dumps(publication, ensure_ascii=False)
        required = {
            "K0.2": ROOT / "formalization" / "K0.2-ROLE-MODEL.md",
            "CF-v0.1": ROOT / "formalization" / "CF-v0.1-CANONICAL-FALSIFICATION-CORPUS.md",
            "A1-A8": ROOT / "applied" / "CROSS-CONSUMER-FINDINGS-v0.2.md",
        }
        for token, path in required.items():
            self.assertIn(token, corpus)
            self.assertTrue(path.is_file(), str(path))

    def test_owner_readme_links_recovered_surfaces(self) -> None:
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        for target in ("formalization/README.md", "applied/README.md", "RECOVERED-RESEARCH-ARTIFACTS-20260827.json"):
            self.assertIn(target, text)
            self.assertTrue((ROOT / target).exists(), target)

    def test_semantic_firewall_regressions_remain_explicitly_recoverable(self) -> None:
        fixture = json.loads(
            (ROOT / "checks" / "semantic-firewall-regressions.json").read_text(encoding="utf-8")
        )
        self.assertEqual(fixture["truthRole"], "non-authoritative-executable-recovery-guard")
        for case in fixture["cases"]:
            text = (ROOT / case["sourcePath"]).read_text(encoding="utf-8")
            for term in case["requiredTerms"]:
                self.assertIn(term, text, case["id"])
            left, right = map(re.escape, case["requiredTerms"])
            negative = re.compile(left + r".{0,80}(?:!=|≠|not imply|does not imply).{0,80}" + right, re.I | re.S)
            reverse = re.compile(right + r".{0,80}(?:!=|≠|not imply|does not imply).{0,80}" + left, re.I | re.S)
            self.assertTrue(negative.search(text) or reverse.search(text), case["id"])


if __name__ == "__main__":
    unittest.main()
