import os

from sqlalchemy import create_engine, text

db_conn_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conn_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(dict(row._mapping))
    return jobs


def load_job(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :id"),
                          {"id": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    return dict(rows[0]._mapping)


def add_application(job_id, application):
  with engine.connect() as conn:
    query = text(
        "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :name, :email, :linkedIn, :education, :workExperience, :resume)"
    )

    conn.execute(
        query, {
            "job_id": job_id,
            "name": application["name"],
            "email": application["email"],
            "linkedIn": application["linkedIn"],
            "education": application["education"],
            "workExperience": application["workExperience"],
            "resume": application["resume"]
        })
