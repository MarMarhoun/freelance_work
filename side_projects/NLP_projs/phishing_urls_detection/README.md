# Phishing URLs detection using PhishStorm dataset & SVM, XGBoost and Random Forest algorithms.

## Project Description:

Phishing is a form of fraud in which the attacker tries to learn sensitive information such as login credentials or account information by sending as a reputable entity or person in email or other communication channels.

Typically a victim receives a message that appears to have been sent by a known contact or organization. The message contains malicious software targeting the user’s computer or has links to direct victims to malicious websites in order to trick them into divulging personal and financial information, such as passwords, account IDs or credit card details.

## Dataset Description:

URLs dataset with features built and used for evaluation in the paper "[PhishStorm](https://research.aalto.fi/en/datasets/phishstorm-phishing-legitimate-url-dataset): Detecting Phishing with Streaming Analytics" published in IEEE TNSM.
The dataset contains 96,018 URLs: 48,009 legitimate URLs and 48,009 phishing URLs.

This is a CSV file where the "domain" column provides a unique identifier for each entry (which is actually a URL). The "label" column provides the domain entry status, 0: legitimate / 1:phishing.
