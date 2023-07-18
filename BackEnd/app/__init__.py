# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:35:06 2023

@author: 86136
"""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__,
            template_folder="../../FrontEnd/dist",
            static_folder="../../FrontEnd/dist",
            static_url_path="")
# 跨域
CORS(app)

from app import routes