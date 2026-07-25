#!/usr/bin/env python3
"""Validate that all skills follow the WHAT/WHY/WHERE/WHEN/HOW framework."""

import os
import re
import sys

REQUIRED_SECTIONS = ["WHAT", "WHY", "WHERE", "WHEN", "HOW"]
SKILLS_DIR = "skills"

def validate_skill(skill_path):
    errors = []

    if not os.path.exists(skill_path):
        return [f"  MISSING: {skill_path}"]

    with open(skill_path, "r") as f:
        content = f.read()

    for section in REQUIRED_SECTIONS:
        pattern = rf"^#+\s*{section}\b"
        if not re.search(pattern, content, re.MULTILINE):
            errors.append(f"  MISSING section: {section}")

    secret_patterns = [
        r"api[_-]?key\s*[=:]\s*['\"][^'\"]+['\"]",
        r"token\s*[=:]\s*['\"][^'\"]+['\"]",
        r"password\s*[=:]\s*['\"][^'\"]+['\"]",
    ]
    for pattern in secret_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            errors.append("  POSSIBLE HARDCODED SECRET detected")

    return errors

def main():
    print("=" * 50)
    print("  Agent Skills Validator")
    print("  WHAT / WHY / WHERE / WHEN / HOW")
    print("=" * 50)
    print()

    if not os.path.exists(SKILLS_DIR):
        print(f"ERROR: {SKILLS_DIR}/ directory not found")
        sys.exit(1)

    total = 0
    passed = 0
    failed = 0

    for domain in sorted(os.listdir(SKILLS_DIR)):
        domain_path = os.path.join(SKILLS_DIR, domain)
        if not os.path.isdir(domain_path):
            continue

        for skill_name in sorted(os.listdir(domain_path)):
            skill_dir = os.path.join(domain_path, skill_name)
            if not os.path.isdir(skill_dir):
                continue

            skill_file = os.path.join(skill_dir, "SKILL.md")
            total += 1
            errors = validate_skill(skill_file)

            if errors:
                failed += 1
                print(f"FAIL  {domain}/{skill_name}")
                for e in errors:
                    print(e)
                print()
            else:
                passed += 1
                print(f"PASS  {domain}/{skill_name}")

    print()
    print("-" * 50)
    print(f"  Total: {total}  |  Passed: {passed}  |  Failed: {failed}")
    print("-" * 50)

    if failed > 0:
        print("\n  Fix the issues above and re-run.")
        sys.exit(1)
    else:
        print("\n  All skills valid!")
        sys.exit(0)

if __name__ == "__main__":
    main()
