# BrightPost

brightpost.org: a guide for the neurodivergent community and the people who support it. A program of GOVW Foundation, Inc. (planned).

- `site/`: the static site (no third-party scripts, self-hosted Atkinson Hyperlegible font under the SIL Open Font License).
- `scripts/build.py`: builds every page in `site/` from one file (`python3 scripts/build.py`).
- `scripts/deploy-aws.sh`: one-time AWS setup (private S3 bucket, CloudFront, ACM certificate, Route 53) and upload, run from CloudShell.

BrightPost is a guide, not a clinic. Nothing here is medical, psychological or legal advice.
