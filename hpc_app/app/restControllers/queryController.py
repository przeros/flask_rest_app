from flask import render_template, request, url_for, redirect
from app.db.db import db
from sqlalchemy import asc, desc, func, extract, cast, text
from sqlalchemy import create_engine

engine = create_engine("postgresql://hpc_app:hpc_app@db:5432/hpc_app")


def index():
    return render_template("index.html")

    