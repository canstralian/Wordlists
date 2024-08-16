---
license: mit
---

# Password List Collection

## Dataset Summary
The Password List Collection is a compilation of commonly used passwords, leaked passwords from security breaches, and other password-related data. The dataset is intended for cybersecurity research, including the study of password strength, the development of password policies, and the improvement of password hashing algorithms.

**Important Note:** This dataset is for research purposes only. Using it for malicious activities, including unauthorized access to systems or accounts, is illegal and unethical.

## Supported Tasks and Leaderboards
- **Password Strength Analysis:** Assessing the strength of passwords and identifying common patterns.
- **Security Research:** Developing and testing password-related algorithms, including password hashing, password cracking, and secure password storage.
- **Educational Purposes:** Teaching about cybersecurity, password hygiene, and data privacy.

## Languages
The dataset primarily contains passwords in English, but may include passwords in other languages due to the nature of the data sources.

## Dataset Structure

### Data Instances
Each instance in the dataset represents a single password entry. Depending on the source, entries might also include associated metadata such as the hash of the password, the original breach source, or the frequency of occurrence.

Example:
```
{
    "password": "123456",
    "hash": "e10adc3949ba59abbe56e057f20f883e",
    "source": "RockYou",
    "frequency": 3456789
}
```

### Data Fields
- **password:** `string` - The plaintext password.
- **hash:** `string` (optional) - The hashed representation of the password.
- **source:** `string` (optional) - The source of the password list (e.g., RockYou, LinkedIn breach).
- **frequency:** `int` (optional) - The frequency of the password in the dataset, if applicable.

## Data Splits
The dataset may be divided into various splits based on the source of the data or the type of password (e.g., common passwords vs. breached passwords).

Example:
- **train:** Contains a broad set of passwords used for developing models or algorithms.
- **test:** Contains a smaller set of passwords reserved for testing.

## Dataset Creation

### Curation Rationale
This dataset was curated to provide researchers and developers with a resource for studying password-related issues. The passwords were collected from publicly available sources, including password leaks and security reports.

### Source Data
- **Initial Data Collection and Processing:** The passwords were collected from public data breaches and other accessible sources. Each password was processed to remove personally identifiable information (PII) and to ensure compliance with ethical guidelines.

- **Considerations for Using the Data:**
  - **Legal:** The dataset is composed of data already made public. However, users must comply with legal and ethical standards when using this dataset.
  - **Ethical:** This dataset should only be used for lawful research and education. Misuse of this dataset is strictly prohibited.

## Uses

### Primary Intended Uses
The dataset is intended for:
- Research in password security and cryptography.
- Development and testing of password management tools.
- Educational use in cybersecurity courses.

### Out-of-Scope Use Cases
- Any form of illegal activity, including unauthorized access to systems.
- Attempts to crack or decrypt passwords in a manner that violates ethical or legal standards.

## Dataset Curators
The dataset was curated by [Your Name/Organization], with the goal of supporting cybersecurity research and education.

## Licensing Information
This dataset is distributed under the [Appropriate License, e.g., Creative Commons License CC BY-NC 4.0], which permits non-commercial use only.

## Citation
If you use this dataset, please cite:
```
@dataset{your_name_2024_password_list_collection,
  title        = {Password List Collection},
  author       = {Your Name/Organization},
  year         = 2024,
  publisher    = {Your Publisher},
  url          = {URL to the dataset},
}
```

## Contributions
We welcome contributions to improve this dataset. Please submit issues or pull requests via [repository link, if applicable].