from resume_scraper import scraper as rs
from description_scraper import scraper as ds

# both arguments contain lists of words. All this method is doing
# is finding what they have in common
def match(project_descriptions, resume_words, user_career_level):
    lengths = set()
    assignment_matching = dict()
    for key in project_descriptions.keys():
        # project_descriptions[key]['words'] contains descriptive words from:
        # description, talent segment, assigned role, and skills and proficiencies
        intersection = set(project_descriptions[key]['words']) & set(resume_words)
        # used a set here, not to have to deal with duplicates
        # print(len(intersection)) if len(intersection) != 0 else False
        lengths.add(len(intersection))
    for key in project_descriptions.keys():
        intersection = set(project_descriptions[key]['words']) & set(resume_words)
        assignment_matching[key] = len(intersection)/max(lengths)*careerLevelMatch(int(project_descriptions[key]['career_level_to']), int(project_descriptions[key]['career_level_from']), user_career_level)
        # print(assignment_matching[key]*10)
    # print("Max length: ", max(assignment_matching.values())*10)
    # print("Min length: ", min(assignment_matching.values())*10)
    return assignment_matching

def careerLevelMatch(cto, cfrom, actual):
    # schema is if they are too low (eg they are 11 and the position starts at 9)
    # then they are discouraged from applying
    # if they are only 1 away then they aren't discouraged from applying as they should grow
    # if they are in the range then they should definitely apply
    # if they are higher rank then they shouldn't apply
    if actual-1 > cfrom: return .75
    elif actual-1 == cfrom: return 1
    elif cto <= actual <= cfrom: return 1.25
    else: return 0



# important characteristics
# career level

if __name__ == '__main__':
    match(ds(), rs("resume.pdf"), 11)
