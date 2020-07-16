from app.website import db


class Role(db.Model):

    __tablename__ = 'role'

    assignment_id = db.Column(db.Integer, primary_key=True)
    demand_type = db.Column(db.String, nullable=False)
    career_track = db.Column(db.String, nullable=False)
    location_radius = db.Column(db.String, nullable=False)
    source_location = db.Column(db.String, nullable=False)
    gu = db.Column(db.String, nullable=False)
    assignment_fulfillment_entity = db.Column(db.String, nullable=False)
    client = db.Column(db.String, nullable=False)
    project = db.Column(db.String, nullable=False)
    project_metro_city = db.Column(db.String, nullable=False)
    project_supervising_entity = db.Column(db.String, nullable=False)
    project_client_supply_demand_specialist = db.Column(db.String, nullable=False)
    sold = db.Column(db.Boolean, nullable=False)
    gcp_preference = db.Column(db.Boolean, nullable=False)
    client_contract_based = db.Column(db.Boolean, nullable=False)
    assignment_title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    fulfillment_channel = db.Column(db.String, nullable=False)
    created_date = db.Column(db.Date, nullable=False)
    source = db.Column(db.String, nullable=False)
    requested_start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String, nullable=False)
    career_level_from = db.Column(db.Integer, nullable=False)
    career_level_to = db.Column(db.Integer, nullable=False)
    talent_segment = db.Column(db.String, nullable=False)
    assigned_role = db.Column(db.String, nullable=False)
    work_location = db.Column(db.String, nullable=False)
    assignment_primary_specialization_level_one = db.Column(db.String, nullable=False)
    assignment_primary_specialization_level_two = db.Column(db.String, nullable=False)
    assignment_primary_specialization_level_three = db.Column(db.String, nullable=False)
    assignment_primary_specialization_level_four = db.Column(db.String, nullable=False)
    assignment_primary_specialization_level_five = db.Column(db.String, nullable=False)
    assignment_primary_specialization_paths = db.Column(db.String, nullable=False)
    skill_and_proficiency = db.Column(db.String, nullable=False)
    primary_contact = db.Column(db.String, nullable=False)
    assignment_audit = db.Column(db.String, nullable=False)
    role_client_supply_demand_specialist = db.Column(db.String, nullable=False)
    candidates = db.Column(db.Integer, nullable=False)

    def __init__(self, assignment_id, demand_type, career_track, \
                location_radius, source_location, gu, \
                assignment_fulfillment_entity, client, project, \
                project_metro_city, project_supervising_entity, \
                project_client_supply_demand_specialist, sold, \
                gcp_preference, client_contract_based, assignment_title, \
                description, fulfillment_channel, created_date, source, \
                requested_start_date, end_date, status, career_level_from, \
                career_level_to, talent_segment, assigned_role, work_location, \
                assignment_primary_specialization_level_one, \
                assignment_primary_specialization_level_two, \
                assignment_primary_specialization_level_three, \
                assignment_primary_specialization_level_four, \
                assignment_primary_specialization_level_five, \
                assignment_primary_specialization_paths, \
                skill_and_proficiency, primary_contact, assignment_audit, \
                role_client_supply_demand_specialist, candidates):

        self.assignment_id = assignment_id
        self.demand_type = demand_type
        self.career_track = career_track
        self.location_radius = location_radius
        self.source_location = source_location
        self.gu = gu
        self.assignment_fulfillment_entity = assignment_fulfillment_entity
        self.client = client
        self.project = project
        self.project_metro_city = project_metro_city
        self.project_supervising_entity = project_supervising_entity
        self.project_client_supply_demand_specialist = project_client_supply_demand_specialist
        self.sold = sold
        self.gcp_preference = gcp_preference
        self.client_contract_based = client_contract_based
        self.assignment_title = assignment_title
        self.description = description
        self.fulfillment_channel = fulfillment_channel
        self.created_date = created_date
        self.source = source
        self.requested_start_date = requested_start_date
        self.end_date = end_date
        self.status = status
        self.career_level_from = career_level_from
        self.career_level_to = career_level_to
        self.talent_segment = talent_segment
        self.assigned_role = assigned_role
        self.work_location = work_location
        self.assignment_primary_specialization_level_one = assignment_primary_specialization_level_one
        self.assignment_primary_specialization_level_two = assignment_primary_specialization_level_two
        self.assignment_primary_specialization_level_three = assignment_primary_specialization_level_three
        self.assignment_primary_specialization_level_four = assignment_primary_specialization_level_four
        self.assignment_primary_specialization_level_five = assignment_primary_specialization_level_five
        self.assignment_primary_specialization_paths = assignment_primary_specialization_paths
        self.skill_and_proficiency = skill_and_proficiency
        self.primary_contact = primary_contact
        self.assignment_audit = assignment_audit
        self.role_client_supply_demand_specialist = role_client_supply_demand_specialist
        self.candidates = candidates


    def __repr__(self):
        return f'<title {self.body}>'
