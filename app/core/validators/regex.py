import re

CPF_REGEX = r'^\d{11}$'
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'
NOME_REGEX = r'^[A-Za-zÀ-ÖØ-öø-ÿ]{2,}(?:\s+[A-Za-zÀ-ÖØ-öø-ÿ]{2,})+$'