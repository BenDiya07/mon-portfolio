from flask_frozen import Freezer
from app import app, projects_data

freezer = Freezer(app)

@freezer.register_generator
def project_detail():
    for project in projects_data:
        yield {'project_id': project['id']}

if __name__ == '__main__':
    freezer.freeze()
