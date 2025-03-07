[project]
name = "QA_automation_phone"
version = "0.1.0"
description = "Automation test for phone"
readme = "README.md"
requires-python = ">=3.7"  # Đảm bảo đúng cú pháp
license = { text = "GNU General Public License v3" }

authors = [
    { name = "Thoang", email = "nhothoang@gmail.com" }
]

dependencies = [
    "uiautomator2>=3.2.8,<4.0"
]

[project.urls]
Documentation = "https://github.com/NhoThoang/QA_phone_automation/blob/main/README.md"
Source = "https://github.com/NhoThoang/QA_phone_automation.git"
Tracker = "https://github.com/NhoThoang/QA_phone_automation/issues"

[build-system]
requires = ["setuptools>=40.8.0", "wheel"]
build-backend = "setuptools.build_meta"

[tool.setuptools]
license-files = ["LICENSE"]
