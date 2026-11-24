"""Alien Field Notes: The Two Day Earth Review — variant C.

Concept: an alien tourist reviews humans who are unfailingly polite to
machines — saying "please" and "thank you" to toasters, lifts and voice
assistants, then apologising to chairs they bump into. The tourist's
conclusion is the joke: Earth must be ruled by its appliances, who are
too polite to admit it. One concrete scene, one clean punch, rating
mid-line ("4/5 stars") so the punch lands on the final words.

Iteration (one concept, v1 -> v8, wording/timing/punch only):
  v1 (197): "...I now believe Earth is ruled by its appliances.
              4/5 stars, would visit again." — punch buried mid-line.
  v2 (193): "Clearly Earth is ruled by very polite appliances." — same flaw.
  v3 (206): over 200 chars, dropped.
  v4 (207): "Two days on Earth:" opener, over 200 chars, dropped.
  v5 (192): rating moved mid-line, verdict last — SHIPPED.
  v6 (213): "...would visit again if the toaster allows it." — punch
            stronger but over 200 chars, dropped.
  v7 (210): "...if the toaster permits it." — over 200 chars, dropped.
  v8 (227): "...waiting for the toaster to approve my return trip."
            — over 200 chars, dropped.

Final line: 192 characters.
"""

import os

LINE = "Humans say please and thank you to toasters, lifts and voice assistants, then apologise to chairs they bump into. 4/5 stars. My conclusion: Earth is ruled by appliances too polite to admit it."


def main():
    # Write /output FIRST: the grader sandbox mounts the repo read-only,
    # so the repo-root copy must never be allowed to crash the run.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    try:
        with open(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"),
            "w",
            encoding="utf-8",
        ) as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
